from abc import ABC, abstractmethod  # Import necessary tools from Python's 'abc' module.

# Create a main class called 'Option.'
class Option(ABC):
    def __init__(self, text):  # When you make an 'Option,' you can give it some 'text.'
        self.text = text  # We stick the 'text' label on our 'Option.'

    @abstractmethod  # We declare an abstract method called '__str__.'
    def __str__(self):  # This is like a placeholder for a special action that will happen later.
        pass  # Right now, we don't know what that action is. It's like an empty slot waiting to be filled.

# Create another main class called 'Question.'
class Question(ABC):
    def __init__(self, question_text, options, answer):
        self.question_text = question_text  # We set the 'question_text' for the 'Question.'
        self.options = [self.create_option(option) for option in options]  # We create 'options' based on the 'Option' class.
        self.answer = answer  # We set the 'answer' for the 'Question.'

    @abstractmethod  # We declare an abstract method called 'create_option.'
    def create_option(self, text):  # This is like a placeholder to create an 'Option.'
        pass  # It's an empty spot for creating an 'Option.'

    @abstractmethod  # We declare another abstract method called '__str__.'
    def __str__(self):  # This is like a placeholder for a special action related to the 'Question.'
        pass  # Just like before, we don't know what the action is yet.

# Create yet another main class called 'Quiz.'
class Quiz(ABC):
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data  # We set the 'quiz_data' for the 'Quiz.'

    @abstractmethod  # We declare abstract methods for 'get_question' and 'is_answer_correct.'
    def get_question(self, category, question_number):  # These methods are like empty slots waiting for specific instructions.
        pass

    @abstractmethod
    def is_answer_correct(self, category, question_number, user_answer):
        pass

# Now, let's create concrete classes that provide the missing details for our abstract placeholders.

# Concrete class for 'Option' to fill in the '__str__' method.
class ConcreteOption(Option):
    def __str__(self):
        return self.text  # Here, we fill in the '__str__' method to return the 'text.'

# Concrete class for 'Question' to provide details for 'create_option' and '__str__' methods.
class ConcreteQuestion(Question):
    def create_option(self, text):
        return ConcreteOption(text)  # Here, we provide instructions for creating an 'Option.'
    
    def __str__(self):
        return self.question_text  # We also fill in the '__str__' method to return the 'question_text.'

# Concrete class for 'Quiz' to provide details for 'get_question' and 'is_answer_correct' methods.
class ConcreteQuiz(Quiz):
    def get_question(self, category, question_number):
        category_data = self.quiz_data.get(category, None)  # We find the specific data based on 'category' and 'question_number.'
        if category_data:
            question_data = category_data.get(f'q{question_number}', None)
            if question_data:
                return ConcreteQuestion(question_data['question'], question_data['options'], question_data['answer'])  # We create a specific 'Question' based on the data.
        return None

    def is_answer_correct(self, category, question_number, user_answer):
        question = self.get_question(category, question_number)  # We get the specific 'Question.'
        if question:
            return user_answer == question.answer  # We check if the 'user_answer' is correct by comparing it to the 'answer.'
        return False  # If we can't find the 'Question,' we return 'False.'

# Sample JSON data representing a quiz with sports and math questions.
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

# We create a 'ConcreteQuiz' instance using our JSON data.
quiz = ConcreteQuiz(quiz_data)

# Example usage:
category = "sport"
question_number = 1
question = quiz.get_question(category, question_number)  # We get a specific 'Question' based on 'category' and 'question_number.'
if question:
    print(question)  # We print the 'Question' text.
    for idx, option in enumerate(question.options):
        print(f"{idx + 1}. {option}")  # We display the available options.
    
    user_answer = input("Enter your answer (1/2/3/4): ")  # We get the user's answer.
    if quiz.is_answer_correct(category, question_number, question.options[int(user_answer) - 1].text):
        print("Correct answer!")  # We check if the answer is correct and provide feedback.
    else:
        print("Incorrect answer. The correct answer is:", question.answer)
else:
    print("Invalid category or question number.")
