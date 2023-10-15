#general method to  call abstract method
from abc import ABC, abstractmethod

#create a main class
class Option(ABC):
    def __init__(self, text):
        self.text = text

    #need explaination on this 
    @abstractmethod
    def __str__(self):
        pass

class Question(ABC):
    def __init__(self, question_text, options, answer):
        self.question_text = question_text
        self.options = [self.create_option(option) for option in options]
        self.answer = answer

    @abstractmethod
    def create_option(self, text):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Quiz(ABC):
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data
    
    @abstractmethod
    def get_question(self, category, question_number):
        pass

    @abstractmethod
    def is_answer_correct(self, category, question_number, user_answer):
        pass

# Concrete classes implementing the abstractions
class ConcreteOption(Option):
    def __str__(self):
        return self.text

class ConcreteQuestion(Question):
    def create_option(self, text):
        return ConcreteOption(text)

    def __str__(self):
        return self.question_text

class ConcreteQuiz(Quiz):
    def get_question(self, category, question_number):
        category_data = self.quiz_data.get(category, None)
        if category_data:
            question_data = category_data.get(f'q{question_number}', None)
            if question_data:
                return ConcreteQuestion(question_data['question'], question_data['options'], question_data['answer'])
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

# Create a ConcreteQuiz instance
quiz = ConcreteQuiz(quiz_data)

# Example usage:
category = "sport"
question_number = 1
question = quiz.get_question(category, question_number)
if question:
    print(question)
    for idx, option in enumerate(question.options):
        print(f"{idx + 1}. {option}")

    user_answer = input("Enter your answer (1/2/3/4): ")
    if quiz.is_answer_correct(category, question_number, question.options[int(user_answer) - 1].text):
        print("Correct answer!")
    else:
        print("Incorrect answer. The correct answer is:", question.answer)
else:
    print("Invalid category or question number.")
