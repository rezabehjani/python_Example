from builtins import print



while True:
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("1 => add user")
    print("2 => read user")
    print("3 => Read file")
    print("4 => Delete user")

    Choise = input("Choise opration in List ?")


    #add user
    if (Choise == '1'):
        print("Enter your ID :")
        ID = input()
        print("Enter your Name :")
        Name = input()
        print("Enter your Family :")
        Family = input()
        f = open("dynamick.txt", "a")
        name_file = "*" + "0" + "_" + "ID=" + ID + "_" + "Name=" + Name + "_" + "Family=" + Family + "|"
        f.write(name_file)
        f.close()


        #open and read the file after the appending:
        #f = open("test.txt", "r")
        #print(f.read())
        #print("postion pointer = ", f.tell())



    #read user
    elif (Choise == '2'):

        f = open("dynamick.txt", "r")
        id = input("Enter block  ")
        buffer = ''
        i = 0
        len = 1000
        block = 0

        while (i <= len):
            i += 1
            state = f.read(1)
            buffer = buffer + state

            if (state == '|'):
                block = block + 1
                len = len + 100

                ss = buffer
                index = "ID=" + id
                buffer = ''
                if(int(id) == block ):
                #if(ss.split('_')[1] == index ):

                    len = 0

                    print(ss.split('_')[1])
                    print(ss.split('_')[2])
                    print(ss.split('_')[3])
                    print("ok")
                    break


    #Read file
    elif(Choise == '3'):
        f = open("dynamick.txt", "r")
        buffer = ''
        i = 0
        len = 1000
        while (i < len):
            i += 1
            state = f.read(1)
            buffer = buffer + state

            if (state == '|'):
                len = len + 100

                ss = buffer
                print('---------------------')
                print(ss.split('_')[1])
                print(ss.split('_')[2])
                print(ss.split('_')[3])

                buffer = ''



    #Delete user
    elif (Choise == '4'):
        pointer = 0
        f = open("dynamick.txt", "r+")
        id = input("Enter ID user for Delet ")
        buffer = ''
        i = 0
        len = 1000
        block = 0

        while (i < len):
            i += 1
            state = f.read(1)
            buffer = buffer + state

            if(state == '*'):
                pointer = f.tell()
                print("pointer=")
                print(pointer)
            elif(state == '|'):
                block = block + 1
                len = len + 100

                ss = buffer
                index = "ID=" + id
                buffer = ''
                if(int(id) == block ):
                #if(ss.split('_')[1] == index ):
                    len = 0
                    print(ss)
                    print(ss.split('_')[0])
                    print(pointer)
                    f.seek(pointer)

                    f.write("1")
                    print("delete complet ok")

                    break




    else:

        print("ronge choise try again?")
        print()
        print()