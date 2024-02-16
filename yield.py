import sys

# def myFunc():
#     i = 1
#     print("First")
#     print(i)
#     i+=1

#     print("Second")
#     print(i)
#     i+=1

#     print("Third")
#     i+=1

#     return i

# myFunc()
# x = myFunc()
# print(x)


def myGenFunc():
    i = 1
    print("First")

    yield i

    print("Second")
    i += 1

    yield i

    print("Third")
    i+= 1

    yield i

result = myGenFunc()
for result in myGenFunc():
    print(result)


def csvReader(fileName):
    for line in open(fileName):
        yield line

# csv = csvReader("sample.txt")
# for result in csv:
#     print(result)





listOne = [i * 2 for i in range(1000000)]
print(sys.getsizeof(listOne))

listTwo = (i *2 for i in range(1000000))
print(sys.getsizeof(listTwo))


for i in listOne:
    print(i)
