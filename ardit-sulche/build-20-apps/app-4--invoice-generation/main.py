import pandas as pd
import glob

# take all files inside invoices with the extension .xlsx
# glob.glob will return an array of file names
filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    # loop 3 excels and create data frames for each
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
