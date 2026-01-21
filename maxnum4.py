# def max(*num):
#     if len(num) ==0:
#         return None
#     max_num = num[0]
#     for n in num:
#         if n > max_num:
#            max_num=n
#         return max_num

# tup = ()
# for i in range(5):
#     a=list(tup)
#     m=int(input("enter num : "))
#     a.append(m)
#     tup = tuple(a)
# result = max(*tup)
# print("max num is : ",result)

def find_max(*num):
    if len(num) == 0:
        return None

    max_num = num[0]
    for n in num:
        if n > max_num:
            max_num = n

    return max_num


tup = ()
for i in range(5):
    a = list(tup)
    m = int(input("enter num : "))
    a.append(m)
    tup = tuple(a)

result = find_max(*tup)
print("Maximum number:", result)



