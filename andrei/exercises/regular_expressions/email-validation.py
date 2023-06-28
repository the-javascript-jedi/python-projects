import re

# email validation
email_pattern = re.compile(r"^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$")
string="Andressis.me@gmail.com"
a=email_pattern.search(string)
print(a)
# None is printed if there is no match with the string

# Password validation
# password must be 8 characters long, contains letters and numbers with special characters $%#@
password_pattern=re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
string="Andressis8dd"
b=password_pattern.fullmatch(string)
print(b)