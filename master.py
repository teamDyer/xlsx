"""
"""

import ccvPerf_Parser
parsed = ccvPerf_Parser.example()

import Tools_Xlsx_Writer 
Tools_Xlsx_Writer.sample(parsed)

import Tools_Xlsx_Reader
read = Tools_Xlsx_Reader.example()

print('diffing')
print('-------')

value = { k : read[k] for k in set(read) - set(parsed) }
print(value)

print('-------')
print('done')