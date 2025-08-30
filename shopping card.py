#shopping cart program
Foods=[]
prices=[]
total=0


while True:
    food=input("Enter food name(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price=float(input(f"Enter price of {food}:Rs "))
        Foods.append(food)
        prices.append(price)

for food in Foods:
    print(food,end=" ")
for price in prices:
    total += price
print()
print(f'total is {total}')
