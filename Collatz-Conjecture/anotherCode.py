numbers = {}
numbers[1] = 0

def collatz(i):
    if (i%2 == 1):
        return (3*i+1)
    else:
        return i/2

def calc_iterations(i):
    if not numbers.has_key(i):
        return 1+calc_iterations(collatz(i))
    else:
        return numbers[i]

max = 0 
for i in range(2, 10001):
    numbers[i] = calc_iterations(i)
    if numbers.get(i) >= numbers.get(max):
        max = i


print max
    

        
