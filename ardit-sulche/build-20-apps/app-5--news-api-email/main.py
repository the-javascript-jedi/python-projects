import requests
from send_email import send_email

api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      "890603a55bfa47048e4490069ebee18c"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    # Access the article titles and description
    body = ""
    for article in content["articles"]:
        if article["title"] is not None:
            body = body + article["title"] + "\n" + str(article["description"]) + 2 * "\n"

    body = body.encode("utf-8")
    # send_email(message=body)