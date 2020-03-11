import random
import time
def main():
    get = input('Enter a positive Integer: ');
    length = int(get)
    array = [random.randint(-5000, 5000) for iter in range(length)]
    maxSum = 0;
    thisSum = 0;

    startTime = time.time();
    for i in range(len(array)):
        thisSum +=array[i];
            
        if thisSum > maxSum:
            maxSum = thisSum;
        elif thisSum < 0:
            thisSum = 0;
    print(maxSum);
    print(time.time() - startTime);

main()