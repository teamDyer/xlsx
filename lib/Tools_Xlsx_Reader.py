"""
"""

from pprint import pprint
import openpyxl

sample = "sample.xlsx"

def example():
    """
    """
    ##nested dictionary all of the data comes into
    data = {}
    ##load the file 
    workbook = openpyxl.load_workbook(filename=sample, read_only=True)
    ##grab all of the runs
    runs = workbook._sheets
    ##assume the structure based on the first run's header
    structure = []
    run = runs[0]
    for column in range(1,run._max_column):
        cell = run.cell(row=1,column=column)
        structure.append(cell.value)
    ##add all of the data from each run into the nested dictionary
    for run in runs:
        sheet = {}
        ##add each test individually
        for row in range(2,run._max_row):
            ##the test number is stored in the first column of each row
            testnumber = run.cell(row=row,column=1).value
            test = {}
            for column in range(2,run._max_column):
                test[column-1] = run.cell(row=row,column=column).value
            sheet[testnumber] = test
        data[run.title] = sheet
    return data
