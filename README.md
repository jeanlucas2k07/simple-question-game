General Knowledge Quiz
This Python script is an interactive General Knowledge Quiz that allows users to test their knowledge on various topics through multiple-choice questions. The script provides immediate feedback and tracks the user's score, offering a replay option at the end.

Features
Randomized Questions: The order of questions is shuffled for each session, providing a unique experience every time.
Immediate Feedback: The user is informed whether their answer is correct or incorrect immediately after each question.
Score Tracking: The script maintains a count of the correct answers and displays the total score at the end.
Replay Option: Users can choose to retake the quiz after completing it.
Code Description
Importing Libraries
The script imports the os and random libraries. The os library is used to clear the console screen, while the random library is used to shuffle the list of questions to ensure they appear in a random order each time the quiz is taken.

Main Loop
The main loop of the script controls the execution of the quiz. It keeps running as long as the user wants to play again. At the start of each loop iteration, the console screen is cleared.

Questions List
A list of questions is defined, where each question includes the question text, four possible answers, and the correct answer. This list is used to present the questions to the user.

User Input
The script prompts the user to enter their name at the start of the quiz. This name is then used in the prompts throughout the quiz.

Question Presentation
For each of the 10 questions in the quiz, the script randomly selects and presents a question to the user along with four answer choices. The script ensures that questions are not repeated within the same quiz session.

Answer Validation
After the user selects an answer, the script checks if the answer is correct. Immediate feedback is provided, indicating whether the user's answer was correct or incorrect. The script also displays the correct answer if the user's answer was wrong.

Score Tracking
The script keeps track of the number of correct answers. At the end of the quiz, the total score is displayed to the user.

Replay Option
After displaying the score, the script asks the user if they want to play the quiz again. If the user chooses to play again, the main loop restarts, and the quiz begins anew. If the user chooses not to play again, the script exits the loop and terminates.
