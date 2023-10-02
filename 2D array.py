TWODLIST = ['AKJFDLSF','AIODFJOAIJFD','AODIJFOAJ','AKDJFOAIDJF']
while True:
    action = input("""\n
Would you like to:
    1 - Add note
    2 - Delete note
    3 - See all notes  
    4 - See specfic note
    5 - Exit

            Enter choice: """)
            
    if action == '5':
        exit()

    elif action == '1':
        note = input("Enter note: \n")
        TWODLIST.append(note)

    elif action == '2':
        print("Input list index (1-",length,")")
        index = int(input("Index: "))
        if index > len(TWODLIST) or index < 0:
            print("Invalid index \n")
        if type(index) == 'int':
            TWODLIST.pop(index)
        else:
            print(print("Invalid index \n"))

    elif action == '3':
        for i in range(len(TWODLIST)):
            print("Note ",i+1,": ", TWODLIST[i])

    elif action == '4':
        length = len(TWODLIST)
        print("Input list index ( 1 -",length,")")
        index = input("Index: ")

        if index.isnumeric():
            index = int(index)
            index -= 1
            if index > len(TWODLIST) or index < 0:
                print("Invalid index: Not within range")
            else:
                print("Note ",index,":", TWODLIST[index],'\n')
        else:
            print(print("Invalid index: Not a number"))

    else:
        print("Invalid number: please make choice in range of 1-5")
