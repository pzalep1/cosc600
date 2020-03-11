import random
import time
def main():
    get = input('Enter a positive Integer: ');
    length = int(get)
    array = [random.randint(-5000, 5000) for iter in range(length)]
    maxSum = 0;

    startTime = time.time();
    print(startTime);
    for i in range(len(array) + 1):
        for j in range(i, len(array) + 1):
            thisSum = 0;

            for k in range(j, len(array)):
                thisSum = thisSum + array[k];
            if thisSum > maxSum:
                maxSum = thisSum;
    print(maxSum);
    print(time.time() - startTime);

main()

