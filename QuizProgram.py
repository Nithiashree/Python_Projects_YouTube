# a dictionary that stores questions and answers.
# Have a variable that tracks the score of the player.
# Loop thorough the dictionary using the key-value pairs.
# Display each question to the user and allow them to answer.
# Tell them if they are right or wrong.
# Show the final result when the quiz is completed.

quiz = {
    "question1": {
        "question" : "What is the capital of France?",
        "answer" : "Paris"
    },
    "question2":{
        "question": "What is the capital of Germany?",
        "answer":"Berlin"
    },
    "question3":{
        "question":"What is the capital of Japan",
        "answer":"Tokyo"
    },
    "question4":{
        "question":"What is the capital of Italy",
        "answer":"Rome"
    },
    "question5":{
        "question":"What is the capital of Spain",
        "answer":"Madrid"
    },
    "question6":{
        "question":"What is the capital of Portugal",
        "answer":"Lisbon"
    },
    "question7":{
        "question":"What is the capital of Switzerland",
        "answer":"Bern"
    },
    "question8":{
        "question":"What is the capital of Austria",
        "answer":"Vienna"
    },
}

score = 0

for key, value in quiz.items(): #loop through a dictionary
    print(value["question"])
    answer = input("Answer is:")

    if answer.lower() == value["answer"].lower():
        print("correct answer!")
        score = score + 1
        print("Your score is:" + str(score))

        print("")
        print("")

    else:
        print("wrong answer!")
        print("The answer is:" + value["answer"])
        print("score is:" + str(score))

        print("")
        print("")

#to enhance your code, you can also enter the final results as follows:

print("You scored: " + str(score) + "out of 8 questions correctly")
print("Congratulations!.Your percentage is:" + str(int(score/8*100)) + "%")
