import sys

# Gets an integer from the user and checks to make sure that it is an integer and it is greater than 
def getInt():
    while True:
        convert = raw_input('Enter a positive Integer to convert to binary: ');
        if convert.isdigit():
            if convert > 0:
                return int(convert)
        elif type(convert) != int:
            print('Not a positive integer')

def convertNum(num):
    if num < 2:
        sys.stdout.write(str(1))
    elif num%2 == 0:
        convertNum(num/2)
        sys.stdout.write(str(0))
    elif num%2 == 1:
        convertNum(num/2)
        sys.stdout.write(str(1))

def main():
    cont = 'Y'
    while cont == 'Y' or cont == 'y':
        convert = getInt()
        sys.stdout.write(str(convert) + ' in binary is: ')
        convertNum(convert)
        print
        cont = raw_input('Enter Y to continue converting numbers or any other key to stop: ')

main()


