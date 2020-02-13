import time
check_time = 0.5
path = ''
x=''
y=''
while True:
    with open(path,'rt') as o:
        y=x
        x=o.read()
        if y!= x:
            with open('commands.txt','at+') as c:
                c.write(x+'\n')
        time.sleep(check_time)