nth = 1
prev = 0
prev_2nd = 1
count = True
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
    print(nth)
#
# # Program to check if a number is prime or not
#
# # To take input from the user
# num = int(input("Enter a number: "))
#
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")
#
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#     print(num, "is not a prime number")