import pandas as pd
import json
from TestRunner.get_filename import *

'''0. Get the output folder path which created by cTAKES'''

outfilePath = 'C:/Users/DELL/Desktop/Result'
outfile_name, _, file_list = get_filename(outfilePath)

for i in range(len(outfile_name)):

    df = pd.read_csv('C:/Users/DELL/Desktop/Result/%s.csv' % outfile_name[i])
    # choose columns to keep, in the desired nested json hierarchical order
    df = df[["Semantic Types", "CUI"]]
    df['CUI'] = df['CUI'] .map(lambda x : outfile_name[i]+ '.' + x)
    
    df_sort = df.groupby(['Semantic Types', 'CUI']).sum()
    df_sort = df_sort.reset_index()
    
    # start a new flare.json document
    flare = []
    children = df_sort['CUI'].values.tolist()
    
    for line in df_sort.values:
        the_parent = line[0]
        the_child = line[1]

        # make a list of keys
        keys_list = []
        for item in flare:
            keys_list.append(item['name'])

        # if 'the_parent' is NOT a key in the flare.json yet, append it
        if not the_parent in keys_list:
            flare.append({"name": the_parent, "imports":[the_child]})

        # if 'the_parent' IS a key in the flare.json, add a new child to it
        else:
            flare[keys_list.index(the_parent)]['imports'].extend([the_child])
    
        #print(children)
        for index in range(len(children)):
            # if 'the_child' is NOT a key in the flare.json yet, append it
            if not children[index] in keys_list:
                flare.append({"name": children[index], "imports":children[index + 1:]})
            else:
                index += 1
                
    # export the final result to a json file
    with open('C:/Users/DELL/Desktop/Outfile/%s.json' % outfile_name[i], 'w') as outfile:
        json.dump(flare, outfile)    