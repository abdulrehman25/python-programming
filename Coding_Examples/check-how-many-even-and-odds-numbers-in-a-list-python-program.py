numbers = [24,67,45,34,89,88,21,34,0,5]
evens_list = []
odds_list = []
for number in numbers:
    if number % 2 == 0:
        evens_list.append(number)
    elif number % 2 != 0:
        odds_list.append(number)
print("Even Numbers:{} totol {}".format(evens_list,len(evens_list)))
print("Odd Numbers:{} totol {}".format(odds_list,len(odds_list)))