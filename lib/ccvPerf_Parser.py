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
        "@@@@" : {"Test Name": 1, "Result": 3},
        "^^^^ CUDA" : {"CUDA - Elapsed Time (s)" : 5, "CUDA - Bandwidth (GB/s)" : 10}
        #"^^^^REF" : {"REF - Elapsed Time (s)" : 4, "REF - Bandwidth (GB/s)" : 8, "REF - Speedup" : 10}
    }
)

repository = 'examples/cublas'

def example():
    """
    """
    data = OrderedDict()
    for iteration in os.listdir(repository):
        run = OrderedDict()
        testLogs = os.listdir(repository + "/" + iteration)
        for testLog in sorted(testLogs):
            file = repository + '/' + iteration + '/' + testLog
            results = grep(file)
            run[os.path.basename(testLog)] = results
        data[iteration] = run
    return data

def read(path):
    """
    """
    with open(path,'r') as file:
        content = file.readlines()
    content =  [line.strip() for line in content]
    return content

def grep(file):
    """
    """ 
    results = OrderedDict()
    content = read(file)
    ##add any extra stuff here that will be with test log
    results['Test'] = os.path.splitext(os.path.basename(file))[0]
    results['Command Line'] = content[0]
    results['Exit Code'] = content[-1]
    ##parse for each grep request in their order
    for grep in CublasConfig.keys():
        for line in content:
            ##search for the grep request in each line of the test log
            if grep in line:
                ##if grep request found, split the line up into tokens 
                tokens = line.split(' ')
                for statistic in CublasConfig[grep].keys():
                    ##store each statistic based on its token position
                    token = CublasConfig[grep][statistic]
                    results[statistic] = tokens[token]
    return results
