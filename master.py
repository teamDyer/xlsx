from Tools_Xlsx_Writer import generate
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

generate(data)
