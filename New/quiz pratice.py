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

print("--- Menu ---")
for key,value in Menu.items():
    print(f'{key} : {value}')
while True:
    add=input("Enter The Menu What U Want (Q to Quit) : ").lower()
    if add == "q" or "quit":
        print("Thank u For using")
        break;




