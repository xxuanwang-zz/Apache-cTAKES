import re
import os
'''
Afer running Apache cTAKES , Get the file names and extensions of two output files.
'''
def get_filename(FilePath):
    File_Name = []
    Text_Name = []
    File_List = []
    #SUM = 0
    for i in os.listdir(FilePath):
        
        text_name = os.path.splitext(i)[0].split('.')[0]
        if not text_name in Text_Name:
            Text_Name.append(text_name) # All the names of output files without extension
    
        file_name = os.path.splitext(i)[0]
        file_extension = os.path.splitext(i)[1]
        
        if not file_name in File_Name:
            File_Name.append(file_name + file_extension) # name + extension in ONE list
        
    for n in range(len(Text_Name)):
        file = [] # Collect all files which have the same text name
        for f in range(len(File_Name)):
            if re.findall(r'^%s.*?' % Text_Name[n], File_Name[f]) != []:
                file.append(File_Name[f])
                file.sort()
        File_List.append(file) # name + extension in lists
                    

    return  Text_Name, File_Name, File_List
