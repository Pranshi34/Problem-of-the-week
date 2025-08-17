import math

def gcd_no(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)
    return result

n = int(input())
numbers = list(map(int, input().split()))
print(gcd_no(numbers))
