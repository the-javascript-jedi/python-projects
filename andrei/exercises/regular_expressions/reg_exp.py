# re - regular expression
# test in regex 101 website
#  https://regexone.com/lesson/introduction_abcs -- regex exercise
import re

string="search inside of this text please this!"

a=re.search("this",string)

# span - tells where search string occurs and ends
print("a.span()",a.span())
# O/P - a.span() (17, 21)

# start - tells where search string starts
print("a.start()",a.start())
# O/P - a.start() 17

# start - tells where search string ends
print("a.end()",a.end())
# O/P - a.end() 21

# using pattern
pattern = re.compile('this')
# pattern.search
a=pattern.search(string)
print("a.group()",a.group())
# O/P - a.group() this

# find all instances of the match
b=pattern.findall(string)
print("b",b)
# O/P - b ['this', 'this']

# full match the entire searched string exactly
c=pattern.fullmatch(string)
print("c",c)
#O/P - c None