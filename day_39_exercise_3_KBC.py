# Exercise 3: Kaun Banega Crorepati game in python

questions = [
    "What is my name?", "Aakash", "Sukesh", "Sudi", "Bibek", 1
],
[
    "What is my birth place?", "india", "USA", "janakpur", "kathmandu", 3
],
[
    "What is my date of birth?", "05 april", "28 march", "03 march", "23 january", 2
],
[
    "Where do i live?", "nepal", "india", "usa", "russia", 1
],

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\n Question for Rs:{levels[i]}\n")
    print(f"{question[0]}\n")
    print(f"1. {question[1]}  2. {question[2]}\n")
    print(f"3. {question[3]}  4. {question[4]}\n")
    reply = int(input("Enter your answer (1-4) or 0 to quit: \n "))
    if (reply == 0):
        money = levels[i - 1]
        break
    if (reply == question[len(question)-1]):
        print(f"Correct answer")
    else:
        print("Wrong answer!")
        break
print(f"You have won Rs:{levels[i]}")
