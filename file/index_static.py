while True:
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("1 => add user")
    print("2 => read user")
    print("3 => Read file")
    print("4 => Delete user")
    Choise = input("Choise opration in List ?")

    #   static file     50 char

    # add user
    if (Choise == '1'):
        print("Enter your ID :")
        ID = input()
        print("Enter your Name :")
        Name = input()
        print("Enter your Family :")
        Family = input()

        # open whit
        f = open("index_data.txt", "a")
        pointer = f.tell()
        # code to pad spaces in string
        name_file = "*" + "0" + "_" + "ID=" + ID + "_" + "Name=" + Name + "_" + "Family=" + Family + "|"
        f.write(name_file)


        f.close()

    # len data 20 char
        f1 = open("index.txt", "a")
        address = str(pointer)
        #address = address.ljust(16)
        f1.write(address.ljust(16) + ID.ljust(4))
        #f1.write(ID.ljust(4))
        f.close()






    # read user
    elif (Choise == '2'):
        pointer = 0
        index = open("index.txt", "r+")

        id = input("Enter block  ==> ")
        id = id.ljust(4)
        buffer = ''

        positon = int(id) * 20
        index.seek(positon - 20)
        buffer = index.read(20)
        address_pointer = int(buffer[0:15])




        f = open("index_data.txt", "r")
        f.seek((address_pointer-50))
        buffer = f.read(50)
        print(buffer)
        break



    # Read file
    elif (Choise == '3'):
        pointer = 0
        index = open("index.txt", "r+")

        indexenn = len(index.read())
        indexenn = int(indexenn / 20)

        for i in range(1, indexenn):
            positon = i * 20
            index.seek(positon - 20)

            buffer = index.read(20)
            address_pointer = int(buffer[0:15])

            f = open("index_data.txt", "r")
            f.seek((address_pointer-50))
            bufferf = f.read(50)
            print(bufferf)



    # Delete file
    elif (Choise == '4'):
        pointer = 0
        index = open("index.txt", "r+")

        id = input("Enter block  ==> ")
        id = id.ljust(4)
        buffer = ''

        positon = int(id) * 20
        index.seek(positon - 20)
        buffer = index.read(20)
        address_pointer = int(buffer[0:15])


        f = open("index_data.txt", "r+")
        f.seek((address_pointer-50))
        f.write("1")
        f.close()
        print("delete OK")
        break



    else:
        print("ronge choise try again?")
        print()
        print()
