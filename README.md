# Folder_Prettify
Suppose you have a folder, and its path is also given. You have to create a function which takes three input arguments, which are:

def soldier("C://", "file.txt", "jpg")

Full Path of the folder as input strings.
Dictionary file
File Format
The function will perform three tasks:

First, it will check all the files present in the folder whose paths are given as an input argument.
Then it will capitalize the first letter of each file. If the name of the file is present in a dictionary file then it will not capitalize the first letter. It will only capitalize the first letter of the files, which are not present in the dictionary file. 
The function renames the file names to number in range of 1 to100 whose format is the same as mentioned in the input parameter like 1.jpg.
After performing these tasks, your folder will prettify as all the first letters of the files in the folder will be capitalize except for those files whose names are present in the dictionary file. And the files having the same format as given in the input argument will rename to number in the range of 1-100.
