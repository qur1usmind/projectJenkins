
#1. Use list comprehension to create a list containing a solution for the
#famous FizzBuzz problem. For integers 1 to 100, inclusively, the value
#should be:
#➢ 'Fizz' if divisible by 3
#➢ 'Buzz' if divisible by 5
#➢ 'FizzBuzz' if divisible by both 3 and 5
#➢ The integer itself if not divisible by both 3 and 5



num=[1-101]
#grades_l = [('A' if g>=90 else ('B' if g>=75 else 'C')) for g in grades]

fbproblem = [('Fizz' if n%3==0 else ('Buzz' if n%5==0 else ('FizzBuzz' if n%5==0 and n%3==0 else str(n)))) for  n in num]
print (fbproblem)
