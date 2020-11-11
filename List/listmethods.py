# from random import randint
# n = int(input("n="))
# randomArray = [randint(0,100) for _ in range(n)]
# print(randomArray)

arr = [51, 86, 47, 11, 52, 1, 58, 27, 29, 51]
print(arr)
# searchValue=51
# print(f"{searchValue} водить в список {arr.count(searchValue)} раз")
# # k = 0
# # for el in arr:
# #     if el == searchValue:
# #         k +=1
# # print(k)
# arr.append(42)
# print(arr)

# otherArr = arr.copy()
# arr [0] = 0
# print(arr)
# print(otherArr)

# arr.extend(arr)
# print(arr)
# searchValue=51
# print(arr.index(searchValue))
# index = -1
# for i in range(len(arr)):
#     if arr[i] == searchValue:
#         index = i
#         break
# print(index)
#
# print(arr.index(searchValue, 3))
# arr.insert(5, 100)
# print(arr)
#
# arr.remove(27)
# print(arr)

# arr.reverse()
# print(arr)

arr.sort()
arr.reverse()
print(arr)

print(sum(arr))
