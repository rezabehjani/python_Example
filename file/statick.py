while True:
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("1 => add user")
    print("2 => read user")
    print("3 => Read file")
    print("4 => Delete user")
    Choise = input("Choise opration in List ?")



#   static file     50 char


    # add user
    if (Choise== '1'):
        print("Enter your ID :")
        ID = input()
        print("Enter your Name :")
        Name = input()
        print("Enter your Family :")
        Family = input()

        # open whit ascii b
        f = open("statick.txt", "a")


        f.write("0_" + ID.ljust(4) + Name.ljust(22) + Family.ljust(22))

        # # code to pad spaces in string
        # ID = ID.ljust(4)
        # f.write("0_" + ID)
        # Name = Name.ljust(22)
        # f.write(Name)
        # Family = Family.ljust(22)
        # f.write(Family)



        f.close()


        #open and read the file after the appending:
        #f = open("statick.txt", "r")
        #print("read file ==>> ", f.read())


    # read user
    elif (Choise== '2'):
        pointer = 0
        f = open("statick.txt", "r+")
        flen = open("statick.txt", "r")
        lenn = len(flen.read())

        id = input("Enter ID user ==> ")
        id = id.ljust(4)
        buffer = ''

        i = 0
        while (i <= int(lenn/50)):
            i += 1
            buffer = f.read(50)

            if (buffer[2:6] == str(id)):
                print(buffer)
                break



    # Read file
    elif (Choise== '3'):

        pointer = 0
        f = open("statick.txt", "r+")
        flen = open("statick.txt", "r")
        lenn = len(flen.read())
        buffer = ''
        i = 0
        while (i <= int(lenn/50)):
            i += 1
            buffer = f.read(50)
            print(buffer)

    # Delete file
    elif (Choise== '4'):
        pointer = 0
        f = open("statick.txt", "r+")
        id = input("Enter ID user for Delete==> ")
        id = id.ljust(4)
        buffer = ''

        i = 0
        while (i <= 20):
            i += 1
            buffer = f.read(50)
            if (buffer[2:6] == str(id)):

                pointer = (f.tell() - 50)
                f.seek(pointer)
                print(f.tell())
                f.write('1')
                print(f.read())
                break





    else:
        print("ronge choise try again?")
