Menu = {"pizza": 3.00,
               "nachos": 4.50,
               "popcorn": 6.00,
               "fries": 2.50,
               "chips": 1.00,
               "pretzel": 3.50,
               "soda": 3.00,
               "lemonade": 4.25}
cart = []
total = 0
print("---Menu---")
for key,value in Menu.items():
    print(f'{key:10} : ${value:.1f}')
print("------------")
#Here we are entering in while loop this will iterae
while True:
    food=input("Select A Food U want q to quit : ").lower()

    if food =="q":
        print("Thank U For Shopping")
        break
        #here menu.get(food) is not none:oka vela none kakapothy cart lo add chy
    elif Menu.get(food) is not None:
        cart.append(food)

print("----------Your Order--------------")
for food in cart:
    total = total + Menu.get(food)
    print(food,end=" ")
print(f'This is u r ${total:.02f}')



