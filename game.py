def game_math():
    print("Let's start game: ")
    questions = [
        ('What is the value of 5 + 7 * 3 - 5?', ['a) 26', 'b) 22', 'c) 24', 'd) 20'], 'b'),
        ('What is the square root of 144?', ['a) 10', 'b) 12', 'c) 14', 'd) 20'], 'b'),
        ('If x + (x/4) = 20, what is the value of x?', ['a) 10', 'b) 16', 'c) 12', 'd) 14'], 'b'),
        ('What is the sum of the first 100 positive even integers?', ['a) 5050', 'b) 5150', 'c) 4950', 'd) 5000'], 'a'),
        ('If (1/x) + (1/y) = (1/3) and xy = 15, what is the value of x + y?', ['a) 9', 'b) 12', 'c) 6', 'd) 15'], 'd')
    ]
    
    count = 0
    wrong = 0
    arr = []
    for i, (question, options, correct_answer) in enumerate(questions, start=1):
        print(f'Question {i}: {question}')
        print('Options:')
        for option in options:
            print(option)
        
        user_answer = input('Enter Your answer: ').strip().lower()
        arr.append(user_answer)
        if user_answer == correct_answer:
            count += 1
        else:
            wrong += 1
    print('Your Answer: ')
    for i in range(5):
        print(i, ') ', arr[i], end =" ")
    print()
    return count, wrong


correct_answers, wrong_answers = game_math()
print("Correct Answers:", correct_answers)
print("Wrong Answers:", wrong_answers)
