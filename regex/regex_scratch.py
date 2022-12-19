import re

# Placing the r before the string passes it as a raw string. This does not allow escape characters.
# Adding parentheses will group the regex. When you then use group() you can match the object from the text from
# just one group.
# group() with a 0 returns the entire matched text
phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# Grouping with parentheses
mo = phone_regex.search('My number is 555-555-5555.')
print(mo.group(2))

# If you would like to retrieve all groups at once use groups()
print(mo.groups())