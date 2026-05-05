def book():
    contact = {}
    while True:
        key = input('name the contact = ')
        value = int(input('add the no. of the contact = '))
        contact[key] = value
        print(contact)
book()