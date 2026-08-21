print("Assignment 3: Generate Prime numbers upto 20")

for n in range(2, 21):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, end=" ")