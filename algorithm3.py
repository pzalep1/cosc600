import random
import time
import sys
sys.setrecursionlimit(1500)

def main():
    get = input('Enter a positive Integer: ');
    length = int(get)
    array = [random.randint(-5000, 5000) for iter in range(length)]
    startTime = time.time();
    maximum = maxSum(array, 0, len(array) - 1);
    print(maximum);
    print(time.time() - startTime);

def maxSum(a, left, right):
    if left == right:
       return a[left];
    
    center = (left + right) // 2;

    return max(maxSum(a, left, center), maxSum(a, center + 1, right), maxCross(a, left, center, right));

def maxCross(a, left, center, right):
    sum = 0; leftSum = 0;

    for i in range(center, left - 1, -1):
        sum = sum + a[i];
        if(sum > leftSum):
            leftSum = sum;
    
    sum = 0; rightSum = 0;
    for i in range(center + 1, right + 1):
        sum = sum + a[i];

        if(sum > rightSum):
            rightSum = sum;
    return leftSum + rightSum;

main()