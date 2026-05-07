def book():
    contact = {}
    s = list(contact)
    # print(s)
    print('----your contact book----')
    while True:
        print('available options')
        print('1.add\n2.update\n3.delete\n4.viewn\n5.exit')
        operation = (int(input('enter the operationt = ')))
        def a():
            key = input('name the contact = ')
            value = int(input('add the no. of the contact = '))
            s.append(key)
            s.append(value)
            print(s)
            

        def u():
            d = input('enter the key name want to update =')
            f = int(input('enter the no. you want to update = '))
            b = input('enter the new name you want to update = ')
            c = int(input('enter the new no. you want to update = '))
            ind = s.index(d)
            inx = s.index(f)
            s[ind] = b
            s[inx] = c
            print(f'the name is successfully updated as {b} and the no. as {c}')
            print(s)

        def de():
            de_val_name = input('enter the name you want to delete =')
            de_val_no = int(input('enter the no. you want to delete = '))
            ix = s.index(de_val_name)
            del s[ix]
            io = s.index(de_val_no)
            del s[io]
            print(s)

        def veiw():
            print(s)

        if operation == 1:
            a()
        elif operation == 2:
            u()
        elif operation == 3:
            de()
        elif operation == 4:
            veiw()
        else:
            print('invalid code')
book()