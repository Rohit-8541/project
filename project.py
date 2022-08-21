print("Welcome to my game")
playing =input("Do you want to play ? ")
if playing.lower() != "yes":
    quit()
score =0
print("okay let's play")
answer = input("What does CPU Stands for ? ").lower()
if answer == "central processing unit":
    print("correct")
    score += 1
else:
    print("No You are wrong")
    
    
answer = input("What does ALU Stands for ? ").lower()
if answer == "arithmetic logic unit":
    print("correct")
    score += 1
else:
    print("No You are wrong")
    
answer = input("What does RAM Stands for ? ").lower()
if answer == "random access memory":
    print("correct")
    score += 1
else:
    print("No You are wrong")
    
print("You Got " + str(score) + " questions correct")
print("You Got " + str((score/3)*100) + "%.") 



