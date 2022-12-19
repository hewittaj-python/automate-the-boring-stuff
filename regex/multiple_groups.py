"""
You can match multiple groups with the Pipe ( | ) symbol. You can use it anywhere you want to match one of many
expressions.

For example the regex r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'.

When both Batman and Tina Fey occur in the searched string, the first occurrence of matching text will be returned as
the Match object.
"""
import re

hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey.')
print(mo1.group())

""" 
You can also use the pipe to match one of several patterns as part of your regex. Say you wanted to match any of the 
strings 'batman', 'batmobile', 'batcopter', 'batbat'
"""
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
