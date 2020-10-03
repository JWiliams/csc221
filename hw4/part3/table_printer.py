tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    # search for the longest element in each array of 
    for arrays in range(len(table)):
        for elements in table[arrays]:
            if colWidths[arrays] < len(elements):
                colWidths[arrays] = len(elements)

    # forming elements into table
    for elements in range(len(table[0])) :
        for arrays in range(len(table)) :
            print(table[arrays][elements].rjust(colWidths[arrays]), end=" ")
        print()
        elements += 1

printTable(tableData)

