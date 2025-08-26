#list
fruites=["apple",'orange','banana','grape']
answer="apple" in fruites
print(answer)
if answer==True:
    fruites.append("orange")
    fruites[0]="banana"
else:
    fruites.append("banana")
    fruites[3]="orange"
print(fruites)
for x in fruites:
    print(x)

fruites.clear()
print(fruites)

fruites.append("orange")
print(fruites)

fruites.insert(1,"banana")
print(fruites)
fruites.pop()
print(fruites)
sweets=["orange","banana","grape"]
fruites.extend(sweets)
print(fruites)
print(fruites.index('grape'))



