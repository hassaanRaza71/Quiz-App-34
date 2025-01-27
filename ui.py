from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=600, height=500, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            300, 250, width=450, text="Saleem", fill=THEME_COLOR, font=("Ariel", 25, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        true_image = PhotoImage(file="true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


      
      
    
    
    

