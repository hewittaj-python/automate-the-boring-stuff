"""
If you have a group that you want to repeat a specific number of times, follow the group in your regex with a number
in curly brackets.
For example, the regex (Ha){3} will match 'HaHaHa'

Instead of one number, you can specify a range by writing a minimum, a comma, and a maximum between curlies.

So regex (Ha){3, 5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'
"""
import re

ha_regex = re.compile(r'(Ha){3}')
mo1 = ha_regex.search('HaHaHa')

print(mo1.group())