def shipping_Address(*args, **kwargs):
    for arg in args:
        print(arg)
    print()
    if "name" in kwargs:
        print(f"Hi Hello! {kwargs.get('name')}")
    elif "Name" in kwargs:
        print(f"Hello Hi {kwargs.get('name')}")
    else:
        print(f"Hello Hi This is else")

    print(f"The shipping adress is the "
          f"Street = {kwargs.get('street')}"
          f"Village is {kwargs.get('village')}"
          f"Zip is {kwargs.get('zip')}")
shipping_Address("Sri ram naidu ","This is an Arguments",
                    street="Nazer pet",
                    village='Tenali',
                    zip='522201')