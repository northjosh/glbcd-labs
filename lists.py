list = []
list.append('a')
print (list)


def list_even(min, max):
    even = []
    
    for num in range(min, max):
        if num % 2 == 0:
            even.append(num)
    return even

print(list_even(1, 10))