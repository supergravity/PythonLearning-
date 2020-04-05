# os library exercise

import os

print('exercise 1')
# 1. Getting the PATH of the system (os.environ -> getting the parameters of the system)
path=os.environ.get('PATH')
print(path)

print()
print('exercise 2')

# 2. Getting the PATH of home directory of the user

home_path = os.path.expanduser('~')
print(home_path)

print()
print('exercise 3')

# 3. Getting the PATH of a file 

pict_path = os.path.join(home_path, 'Pictures', 'Batman.jpg')
print(pict_path)

print()
print('exercise 4')

# 4. Listing the directory 

output = os.listdir(home_path)
print(output)

print()
print('exercise 5')

# 5. Getting the current working directory

cwd = os.getcwd() # -> NO input NEEDED !!!
print(cwd)

print()
print('exercise 6')

# 6. Changing the directory

chdir = os.chdir(home_path)
print(chdir)

print()
print('exercise 7')

# 7. Making a directory

mkdir = os.mkdir('The_dark_knight')

print()
print('exercise 8')

# 8. Deleting the directory

# os.rmdir('The_dark_knight')

print()
print('exercise 9')

# 9. Renaming the file

os.rename('The_dark_knight','The_Joker') # -> Inserting two strings: the old file name and the new one
output = os.listdir(home_path)
print(output)
print()
os.rmdir('The_Joker')
output = os.listdir(home_path)
print(output)


print()
print('exercise 10')
# 10. Removing file

os.chdir('/home/liam/Pictures/') # -> Inserting string
#os.remove('Batman.jpg') # -> Inserting string

print()
print('exercise 11')
# 11. Checking the status of a file 

stat = os.stat('Batman.jpg') # -> Inserting string
print(stat)

print()
print('exercise 12')
# 12. Browsing the path of the whole directory

walk = os.walk('/home/liam/Pictures') # -> Inserting string  
print(walk)

print()
print('exercise 13')
# 13. Checking whether files or directories
isfile = os.path.isfile('/home/liam/Pictures')
print(isfile)
print()
isdir  = os.path.isdir('/home/liam/Pictures')
print(isdir)
print()

