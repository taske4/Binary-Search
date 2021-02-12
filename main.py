def binSearch(collection, searchNum):
    if searchNum < collection[0] or searchNum > collection[-1]: return False
    left, right = 0, len(collection) - 1
    while(left <= right):
        index = (left + right) // 2
        if searchNum == collection[index]:
            return index
        elif searchNum < collection[index]:
            right = index - 1
        else:
            left = index + 1

    return False

def main():
    collection = list(range(3,34))

    print(collection)
    for searchNum in range(0,50):
        searchResult = binSearch(collection=collection, searchNum=searchNum)
        print(searchNum, searchResult)

main()