'''
The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on.
OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
'''

import os

# for Wind- "nt" & for Mac/Linux- "posix"
print("os name is-", os.name)

print("to get environment info.-", os.getenv('PATH'))

# to get the Current Working Directory:-
print("to get current working directory of the project-", os.getcwd())

'''
To create a new directory using the mkdir()-
note - we get error as OS won't allow to make two files with same name at same dir.
FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'C:/Users/dir'
'''
print(os.mkdir('C:/Users/risha/PycharmProjects/Machine_Learning_with_Python/package01/newdir'))
print("new folder/ directory is created")

# to creat dir in same project, then write dirName instead of path name
print(os.mkdir("we"))

# Note-
# 1) we can't use this (\) symbol in path (os.mkdir("C:\project\new\dir")) as we get error-
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
# Bcz (\) is escape character.
# 2) if we use print() with os fnx, then we get "None" if that fnx. doesn't return anything


# to change the Current Working Directory:-
print("to change dir location-", os.chdir("we"))
print("folder location changed")
print(os.getcwd())

# to remove any  Directory:-
os.chdir("we")
print(os.getcwd())
os.chdir('..')
os.rmdir("we")
print("folder is deleted")
print(os.getcwd())

# to get the list of all files and directories in the specified directory-
# If we don't specify any directory, then list of files and directories in the current working directory will be returned.
print(os.listdir("C:/Users/risha/PycharmProjects/Machine_Learning_with_Python/"))

# Rename the file or directory src to dst.
os.mkdir("we")
print("folder is created")
print("now this folder ie renamed ")
os.rename("we", "dst")
