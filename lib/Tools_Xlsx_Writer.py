"""
"""

import xlsxwriter
from collections import OrderedDict

data = OrderedDict()

data['run_01'] = {
	'test_0001': {
		'_name': './blah',
		'GFLOPS': '894',
		'Memory Time (ms)': '53'
	},
	'test_0002': {
		'_name': './none',
		'GFLOPS': '2145',
		'Memory Time (ms)': '6541'
	}
}

data['run_02'] = {
	'test_0001': {
		'_name': './blah',
		'GFLOPS': '897',
		'Memory Time (ms)': '49'
	},
	'test_0002': {
		'_name': './none',
		'GFLOPS': '2168',
		'Memory Time (ms)': '6684'
	}
}

def example():
	"""
	Data comes in as a nested dictionary with the format:
		{
			run_01:	
				{
					test_0001:
					{
						_name: 'name'
						result1name: 'value'
						result2name: 'value'
						...
					}
					test_0002:
					{
						_name: 'name'
						result1name: 'value'
						result2name: 'value'
						...
					}
					...
				}
			run_02:	
				{
					test_0001:
					{
						_name: 'name'
						result1name: 'value'
						result2name: 'value'
						...
					}
					test_0002:
					{
						_name: 'name'
						result1name: 'value'
						result2name: 'value'
						...
					}
					...
				}

		}
	"""
	workbook = xlsxwriter.Workbook('sample.xlsx')

	##pick the first set of attributes generate the headers
	for run in data.keys():
		for test in data[run].keys():
			headers = data[run][test]
			break
		break

	##store the header so it can be used multiple times
	header = []
	for entry in headers.keys():
		header.append(entry)

	for run in data.keys():
		##initialize the worksheet
		worksheet = workbook.add_worksheet(name=run)
		row = 0
		column = 0
		writeRow(header,worksheet,row,column) 
		row += 1
		for test in data[run].keys():
			##grab each attribute recorded from this test
			entries = []
			for attribute in data[run][test].keys():
				entries.append(data[run][test][attribute])
			##write each of the test's attributes and move on the next row
			writeRow(entries,worksheet,row,column)
			row +=1
			
	workbook.close()


def writeRow(entries,worksheet,row,column):
	"""
	Write a row of **entries** into the **worksheet** beginning at (**row**, **column**). 
	"""
	for entry in entries:
		worksheet.write(row,column,entry)
		column +=1
