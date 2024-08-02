row=int(input("Enter The No of ROws : "))
column=int(input("Enter The Number of columns : "))
symbol=input("Enter the Symbol : ")

for x in range(row): #outer loop
    for y in range(column): #inner loop
        print(symbol,end='')
        #default print(\n in new line)
    print() #this make to print in new line 

