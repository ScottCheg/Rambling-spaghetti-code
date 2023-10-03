scores = [[],[]]
while True:
    team = input("Enter team 1/2 or type 'e' to exit: ")
    if team == '1' or team == '2':
        if team == '1':
            x = 0
        else:
            x = 1 
        try:
            score = int(input("Enter score: "))
            scores[x].append(score)
        except ValueError:
            print("Please enter a number: ")

    elif team.upper() == 'E':
        break
    else:
        print("Invalid team entry")

tm = 1
lol = 0 
totals = []
print()
for i in scores:
    for x in i:
        print("Team "+str(tm)+": "+str(x))
        lol += x
    totals.append(lol)
    lol = 0
    tm += 1

print("""
Team 1 total:""", totals[0], """
Team 2 total:""", totals[1])
