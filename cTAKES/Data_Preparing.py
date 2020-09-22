from TestRunner.text_reader import *

'''
Data preparation
Notice: There are two funtional python files to implement this step. The format of the input file determines which function to call.

        text_reader.py and csv_reader.py
        
        Both of the files represent the whole input data, which need to be splited into single file according to \n or cells.
'''
Original_filePath = 'C:/Users/DELL/Desktop/Data/notes_headache.txt'
Input_filePath = 'C:/apache-ctakes-4.0.0/bin/Input'
print(text_reader(Original_filePath, Input_filePath))