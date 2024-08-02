#Caluclator USe if else

Operator=input("Enter The Operator(+,-,*,/) : ")
N1=int(input("Enter the First Number : "))
N2=int(input("Enter the Second Number : "))

if Operator=="+":
    print(f"The sum of {N1} + {N2} = {N1+N2}")
elif Operator=="-":
    print(f"The Diffrenece of {N1} - {N2} = {N1-N2}")
elif Operator=="*":
    print(f"The Product of {N1} * {N2} = {N1*N2}")
elif Operator=="/":
    print(f"The Divide of {N1} / {N2} = {N1/N2}").round()
else:
    print("Invalid Operator")

print("Thanks For Using Caluclator")
          
           