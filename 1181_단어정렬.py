num = int(input())
dict_arr = []

for i in range(num):
    s = input()
    dict_arr.append(s)

dict_set = set(dict_arr)
dict_arr = list(dict_set)
arr = sorted(dict_arr)
arr.sort(key = len)

for i in range(len(arr)):
    print(arr[i])
