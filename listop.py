mylist=["apple","orange","banana"]
print(mylist[1])
# orange
print(mylist[-1])
# banana
print(mylist[1:3])
# ['orange', 'banana']
mylist[1]="grape"
print(mylist)
# ['apple', 'grape', 'banana'] 
mylist.insert(2,"kiwi")

print(mylist)
# ['apple', 'grape', 'kiwi', 'banana']
mylist.append("mango")
print(mylist)
# ['apple', 'grape', 'kiwi', 'banana', 'mango']
list2=["staberry","melon"]
mylist.extend(list2)
print(mylist)
# ['apple', 'grape', 'kiwi', 'banana', 'mango', 'staberry', 'melon']
mylist.remove("banana")
print(mylist)
# ['apple', 'grape', 'kiwi', 'mango', 'staberry', 'melon']
mylist.pop(2)
print(mylist)
# ['apple', 'grape', 'mango', 'staberry', 'melon']
mylist.pop()
print(mylist)
# ['apple', 'grape', 'mango', 'staberry']
# del -it is used to delete the list or a specific element from the list
# clear() -it is used to delete all element from the list[]
list3=[i for i in mylist]
print(list3)
# ['apple', 'grape', 'mango', 'staberry']
list4=[i for i in  mylist if "g" in i]
print(list4)
# ['grape', 'mango']
mylist.sort(reverse=True)
print(mylist)
# ['staberry', 'mango', 'grape', 'apple']
li=mylist.count("apple")
print(li)
# 1git init