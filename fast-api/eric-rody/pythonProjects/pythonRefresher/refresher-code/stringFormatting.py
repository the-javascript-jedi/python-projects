"""
String Formatting
"""
first_name="NS"
# normal formatting
print("Hi "+first_name)
#f- formatting
print(f"Hi {first_name}")
# .format notation
sentence1 = "Hi {}"
print(sentence1.format(first_name))

# .format notation two strings
sentence2="Hi {} {}"
first_name="NS"
last_name="Samuel"
print(sentence2.format(first_name,last_name))

# f string formatting two strings
print(f"Hi {first_name} {last_name} I hope you are learning")




