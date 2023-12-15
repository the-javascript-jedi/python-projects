import requests
from send_email import send_email

topic = "tesla"

api_key = "bdf4c47abecd4d0f9f3979485f5f9a33"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&apiKey=" \
      "bdf4c47abecd4d0f9f3979485f5f9a33" \
      "&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news\n\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + str(article["title"]) + "\n" + str(article["description"]) + str(
            article["url"]) + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
