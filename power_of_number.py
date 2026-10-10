def power(x , n):
    if n==0:
        return 1
    if n<0:
        return 1/power(x,-n)
    half = power(x , n//2)
    if n%2==0:
        return half*half
    else:
        return half*half*x
print(power(2,10))
