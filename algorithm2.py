import random
import time
def main():
    get = input('Enter a positive Integer: ');
    length = int(get)
    array = [random.randint(-5000, 5000) for iter in range(length)]
    print(array);
    maxSum = 0;

    startTime = time.time();
    for i in range(len(array)):
        thisSum = 0;
        print
        for j in range(i, len(array)):
            thisSum +=array[j];
            
            if thisSum > maxSum:
                maxSum = thisSum;
    print(maxSum);
    print(time.time() - startTime);

main()

