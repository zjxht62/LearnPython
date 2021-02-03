arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(arr1 + arr2)
# out:[1, 2, 3, 4, 5, 6]

str1 = 'hello'
str2 = 'world'
str3 = str1 + str2
print(str3)

#TypeError: can only concatenate str (not "list") to str
str1 + arr1
