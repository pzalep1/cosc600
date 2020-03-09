import random
import time
def main():
    get = input('Enter a positive Integer: ');
    length = int(get)
    array = [random.randint(-5000, 5000) for iter in range(length)]
    startTime = time.time();
    maximum = maxSub(array, 0, len(array));
    print(maximum);
    print(time.time() - startTime);

def maxSub(a, left, right):
    if (left == right):
        if a[left] > 0:
            return a[left];
        else:
            return 0;
    center = (left + right)/2;
    maxLeftSum = maxSub(a, left, center);
    maxRightSum = maxSub(a, center + 1, right);

    maxLeftBorderSum = 0;
    leftBorderSum = 0;

    for i in range(center, left, -1):
        leftBorderSum += a[i];
        if leftBorderSum > maxLeftBorderSum:
            maxLeftBorderSum = leftBorderSum;
        
    maxRightBorderSum = 0;
    rightBorderSum = 0;
    for i in range(center + 1, right):
        rightBorderSum += a[i];
        if rightBorderSum > maxRightBorderSum:
            maxRightBorderSum = rightBorderSum;
    return max(maxLeftSum, maxRightSum, maxLeftBorderSum + maxRightBorderSum);

main()