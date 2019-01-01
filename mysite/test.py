

def addnum(num1=0, num2=0):
    try:
        num1 = int(num1)
    except:
        return('Num1 must be a number')
    try:
        num2 = int(num2)
    except:
        return('Num2 must be a number')

    return num1 + num2

print(addnum(4,'5'))