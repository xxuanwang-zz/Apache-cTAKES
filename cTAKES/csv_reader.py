import pandas as pd

def csv_reader(CSVFilePath, InputFilePath, Nrows, Text_Column):
    df = pd.read_csv(CSVFilePath, nrows = Nrows)
    column_name = str(Text_Column)
    for index, row in df[column_name].iteritems():
        text = open(InputFilePath + '/%s.txt' % index, "w+") # Input file folder path in Apache cTAKES environment
        text.write(row)
        text.close()
    return True
