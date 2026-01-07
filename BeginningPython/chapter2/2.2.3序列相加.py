arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(arr1 + arr2)
# out:[1, 2, 3, 4, 5, 6]

str1 = 'hello'
str2 = 'world'
str3 = str1 + str2
print(str3)

#TypeError: can only concatenate str (not "list") to str，两者类型不一致，str1是str，arr1是list，需要变成str1+str(arr1)
str1 + arr1
print(str1+ str(arr1))