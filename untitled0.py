def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    revDict = dict()
    for key in aDict:
        if revDict.get(aDict[key], -555) == -555 and revDict.get(aDict[key], -555) != -556:
            revDict[aDict[key]] = key
        else:
            revDict[aDict[key]] = -556
            
    res = list()
    for key in revDict:
        if revDict[key] != -556:
            res.append(revDict[key])
    return sorted(res)