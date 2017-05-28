
# coding: utf-8

# In[24]:

import re
str1 = 'BIT110086  TSU111345'
str2 = '110086BIT 111345TSU'

#一次使用
match1 = re.search(r'[0-9]\d{5}', str1)
print(match1.re)
if match1:
    print(match1.group(0))

match2 = re.match(r'[0-9]\d{5}', str2)
if match2:
    print(match2.group(0))
    
match3 = re.findall(r'[0-9]\d{5}', str1)
if match3:
    print(match3)

print(re.split(r'[0-9]\d{5}', str1))

print(re.split(r'[0-9]\d{5}', str1, maxsplit=1))

for m in re.finditer(r'[0-9]\d{5}', str1):
    if m:
        print(m.group(0))

print(re.sub(r'[0-9]\d{5}', '#@@#', str1

#编译多次使用
regex = re.compile(r'[0-9]\d{5}', flags=0)


# In[29]:

match1.span()


# In[33]:

match = re.search(r'PY.*?N', 'PYabcN123N')
print(match.group(0))

#regex.py