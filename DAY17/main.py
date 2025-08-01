from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for que in question_data:
    q_text = que["text"]
    q_answer = que["answer"]

    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")