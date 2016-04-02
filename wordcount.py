#Program for wordcount

import re
line = raw_input('Enter your phrase :')
count = len(re.findall(r'\w+',line))
print (count)