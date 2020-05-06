import random
f = open("quotes.txt")
quotes = f.readlines()
f.close()

#last = 13
#rnd = random.randint(0, last)
print(quotes[0])
print(quotes[1])
print(quotes[3])
print(quotes[9])
print(quotes[-1])
