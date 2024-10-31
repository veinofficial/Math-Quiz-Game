import random
import time


def question_generator():
    a = random.randint(1,9)
    b = random.randint(1,9)

    operator_list = ["+","-","*"]
    selected_operator = random.choice(operator_list)

    print(f"{a} {selected_operator} {b} = ?")

    if selected_operator == "+":
        return a + b
    elif selected_operator == "-":
        return a - b
    else:
        return a * b


score = 0
question_limit =5
time_limit = 10
question_count = question_limit

while question_count > 0:
    # step 1) generate a random question 
    result = str(question_generator())
    start_time = time.time()

    # step 2) get user answer 
    user_answer=input("Enter your answer:")
    end_time=time.time()

    # step 3) check the answer and time 
    if end_time - start_time < time_limit:    
        if user_answer == result:
            score += 1
            print(f"Perfect, your score is {score}")
        else:
            print("Incorrect answer, try again")        
    else:
        print ("You are too late!")

    question_count-= 1
print(f" final score: {score} out of {question_limit}")