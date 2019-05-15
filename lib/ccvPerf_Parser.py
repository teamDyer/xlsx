"""
ParseConfig = {
key : {
value : token position
}
}
"""

import os
from collections import OrderedDict

CublasConfig = OrderedDict()
CublasConfig["@@@@"] = {"Test Name": 1, "Result": 3}
CublasConfig["^^^^ CUDA"] = {"CUDA - Elapsed Time (s)" : 5, "CUDA - Bandwidth (GB/s)" : 10}
##CublasConfig["^^^^REF"] = {"REF - Elapsed Time (s)" : 4, "REF - Bandwidth (GB/s)" : 8, "REF - Speedup" : 10}

CudnnConfig = OrderedDict()
CudnnConfig["@@@@ Overall result"] = {"Result": 8}
CudnnConfig["^^^^ CUDA elapsed median"] = {"CUDA - 100 run median (ms)": 5}
CudnnConfig["^^^^ CUDA elapsed for"] = {"CUDA - 100 run min (ms)": 7, "CUDA - 100 run max (ms)": 10}
CudnnConfig["SOL  :"] = {"SOL - Theoretical Gflops": 5, "SOL - Measured Gflops": 8, "SOL - Percentage": 10}
CudnnConfig["SOL(Memory)"] = {"SOL(MEMORY) - Theoretical (GiB/s)": 4, "SOL(MEMORY) - Measured (GiB/s)": 9, "SOL(MEMORY) - Percentage": 11}
CudnnConfig["^^^^ CUDA :"] = {"Total Elapsed Time (s)": 4, "Total Gflops": 8}

repository = 'examples/cublas'

def example():
    """
    """
    data = OrderedDict()
    for iteration in sorted(os.listdir(repository)):
        run = OrderedDict()
        testLogs = os.listdir(repository + "/" + iteration)
        for testLog in sorted(testLogs):
            file = repository + '/' + iteration + '/' + testLog
            results = grep(file,CublasConfig)
            run[os.path.splitext(os.path.basename(file))[0]] = results
        data[iteration] = run
    return data

def read(path):
    """
    """
    with open(path,'r') as file:
        content = file.readlines()
    content =  [line.strip() for line in content]
    return content

def grep(file,config):
    """
    """ 
    results = OrderedDict()
    content = read(file)
    ##add any extra stuff here that will be with test log
    results['Test'] = os.path.splitext(os.path.basename(file))[0]
    results['Command Line'] = content[0]
    results['Exit Code'] = content[-1]
    ##parse for each grep request in their order
    for grep in config.keys():
        for line in content:
            ##search for the grep request in each line of the test log
            if grep in line:
                ##if grep request found, split the line up into tokens 
                tokens = line.split(' ')
                for statistic in config[grep].keys():
                    ##store each statistic based on its token position
                    token = config[grep][statistic]
                    results[statistic] = tokens[token]
    return results
