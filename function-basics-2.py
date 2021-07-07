

def countdown(number):
    output =[]
    for x in range(number,0,-1):
        output.append(x)
    return output

print(countdown(10))

def print_and_return(list):
    print(list[0])
    return list[1]

print_and_return(5,88)


def first_plus_length(list):
    return list[0] + len(list)


print(first_plus_length([1,6,8,54,9]))


def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for x in range(0,len(list)):
        if list[x] > list[1]:
            output.append(list[x])
    print(len(output))
    return output

print(values_greater_than_second([4,7,2,6,8,4,2]))
print(values_greater_than_second([3]))


def length_and_value(size,value):
    output = []
    for i in range(0,size):
        output.append(value)
    return output

print(length_and_value(5,9))
