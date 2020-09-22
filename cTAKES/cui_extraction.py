import pandas as pd

def cui_extraction(BSV_Filepath):
    
    df_original = pd.read_csv(BSV_Filepath, sep = '|', header = None)
    df_original.columns = ['CUI', 'Count']
    
    df_new = pd.DataFrame(columns = ['CUI', 'Count', 'Negation'])
    df_new['Negation'] = df_original['CUI'].map(lambda x: "Negated" if '-' in x else "Null")
    df_new['CUI'] = df_original['CUI'].map(lambda x: x.replace('-', ''))
    df_new['Count'] = df_original['Count']
    
    return df_new
