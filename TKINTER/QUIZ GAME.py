import tkinter as tk

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")

        self.questions = [
            "What is the capital of France?",
            "Which planet is known as the Red Planet?"
        ]

        self.answers = [
            ["Paris", "Berlin", "Madrid", "Rome"],
            ["Mars", "Venus", "Jupiter", "Saturn"]
        ]

        self.correct_answers = [0, 2]

        self.current_question = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.questions_label = tkLabel(self.master, text = self.questons )



