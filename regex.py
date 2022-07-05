import re
str="""RegExr was created by gskinner.com, and is proudly hosted by Media Temple.

Edit the Expression & Text to see 192.168.99.144 matches. Roll over matches or the expression for details. PCRE & JavaScript flavors of RegEx are  199.244.45.98 (supported. Validate your expression with Tests mode.

The side bar includes a Cheatsheet, full Reference, and Help. You can also Save & Share with the Community, and view patterns you create or favorite in My Patterns.

Explore results with the Tools below.135.55.166.88 Replace & List output custom results. Details  10.0.0.0lists capture groups. Explain describes your expression in plain English."""

s= re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}",str)
print(s)