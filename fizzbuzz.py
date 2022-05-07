# FizzBuzz Game
# Print all number till the max-range but
# 1. for all numbers exactly divisble by 3, print "FIZZ",
# 2. for all numbers exactly divisble by 5, print "BUZZ",
# 3. for all numbers exactly divisble by 3, print "FIZZBUZZ"


print("Please enter the maximum number you want to play this game for:")
max_num = int(input())
for i in range(1, max_num+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0 and i % 5 != 0:
        print("FIZZ")
    elif i % 5 == 0 and i % 3 != 0:
        print("BUZZ")
    else:
        print(i)
