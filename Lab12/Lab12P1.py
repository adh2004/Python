
def dictFunctionAdd(dict):
    dict['CSC161'] = 17
    return dict

def searchDict(dict , matchClass):
    if matchClass in dict:
        output = 'Number of students enrolled: ' + str(dict[matchClass])
        del dict[matchClass]
        return output, dict
    else:
        output =  'Class not found'
        return output, dict

def printDictionary(dict):

    dictToTuple = dict.items()
    print(dictToTuple)

def updateDictionary(dict, updateClass):
    updatedVal = int(input('Enter new value for '+ str(updateClass) + ': '))
    dict[updateClass] = updatedVal
    return dict

def main():
    dict_classes = {'CSC121':55,'CSC131':42,'CSC141':20,'CSC151':25}
    cls = input('Enter a course: ')
    output = ''
    dict_add = dictFunctionAdd(dict_classes)

    output, dict_new = searchDict(dict_add, cls)
    print(output)
    print('Number of courses in Dictionary: ', len(dict_classes))
    printDictionary(dict_new)

    cls = input('Enter a course: ')
    dict_change = updateDictionary(dict_new, cls)

    cls = input('Enter a course: ')
    output, dict_change = searchDict(dict_change, cls)
    print(output)
    print('Number of courses in Dictionary: ', len(dict_change))
    printDictionary(dict_change)

main()
