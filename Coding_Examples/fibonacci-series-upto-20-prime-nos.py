nth = 1
prev = 0
prev_2nd = 1
prime_no_count = 0
while prime_no_count <= 20:
    nth = prev + prev_2nd
    prev_2nd = prev
    prev = nth
    for i in range(2, nth):
        if (nth % i) == 0:
            break
    else:
        prime_no_count = prime_no_count + 1
        print("Number {} is Prime".format(nth))
    print(nth)
