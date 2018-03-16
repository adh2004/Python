def setUnion(setA, setB, matchClause):
    if matchClause == 'union':
        output = 'Combined set of courses: ' + str(setA | setB)
        return output
    elif matchClause == 'intersect':
        output = 'Courses common in both programs: ' + str(setA & setB)
        return output
    elif matchClause == 'javaCert':
        output = 'Courses in Java certificate only: ' + str(setA - setB)
        return output
    elif matchClause == 'csharpCert':
        output = 'Courses in C# certificate only: ' + str(setB - setA)
        return output

def main():
    java_list = ['CSC120', 'CSC121', 'CSC151', 'CSC251']
    csharp_list = ['CSC120', 'CSC121', 'CSC153', 'CSC253']
    javaCert = set(java_list)
    csharpCert = set(csharp_list)
    output = setUnion(javaCert, csharpCert, 'union')
    print(output)
    output = setUnion(javaCert, csharpCert, 'intersect')
    print(output)
    output = setUnion(javaCert, csharpCert, 'javaCert')
    print(output)
    output = setUnion(javaCert, csharpCert, 'csharpCert')
    print(output)

main()
