class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def display_question(self):
        current_question = self.questions[self.current_question_index]
        print(f"Question {self.current_question_index + 1}: {current_question.text}")
        for index, choice in enumerate(current_question.choices, start=1):
            print(f"{index}. {choice}")

    def get_user_answer(self):
        choice = input("Enter your choice (1-4): ")
        return int(choice)

    def check_answer(self, user_answer):
        current_question = self.questions[self.current_question_index]
        if current_question.check_answer(user_answer):
            self.score += 1
            print("Correct answer!")
        else:
            print("Wrong answer!")

    def display_score(self):
        total_questions = len(self.questions)
        print(f"You scored {self.score} out of {total_questions}.")

    def next_question(self):
        self.current_question_index += 1

    def start(self):
        for _ in range(len(self.questions)):
            self.display_question()
            user_answer = self.get_user_answer()
            self.check_answer(user_answer)
            self.next_question()

        self.display_score()


# Creating Quiz Questions
question1 = Question("What is the capital of France?", ["London", "Paris", "Rome", "Berlin"], 2)
question2 = Question("What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Earth", "Neptune"], 1)
question3 = Question("Who painted the Mona Lisa?", ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo"], 3)
question4 = Question("What is python?", ["A high level programming language", "A low level programming language", "A database management system", "An operating system"],1)
question5 = Question("What is the print('Hello'+5)?", ["Hello5", "Hello","5", "TypeError: can only concatenate str"],4)

# Creating Quiz and Adding Questions
quiz = Quiz()
quiz.add_question(question1)
quiz.add_question(question2)
quiz.add_question(question3)
quiz.add_question(question4)
quiz.add_question(question5)
# Starting the Quiz
quiz.start()
