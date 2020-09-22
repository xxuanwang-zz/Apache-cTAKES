'''
For a text file which has \n in it.
'''
def text_reader(TextFilePath, InputFilePath):
    file = open(TextFilePath, "r") # Original file folder path
    lines = file.readlines()
    for index in range(len(lines)):
        text = open(InputFilePath + '/%s.txt' % index, "w+") # Input file folder path in Apache cTAKES environment
        text.write(lines[index])
        text.close()
    
    return True
