print("🧠 **Welcome to the Python Quiz**")
playing =input ("👉 Do you want to play: ")

if playing.lower() !="yes":
    print("👋 Exiting... see you next time!")
    quit()

print ("Okay ! Let's play :)")
score = 0

answer = input(" ❓ What does CPU stand for?")
if answer.lower() == "central processing unit":
    print ("✅ Correct !")
    score +=1
else:
    print ("❌ Incorrect ! It's Central Processing Unit.\n")

answer = input ("What does GPU stand for? ")
if answer.lower()=="graphic processing unit":
    print("✅ Correct!")
    score +=1
else:
    print("❌ Incorrect !  It's Graphics Processing Unit.\n")    

answer = input("What does PS stand for? ")
if answer.lower() =="power supply":
    print ("✅ Correct !")
    score +=1
else:
    print("❌ Incorrect !  It's Power Supply.\n")   

answer= input("What does RAM stand for?")
if answer.lower()=="random access memory":
    print("✅ Correct !")
    score +=1
else:
    print("❌ Incorrect !  It's Random Access Memory.\n")          


print(f"🎯 You got {score} out of 4 questions correct!")
print(f"📊 Your score: {(score / 4) * 100}%")
