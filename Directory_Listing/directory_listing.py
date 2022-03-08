import os
from os import listdir
from os.path import isfile, join

amount = 0
extensions = []
ext_dict = {}

# Path to search for files (change before executing)
folder_path = 'C:/Users/...'

# Adding files to a list
files = [i for i in listdir(folder_path) if isfile(join(folder_path, i))]

# Counting files
for file in range(0, len(files)):
    amount = + file
    filename, extension = os.path.splitext(files[file])
    extension = extension.strip('.')
    extensions.append(extension)

# Counting extensions
for i in extensions:
    keyword = i
    if keyword in ext_dict:
        break
    ext_dict.update({i.title(): extensions.count(i)})
ext_items = ext_dict.items()

# Printing
print("\nThere are {} files in this folder\n".format(amount+1))

for i in ext_items:
    print(i)
