# for i in range(1, 11):
#     print(i)
#     
#     
# for j in [1,2,3]:
#     print(j)
#     
# nums = []
# for k in range(0, 20, 2):
#     nums.append(k)
# 
# print(nums)
# 
# for p in range(0, 5):
#     print("*" * 4)
    
def asterisk(num):
    pos = [x for x in range(num) ]
    for i in range(0, num):
        print("*" * pos[i])
    pos.reverse()
    for j in range(1, num):
        print("*" * pos[j]) 
asterisk(20)

# #

# 
def has_a(text):
    words = list(text)
    
    for letter in words:
        if letter == "a":
            return True
    return False

print(has_a("Joshua"))

def has_letter(text, letter):
    words = list(text)
    
    for w in words:
        if w == letter:
            return True
    return False

# print(has_letter("Joshua","a"))


def has_s_m(text):
    return has_letter(text, "s") and has_letter(text,"m")


print(has_s_m("Johms"))


print("a" in "ama)