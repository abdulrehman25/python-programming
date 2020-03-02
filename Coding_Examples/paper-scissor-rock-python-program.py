print("!!! Game Abbreviations !!!")
print("1: Paper")
print("2: Scissor")
print("3: Rock")
print()
print("!!! Game Rules !!!")
print("Paper(1) VS Rock(3)  --> Paper(1) Wins")
print("Paper(1) VS Scissor(2)  --> Scissor(2) Wins")
print("Scissor(2) VS Rock(3)  --> Rock(3) Wins")
print()
print("!!! Same will Tie !!!")
print()
user1_choice = int(input("User 1 enter Choice ( 1 , 2 , 3 ) ?:"))
user2_choice = int(input("User 2 Enter Choice ( 1 , 2 , 3 ) ?:"))

if user1_choice == user2_choice:
    print("Tie")
elif user1_choice == 1 and user2_choice == 2:
    print("Scissor Wins --> User 2 Wins")
elif user1_choice == 1 and user2_choice == 3:
    print("Paper Wins --> User 1 Wins")
elif user1_choice == 2 and user2_choice == 1:
    print("Scissor Wins --> User 1 Wins")
elif user1_choice == 2 and user2_choice == 3:
    print("Rock Wins --> User 2 Wins")
elif user1_choice == 3 and user2_choice == 1:
    print("Paper Wins --> User 2 Wins")
elif user1_choice == 3 and user2_choice == 2:
    print("Rock Wins --> User 1 Wins")