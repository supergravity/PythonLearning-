# Browsing the Directory

import os 

path = r'/home/liam/Pictures'

# dir_path and dir_names and file_names are list

for dir_path, dir_names, file_names in os.walk(path):
    print('current path:', dir_path)

    if len(dir_names) != 0:
        print('subdir:', dir_names)
    else:
        print('There are no subdirs in this dir')

    if len(file_names) != 0:
        print('File:', file_names)
    else:
        print('There are no files in the dir')


    for f in file_names:
        print('The complete path of the files:', os.path.join(dir_path,f))
