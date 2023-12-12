import pandas as pd
import glob

# take all files inside invoices with the extension .xlsx
# glob.glob will return an array of file names
filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)