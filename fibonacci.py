# variables
sum = 1
prevTerm = 0
val = 0
num = 1

term = input("Enter term number: ")
term = int(term)

for num in range(2, term):
    sum = sum + prevTerm
    prevTerm = sum - prevTerm

if term == 0:
    print(val)
else:
    print(sum)