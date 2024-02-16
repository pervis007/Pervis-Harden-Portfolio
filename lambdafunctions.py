import dis as d

doubleIt = lambda x: x*2

print(doubleIt(5))


def doubleItFunc(x):
    return x*2

# print(doubleItFunc)
# print(d.dis(doubleItFunc))
# print(doubleIt)
# print(d.dis(doubleIt))

my_list = [1,5,4,6,8,11,3,12]

newList = filter(lambda x: (x%2 == 0), my_list)
newList = list(newList)
print(newL
ist)

