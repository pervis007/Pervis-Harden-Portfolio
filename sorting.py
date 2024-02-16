numbers = [5,1,78,23,64,7,43,2,744,121,533,866,8934,1222,53,8,4,3,9,15,67,44,1800] #Tuples/Sequences cannot be changed. .sort only works on list
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.sort(reverse=True)

#sorted is how you sort a text value
text = "This is aa fun litte sentence to sort"
# result = sorted(text.split())
# print(result)
# result = sorted(text.split(), reverse=True)
# print(result)
result = sorted(text.split(), key=lambda x: x[1])
print(result)
