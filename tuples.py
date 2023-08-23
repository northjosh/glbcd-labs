
def partition(num):
    return (num, None) if num % 2 == 0 else (None, num)

print(partition(11))


def partition_list(nums):
    pairs = []
    
    for num in nums:
        pairs.append(partition(num))
    
    return pairs

print(partition_list([1,2,3,4,5,6,7,8,9,1]))