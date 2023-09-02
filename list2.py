# num = int(input("How many Item in List"))
# print("List Item Contain:",num)

# newlist=[] 
# for i in range(num):
#     i = int(input())
#     newlist.append(i)

# print("your list is:",newlist)
# evenlist=[]
# oddlist=[]
# for i in newlist:
#     if i%2==0:
#         evenlist.append(i)
#     else:
#         oddlist.append(i)
# print("even list is :",evenlist)
# print("odd list is:",oddlist)

# print("Largest Number from newlist list using Max:",max(newlist))
# print("Largest Number from evenlist list using Max:",max(evenlist))
# print("Largest Number from oddlist list using Max:",max(oddlist))

# max = newlist[0]

# for n in newlist:
#     if n > max:
#         max = n
# print("maximum number from newlist is:",max)



item=int(input("How Many Item in list"))
print("list item contain:",item)

item2=int(input("How Many Item in list"))
print("list item contain:",item)

newlist=[]
for i in range(item):
    i = int(input())
    newlist.append(i)

for i in range(item):
    i = int(input())
    newlist.append(i)

print("your list is:",newlist)
print(newlist[0:-2])

evenlist=[]
oddlist=[]

for i in  newlist:
    if i%2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)

print("even list is:",evenlist)
print("odd list is:",oddlist)

min_value=newlist[0]
for i in newlist:
    if i < min_value:
        min_value = i
print(min_value)

min_value = evenlist[0]
for i in evenlist:
    if i < min_value:
        min_value=i
print(min_value)

min_value = oddlist[0]
for i in oddlist:
    if i < min_value:
        min_value = i
print(min_value)

max_value = newlist[0]
for i in newlist:
    if i > newlist:
        newlist = i
print(max_value)

max_value = evenlist[0]
for i in evenlist:
    if i > evenlist:
        newlist = i
print(max_value)

max_value = oddlist[0]
for i in oddlist:
    if i > oddlist:
        newlist = i
print(max_value)

# print("Minimum number from newlist using Max:",min(newlist))
# print("Minimum number from newlist using Max:",min(evenlist))
# print("Minimum number from newlist using Max:",min(oddlist))