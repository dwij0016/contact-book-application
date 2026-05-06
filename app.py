def book():
    contact = {}
    print('----your contact book----')
    while True:
        print('available options')
        print('1.add\n2.update\n3.delete\n4.viewn\n5.exit\nenter the opration = ')
        def a():
            key = input('name the contact = ')
            value = int(input('add the no. of the contact = '))
            contact[key] = value
            print(contact)

        def u():
            d = input('enter the key name want to update =')
            f = int(input('enter the no. you want to update = '))
            contact.index(key) = d
            contact.index(value) = f
            print(f'the name is successfully updated as {d} and the no. as {f}')
            print(contact)

        
