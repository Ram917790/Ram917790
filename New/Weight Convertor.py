email=input("enter your email address : ")

index=email.index('@')
user_name=email[0:index]
domain=email[index:-1]
print(f'User Name is {user_name} and Domain is {domain}')
