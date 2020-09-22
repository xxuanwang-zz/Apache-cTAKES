import pandas as pd
import re
import numpy as np

df = pd.read_csv('C:/Users/DELL/Desktop/Data/DIAGNOSES_ICD.csv', index_col = None, usecols = ['SUBJECT_ID', 'HADM_ID', 'ICD9_CODE'])

df['ICD9_CODE'].fillna(value = '999', inplace = True)

for index, row in df['ICD9_CODE'].iteritems():
    if re.findall(r'^[V,E].*?$', row) != []:
        df.loc[index, 'RECODE'] = '0'
    else:
        df.loc[index, 'RECODE'] = df.loc[index, 'ICD9_CODE'][0: 3: 1]

df['RECODE'] = df['RECODE'].astype(int)
# ICD-9 Main Category ranges
icd9_ranges = [(1, 140), (140, 240), (240, 280), (280, 290), (290, 320), (320, 390), (390, 460), (460, 520), (520, 580), (580, 630), (630, 680), (680, 710), (710, 740), (740, 760), (760, 780), (780, 800), (800, 1000), (0, 1)]

# Associate category names
diag_dict = {0: 'infectious', 1: 'neoplasms', 2: 'endocrine', 3: 'blood', 4: 'mental', 5: 'nervous', 6: 'circulatory', 7: 'respiratory', 8: 'digestive', 9: 'genitourinary', 10: 'pregnancy', 11: 'skin', 12: 'muscular', 13: 'congenital', 14: 'perinatal', 15: 'symptoms', 16: 'injury', 17: 'other'}

# Re-code in terms of integers
for num, cat_range in enumerate(icd9_ranges):
    df['RECODE'] = np.where(df['RECODE'].between(cat_range[0], cat_range[1]), num, df['RECODE'])

#print(df['ICD9_CODE'])

# Covert integer to category using diag_dict
df['CATEGORY'] = df['RECODE'].map(diag_dict)
df.to_csv('C:/Users/DELL/Desktop/Recode_icd9.csv', index = False)

