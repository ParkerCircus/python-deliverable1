print("Welcome to GC Mini Golf! What is your name?")
response = input()
print(f"Hi, {response}! Would you like to play 3 or 6 holes of golf today?")
num_holes = input()
if num_holes == "3":
    print("How many puts for hole 1? (par is 3)")
    hole_1 = input()
    print("How many puts for hole 2? (par is 3)")
    hole_2 = input()
    print("How many puts for hole 3? (par is 3)")
    hole_3 = input()
    par = int(hole_1) + int(hole_2) + int(hole_3) - 9
    if par == 0:
        print(f"Good game {response}. Your total score was: " + str(par))
    elif par > 0:
        print(f"Nice try, {response}... Your total score was: +" + str(par))
    else:
        print(f"Great job, {response}! Your total score was: " + str(par))
elif num_holes == "6":
    print("How many puts for hole 1? (par is 3)")
    hole1 = input()
    print("How many puts for hole 2? (par is 3)")
    hole2 = input()
    print("How many puts for hole 3? (par is 3)")
    hole3 = input()
    print("How many puts for hole 4? (par is 3)")
    hole4 = input()
    print("How many puts for hole 5? (par is 3)")
    hole5 = input()
    print("How many puts for hole 6? (par is 3)")
    hole6 = input()
    par_ = int(hole1) + int(hole2) + int(hole3) + int(hole4) + int(hole5) + int(hole6) - 18
    if par_ == 0:
        print(f"Good game {response}. Your total score was: " + str(par_))
    elif par_ > 0:
        print(f"Nice try, {response}... Your total score was: +" + str(par_))
    else:
        print(f"Great job, {response}! Your total score was: " + str(par_))
else:
    print("Invalid answer. Thanks for stopping by.")






