


str=input("Enter a string :")
print("string is ",str)
count={}
for x in str:
    if x in count.keys():
       count[x]+=1
    else:
        count[x]=1
        # print(x,"=",count[x])
print(count)



# for x in  Counter.keys():
#  for x in  reversed(count.keys()):
#       print(x,"=",count[x])

# text = input("Enter the string : ")
# count = { }
# for ch in text:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1
# print(count)


def function_freq(string):
    d={}
    for i in string:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

str=input("Enter the String :")
print(function_freq(str))