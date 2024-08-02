weight=float(input("Enter U r Weight : "))
unit=input("Enter Unit : (L=lbs or K=Kgs) : ").lower()

if unit=="l":
    weight=weight/2.205
    unit='Kgs.'
    print(f'Your Weight is {weight} in {unit}')
elif unit=="k":
        weight=weight*2.205
        unit='Lbs.'
        print(f'Your Weight is {weight} in {unit}')
else:
    print(f'{weight} is invalid')
    print('Please Enter Something New')
