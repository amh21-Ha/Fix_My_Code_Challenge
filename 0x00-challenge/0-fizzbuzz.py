def check(num):
    finalWord = ''
    if num % 3 == 0:
        finalWord += 'Fizz'
    if num % 5 == 0:
        finalWord += 'Buzz'
    return finalWord or num

def FizzLoop(start=0, stop=10, step=1):
    for i in range(start, stop, step):
        print(check(i))

FizzLoop(0, 10)
print("-----")
FizzLoop(0, 50, 5)
