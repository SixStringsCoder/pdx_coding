import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# print(re.match(r'Love', data))
# print(re.search(r'Andrew', data))
#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}',data))
#print(re.findall(r'\w*, \w*', data))
#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
#print(re.findall(r'\b[trehous]{9}\b', data, re.I))
#print(re.findall(r'''
#    \b@[-\w\d.]*
#    [^gov\t]+
#    \b
#''', data, re.VERBOSE|re.I))
#print(re.findall(r'''
#   \b[-\w]+,
#   \s
#   [-\w ]+
#   [^\t\n]
#''', data, re.X))
line = re.search(r'''
    ^(?P<name>[-\w]*,\s[-\w ]+)\t # last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # email address
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # tel. number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # job and company
    (?P<twitter>@[\w\d]+)?$ # twitter
''', data, re.X|re.MULTILINE)
print(line)
print(line.groupdict())

