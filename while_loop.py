# i = 0;
# 
# while(i < 10):
#     i = i + 1
#     print(i)
#

# i = 6;
# while(i < 19):
#     i = i + 1
#     print(i)


# j = 12
# 
# while( j < 20):
#     if j != 20:
#         j += 2
#         print(j)
    
# def evens(n1, n2):
#     
#     
#     
#     if n1 > n2:
#         maximum = n1
#         minimum = n2
#     else:
#         minimum = n1
#         maximum = n2
#     
#     
#     print(maximum)
#     
#     while(minimum < maximum - 2): 
#         minimum +=2
#         print(minimum)     
#         
        
# evens(2, 20)


# def reverse_evens(n1, n2):
#     while n2-2  > n1:
#         n2 -= 2
#         
#         print(n2)
#         
#         
# reverse_evens(2,20)


def evens(n1, n2):
    while(n1 < n2):
        if n1 % 2 == 0:
            print(n1)
        n1+=1
        

evens(1, 10)

def reverse_evens(n1,n2):
    while(n2 > n1):
        if n2 % 2 == 0:
            print(n2)
        n2-=1
            
reverse_evens(1, 10)