#Functions in python
#def keyword is used to create the fn
#def fn_name(Parameters):
#arguments are used to send the data in parameters
#there are mainly 4 types of arguments
#1.Positional 2.Default 3.keyword 4.Arbitary

#Positional Arguments are used to pass the in order only
'''def User_invoice(username,amount,Due_date):
    print(f'The User Name is {username}')
    print(f'The amount :{amount:.2f} and Due_Date is {Due_date:<10}')
User_invoice("Sri ram",10000,"27/07/2004")'''
'''
def Name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first + " " +last
Full_Name=first +' '+ last
    print(Full_Name)
Full_name=Name("Sri Ram","Naidu")
        print(Full_name)
'''

#Default-The default arguments are used to set the Default Values
#And again if pass the parameter then this will update the new argument

'''def price(list_price,discount=0,tax=0.5):
    return list_price*(1-discount)*(1+tax)
Here Return is used to send the output to the print statement
Print-fn display the output return and print doesnt work at a time
print(price(500,0,0))
here the tax and display values are updated through the arguments pases
print(price(450))'''

'''import time
def count(end,start=20):
    #The Default arguments should nt be at first
    for x in range(start,end+1):
        #here We USe +1 for index
        print(x)
        time.sleep(1)
    print("Done!")

print(count(40,35))
'''

#Keyword arguments
def greet(greet,title,first,last,sending_off):
    return f"{greet} {title} {first} {last}"
#The return with formatted string also can do
    #print(f"{greet} {title} {first} {last}")
    #if this line tehre no need to print again there

Greet=greet("Hi",first="Sri Ram",title="Name of The candidate",last="Polakam",sending_off="Bye Bro")
#All The Parameter to be filled here this is the main this
print(Greet)
