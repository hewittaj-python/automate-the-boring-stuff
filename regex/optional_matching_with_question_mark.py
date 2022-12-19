"""
Sometimes there is a pattern that you want to match only optionally. The '?' character flags the group that precedes
it as an optional part of the pattern.
"""
import re

bat_regex = re.compile(r'Bat(wo)?man')
mo = bat_regex.search('The adventures of Batman')
mo2 = bat_regex.search('The adventures of Batwoman')
print(mo.group())
print(mo2.group())
