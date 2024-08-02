user_name = input("Enter a User Name : ")
while True:
        if len(user_name) > 8:
            print("User Name is too long.")
            continue;
        elif not user_name.find(" ")==-1:
            print("User Name cannot contain spaces.")
            continue;
        elif not user_name.isalpha():
            print("User Name Must Bre in Alpha nOt in the digits")
            continue;
        else:
            print(f'Welcome --{user_name}--All The user Conditions has been passed'.format(user_name))
            break;