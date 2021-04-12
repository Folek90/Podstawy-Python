
import os

path = r'c:\Users\user\documents\Cwiczenia_LAB\README.txt'

#os.remove(path)

"""
if s.path.isfile(path):
    print('File % exist', % path)
else:
    print('Creating a file %s' % path)
    open(path,'x').close()
    print('File %s created' % path)
"""

result = os.path.isfile(path) or open(path, 'x').close()
print(result)

