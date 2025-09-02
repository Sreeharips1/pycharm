#2dimensional
fruits = ['apple','banana','orange']
vegetables = ['carrots','potatoes','celery']
meats=['chicken','beef','fish']
groceries=[fruits,vegetables,meats]
#print(groceries[1][1])
for item in groceries:
   #print(item,end=" ")
    for food in item:
        print(food,end=" ")
