# ^         Matches the beginning of a line
# $         Matches the end of the line
# .         Matches any character
# \s        Matches whitespace
# \S        Matches any non-vhitespace character
# *         Fepeats a character zero or more times
# *?        Repeate a character zero or more times (non-greedy)
# +         Repeats a character one or more times
# +?        Repeats a character one or more times (non-greedy)
# [aeiou]   Matches a single character in the listed set
# [^XYZ]    Matches a single character not in the listed set
# [a-z0-9]  The set of characters can include a cange
# (         Indicates where string extraction is to start
# )         Indicates where string extraction is to end

# como uso exp regulares en python
import re

# uso del search()

#  
hand = open ( 'mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print (line)

# es igual a

import re

hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print (line)

#######################################

hand = open ( 'mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:') >= 0:
        print (line)

# es igual a

import re

hand = open ('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print (line)
        
# findall(REGEXP, string)
import re
x = "string"
y = re.findall('[a-z]+', x)


