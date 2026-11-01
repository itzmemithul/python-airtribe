arr = [8,5,3,5,6,2,8,6,5,3,6,8,9]
queries = [10,3,5,6,7,9,12]

frequencyMap = dict()
for key in arr:
    frequencyMap[key] = frequencyMap.get(key, 0) + 1 # get the key and default it to 0 in the beginning and then add 1
print(frequencyMap)
for query in queries:
    if query in frequencyMap:
        print(frequencyMap[query])
    else:
        print("-1")