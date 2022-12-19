"""
While * means match zero or more, the + means match one or more.
Unlike the star, the group preceding a plus must appear at least once. It is not optional.
"""

import re
bat_regex = re.compile(r'Bat(wo)+man')

mo1 = bat_regex.search('The Adventures of Batwoman')
mo2 = bat_regex.search('The Adventures of Batman')
print(mo1.group())
print(mo2 is None)
