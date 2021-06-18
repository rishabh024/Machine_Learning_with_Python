import random

# it returns a random number between the given range
# both 0 & 10 are included in range
print("number is-", random.randint(0, 10))

# it returns a random number between the given range
# here 1 is included but 5 is not included
print("no-", random.randrange(1, 5))

# it returns a random element from the given sequence, all elements are printed
print(random.choice([1, 2, 3]))

# it returns a list with a random selection from the given sequence
print("list is-", random.choices([1, 2, 3]))

# it returns a random float number between 0 and 1
print("random no-", random.random())

# it returns a random float number between two given parameters
print(random.uniform(1, 5))

# it takes a sequence and returns the sequence in a random order
list = [1, 2, 3]
random.shuffle(list)
print("shuffled list is-", list)
