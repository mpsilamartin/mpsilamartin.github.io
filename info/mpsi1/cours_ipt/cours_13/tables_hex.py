def addition():
    for i in range(15):
        for j in range(15):
            print(format(i+1,'X')+' + '+format(j+1,'X') + ' = '+format(i+j+2,'X'))

def multiplication():
    for i in range(15):
        for j in range(15):
            print(format(i+1,'X')+' * '+format(j+1,'X') + ' = '+format((i+1)*(j+1),'X'))
