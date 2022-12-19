"""
The * means match zero or more. The group that precedes the star can occur any number of times in the text.
"""
import re

bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The Adventures of Batman')
mo3 = bat_regex.search('The Adventures of Batwowowowoman')
print(mo1.group())
print(mo3.group())