"""
ParseConfig = {
key : {
value : token position
}
}
"""

import os
from collections import OrderedDict

CublasConfig = OrderedDict( {
        "@@@ isamax test" : {"isamax Test Result": 3},
        "@@@@ total errors" : {"Total Errors" : 3},
        "^^^^ CUDA" : {"CUDA - Elapsed Time (s)" : 5, "CUDA - Bandwidth (GB/s)" : 10},
        "^^^^REF" : {"REF - Elapsed Time (s)" : 4, "REF - Bandwidth (GB/s)" : 8, "REF - Speedup" : 10}
    }
)

repository = 'examples/cublas'

def example():
    """
    """
    run = OrderedDict()
    testLogs = os.listdir(repository)
    for testLog in sorted(testLogs):
        file = repository + '/' + testLog
        content = read(file)
        results = grep(content)
        run[os.path.basename(testLog)] = results

def read(path):
    """
    """
    with open(path,'r') as file:
        content = file.readlines()
    content =  [line.strip() for line in content]
    return content

def grep(content):
    """
    """ 
    results = OrderedDict()
    results['ccv'] = {'Command': content[0], 'Exit Code': content[-1]}
    ##parse for each grep in their order
    for grep in CublasConfig.keys():
        for line in content:
            ##search for the grep in each line of the test log
            if grep in line:
                ##if found split the line up into tokens and grab the needed tokens
                tokens = line.split(' ')
                for statistic in CublasConfig[grep].keys():
                    ##store each 
                    token = CublasConfig[grep][statistic]
                    results[statistic] = tokens[token]
    return results
