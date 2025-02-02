import os
import csv

os.makedirs("dataset")

fields=["Id","Name"]
filename="Id_Name_ref_sheet.csv"

with open(filename,"w") as csvfile:
    filewriter=csv.writer(csvfile)
