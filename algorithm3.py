import random
import time
import sys
sys.setrecursionlimit(1500)

def main():
    get = input('Enter a positive Integer: ');
    length = int(get)
    array = [random.randint(-5000, 5000) for iter in range(length)]
    print(array);
    startTime = time.time();
    maximum = maxSum(array, 0, len(array));
    print(maximum);
    print(time.time() - startTime);

def maxSum(a, left, right):
    if left == right:
        if a[left - 1] > 0:
            return a[left - 1]
        else:
            return 0;
    else:
        center = int((left + right)/2);
        maxLeftSum = maxSum(a, left, center);
        maxRightSum = maxSum(a, center + 1, right);

        maxLeftBorderSum = 0;
        leftBorderSum = 0;
       
        for i in range(center, left, -1):
            leftBorderSum += a[i];
            if (leftBorderSum > maxLeftBorderSum):
                maxLeftBorderSum = leftBorderSum;
        
        maxRightBorderSum = 0;
        rightBorderSum = 0;

        for i in range(center + 1, right -1):
            rightBorderSum += a[i];
            if(rightBorderSum > maxRightBorderSum):
                maxRightBorderSum = rightBorderSum;
        print('Sums');
        print(maxLeftBorderSum);
        print(leftBorderSum);
        print(maxRightBorderSum);
        print(rightBorderSum);
        return max(maxLeftSum, maxRightSum, maxLeftBorderSum + maxRightBorderSum);

main()