# distance = {"name":0,"feets":0,"inches":0,"total_inches":0}
distances = []
greater = ""
j = 1

for i in range(2):
    distance = {}
    distance["name"] = j
    distance["feets"] = int(input("Enter Feets for Distance {}:".format(j)))
    distance["inches"] = int(input("Enter Inches for Distance {}:".format(j)))
    distance["total_inches"] = distance["feets"] * 12 + distance["inches"]
    print(distance)
    distances.append(distance)
    j += 1

print()
for k in distances:
    print(k)
print()
if distances[0]["total_inches"] > distances[1]["total_inches"]:
    greater = distances[0]
else:
    greater = distances[1]
print("Greater is {}".format(greater))