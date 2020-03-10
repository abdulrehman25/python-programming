nth = 0
prev = 0
prev_2nd = 1

for i in range(0,20):
    nth = prev + prev_2nd
    prev_2nd = prev
    prev = nth
    print(nth)
