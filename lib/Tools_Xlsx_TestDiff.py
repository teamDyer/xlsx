"""
"""



def dictionaryDiff(dict1,dict2,dict1name,dict2name,path=''):
    """
    Check if two dictionaries are equivalent.  

    This code only has a few changes from the original for our own purposes:
        https://stackoverflow.com/questions/27265939/comparing-python-dictionaries-and-nested-dictionaries
            Comment author: MohitC
    """ 
    diff = ''
    oldPath = path
    for key in dict1.keys():
        path = oldPath + "[" + key + "]"
        if key not in dict2:
            diff += path + " found in '" + dict1name + "' but not in '" + dict2name + "'\n"
        else:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                diff += dictionaryDiff(dict1[key],dict2[key],dict1name,dict2name, path)
            else:
                if dict1[key] != dict2[key]:
                    diff += path + " has a different value in '" + dict1name + "' (" + dict1[key] + ") than in " + dict2name + "' (" + dict2[key] + ")\n" 

    for key in dict2.keys():
        path = oldPath + "[" + key + "]"
        if key not in dict1:
            diff += path + " found in '" + dict2name + "' but not in '" + dict1name + "'\n"

    return diff

