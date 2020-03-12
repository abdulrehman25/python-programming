profile_points = 0
question_1 = {"upvotes":2,"downvotes":5,"points":0}
question_2 = {"upvotes":10,"downvotes":0,"points":0}

questions = [question_1,question_2]

answer_1 = {"accepted":True,"points":0,"downvotes":0,"upvotes":0}
answer_2 = {"accepted":True,"points":0,"downvotes":0,"upvotes":10}
answer_3 = {"accepted":False,"points":0,"downvotes":2,"upvotes":3}

answers = [answer_1,answer_2,answer_3]


def answer_points_calculator(answer):
    profile_points = 0

    if answer["accepted"]:
        answer["points"] +=15
        profile_points += 15

    for i in range(answer["downvotes"]):
        answer["points"] -=2
        profile_points -= 2

    for i in range(answer["upvotes"]):
        answer["points"] +=10
        profile_points += 10
    return profile_points


def question_points_calculator(question):
    profile_points = 0
    for i in range(question["downvotes"]):
        question["points"] -=2
        profile_points -= 2
    for i in range(question["upvotes"]):
        question["points"] +=10
        profile_points += 10
    return profile_points


for answer in answers:
    profile_points += answer_points_calculator(answer)
for question in questions:
    profile_points += question_points_calculator(question)
print("Total Profile Points are {}:".format(profile_points))
print("All Answer Details:")
for i in answers:
    print(i)
print()
print("All Questions Details:")
for i in questions:
    print(i)