import re
import pandas as pd

def get_property(TXT_Filepath):
    f = open(TXT_Filepath, "r")
    lines = f.readlines()
    list_mystr = []
    for i in range(len(lines)):
        
        '''list_mystr is a important basis.'''
        
        if lines[i].isspace() == False:
            mystr = ''.join(lines[i].strip()).split('\n')
            list_mystr.extend(mystr)
    '''
    index_word: is used to storage the index of words as the beginning of the extracted text.
    semantic_annotation is used to place CUIs and semantic concepts
    Method: Find all CUIs between two indices of words and then append the semantic group to semantic_annotation list.
    Attention: Not every word only has one CUI. Some of them has more than one CUI. 
               So cui_index is used to calculate the number of CUI in a given list_mystr slice.
    '''
    index_word = []
    for i in range(len(list_mystr)):
        if re.findall(r'^(["].*?["])', list_mystr[i]) != []:
            index_word.append(i)
    index_word.append(len(list_mystr))  # print(index_word)
    
    semantic_annotation = []
    for i in range(len(index_word) - 1):
        cui_index = []
        for j in range(index_word[i], index_word[i+1]):
            if re.findall(r'^C[0-9]\d{6}.*?$', list_mystr[j]) != []:
                cui_index.append(j)
        #print(cui_index)
    
        if len(cui_index) > 1:
            for element in cui_index:
                copy_semantic_group = list_mystr[index_word[i]: index_word[i] + 2]
                copy_semantic_group.append(list_mystr[element])
                #print(copy_semantic_group)
                semantic_annotation.append(copy_semantic_group)
        elif len(cui_index) == 1:
            semantic_annotation.append(list_mystr[index_word[i]: index_word[i] + 3])    
         
    #print(semantic_annotation)  
    
    '''Convert txt file into csv file'''
    
    df = pd.DataFrame(semantic_annotation, columns = ['Word', 'Semantic Types', 'Annotation']) #
    df['Negation'] = df['Word'].map(lambda x: "Negated" if 'negated' in x else "Null")
    df['Word'] = df['Word'].map(lambda x : re.findall(r'^["](.*?)["]', x)[0])

    df['CUI'] = df['Annotation'].map(lambda x: x.split(' ')[0])     
    df['Semantic Concept'] = df['Annotation'].map(lambda x: ' '.join(x.split(' ')[1:]))

    df['Words'] = df.groupby(['CUI', 'Negation'])['Word'].transform(lambda x: ','.join(x))
    
    for index, row in df['Words'].iteritems():
        new_word = []
        for i in row.split(','):
            if not i in new_word:
                new_word.append(i)
        df.loc[index, 'Words'] = ', '.join(new_word)
        
        df = df[['CUI', 'Words', 'Negation', 'Semantic Types', 'Semantic Concept']].drop_duplicates()
          
    return df