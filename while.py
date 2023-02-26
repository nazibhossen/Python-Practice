text = input()
dic = {}
for char in text:
    if char in dic:
        dic[char] +=1
    else:
        dic[char] = 1
print(dic)

x = 2**3
print(x)