import pandas as pd
from TestRunner.get_filename import *

df_combine = pd.DataFrame()
file_name, name_list, _ = get_filename('C:/Users/DELL/Desktop/Result')

for i in range(len(name_list)):
    df_cui = pd.read_csv('C:/Users/DELL/Desktop/Result/%s' % name_list[i])

    df_corr = pd.DataFrame(1, index = df_cui.CUI, columns = df_cui.CUI)
    #df_corr.to_csv('C:/Users/DELL/Desktop/try_%s.csv' % file_name[i])
    #print(df_corr)
    df_combine = pd.concat([df_combine, df_corr], axis = 1)


duplicate_list = list(df_combine.columns.duplicated()

#df_combine = df_combine[df_combine.duplicated(keep = False)]
#df_combine = df_combine.groupby(df_combine.columns.tolist()).apply(lambda x: tuple(x.index)).tolist()
#print(df_combine) 
print(duplicate_list)   
#df_combine.to_csv('C:/Users/DELL/Desktop/try.csv')
