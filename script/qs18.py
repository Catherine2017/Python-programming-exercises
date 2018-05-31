import re

items = input().split(',')
rights = []
for p in items:
    if 6 <= len(p) <= 12:
        if re.search(r'[a-z]', p):
            if re.search(r'\d', p):
                if re.search(r'[A-Z]', p):
                    if re.search(r'[$#@]', p):
                        rights.append(p)
print(','.join(rights))
