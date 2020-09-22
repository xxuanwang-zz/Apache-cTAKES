from TestRunner.get_filename import *
from TestRunner.cui_extraction import *
from TestRunner.get_property import *


'''0. Get the output folder path which created by cTAKES'''
output_filePath = 'C:/Users/DELL/Desktop/Output'
text_name, _, file_list = get_filename(output_filePath)

df_SumCUI = pd.DataFrame()

for i in range(len(text_name)):
    '''1. Read the cuicount.bsv file'''
    
    bsv_filepath = 'C:/Users/DELL/Desktop/Output/%s' % file_list[i][0]
    df_CUI = cui_extraction(bsv_filepath)
    #df_CUI.to_csv('C:/Users/DELL/Desktop/%s.csv' % text_name[i], index = False)
    
    df_SumCUI = pd.concat([df_SumCUI, df_CUI], axis = 0, join = 'outer')
    
    '''2. Clean the data in the .txt file. And convert .txt file into .csv file'''
    txt_filepath = 'C:/Users/DELL/Desktop/Output/%s' % file_list[i][1]
    df_note = get_property(txt_filepath)
    #print(df_note.head(10))
    #df_note.to_csv('C:/Users/DELL/Desktop/Note.csv', index = False)
    
    '''3. Merge these two DataFrames together through the primary key'''
    
    df_result = df_note.merge(df_CUI, on = ['CUI', 'Negation'])
    df_result.to_csv('C:/Users/DELL/Desktop/Result/%s_RESULT.csv' % text_name[i], index = False)

df_SumCUI['Total'] = df_SumCUI.groupby(['CUI', 'Negation'])['Count'].transform(lambda x: sum(x))
df_SumCUI = df_SumCUI[['CUI', 'Negation', 'Total']].drop_duplicates()

df_SumCUI.to_csv('C:/Users/DELL/Desktop/Summary.csv', index = False)
