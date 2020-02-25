def getInt():
    while True:
        convert = raw_input('Enter number of disks: ');
        if convert.isdigit():
            if convert > 0:
                return int(convert)
        elif type(convert) != int:
            print('Not a positive integer')

def moveTower(disk, source, dest, spare):
    if disk == 0:
        return
    else:
        moveTower(disk - 1, source, spare, dest)
        print('Disk ' + str(disk) + ' moved from ' + source + ' to ' + dest)
        moveTower(disk - 1, spare, dest, source)
        

def main():
    cont = 'Y'
    while cont == 'Y' or cont == 'y':
        disks = getInt()
        print('The number of disks' + str(disks))
        moveTower(disks, 'A', 'C', 'B')
        print('Total number of movements: '+ str(pow(2, disks) - 1))
        cont = raw_input('Enter Y to continue moving disks or any other key to exit ')
    

main()
