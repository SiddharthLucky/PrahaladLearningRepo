class Option:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

class Question:
    def __init__(self, question_text, options, answer):
        self.question_text = question_text
        self.options = options
        self.answer = answer

    def display_question(self):
        print(self.question_text)
        for idx, option in enumerate(self.options):
            print(f"{idx + 1}. {option}")

class Quiz:
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data

    def get_question(self, category, question_number):
        category_data = self.quiz_data.get(category, None)
        if category_data:
            question_data = category_data.get(f'q{question_number}', None)
            if question_data:
                options = [Option(option) for option in question_data['options']]
                return Question(question_data['question'], options, question_data['answer'])
        return None

    def is_answer_correct(self, category, question_number, user_answer):
        question = self.get_question(category, question_number)
        if question:
            return user_answer == question.answer
        return False

# Sample JSON data
quiz_data = {
    "sport": {
        "q1": {
            "question": "Which one is the correct team name in NBA?",
            "options": [
                "New York Bulls",
                "Los Angeles Kings",
                "Golden State Warriros",
                "Houston Rockets"
            ],
            "answer": "Houston Rockets"
        }
    },
    "maths": {
        "q1": {
            "question": "5 + 7 = ?",
            "options": [
                "10",
                "11",
                "12",
                "13"
            ],
            "answer": "12"
        },
        "q2": {
            "question": "12 - 8 = ?",
            "options": [
                "1",
                "2",
                "3",
                "4"
            ],
            "answer": "4"
        }
    }
}

# Create a Quiz instance
quiz = Quiz(quiz_data)

# Example usage:
category = "sport"
question_number = 1
question = quiz.get_question(category, question_number)
if question:
    question.display_question()

    user_answer = input("Enter your answer (1/2/3/4): ")
    if quiz.is_answer_correct(category, question_number, question.options[int(user_answer) - 1].text):
        print("Correct answer!")
    else:
        print("Incorrect answer. The correct answer is:", question.answer)
else:
    print("Invalid category or question number.")
