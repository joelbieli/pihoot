# Global Readme

<!-- TODO(joelbieli): Set GitHub Repository to public. -->

## Contents

<!-- TODO(laniw): Update if needed. -->
Each of the parts of the pihoot project (frontend, pi and backend) are in their respective folders. Additionally, there's also the docs folder that should contain the api design doc, use cases and test cases/protocol. Each of the parts have a separate README that should contain a description of the project and a quick start guide to get that part working.

## Abstract

The idea of this project is to create a quiz application that is similar to kahoot. This project isn't based on any of kahoot's code, but built anew from the ground up. There are three main components to the Pihoot project. First, you have the backend that stores all of the data about existing quizzes and running games. It also handles the communication between the web-based frontend and the Raspberry Pis. The web-based frontend is the second part of the project, which is intended to be used by the game master to create, update, edit, delete, play and host quizzes. The last and third part of the project is the Raspberry Pi that is used to answer the questions that appear on the screen that the game master uses to show what's going on. The Raspberry Pi uses four buttons and one LED to allow the player to push the buttons to answer a question and for the player to know what color they are from the LED (Players are identified by colors).

### Web Frontend

The frontend of the pihoot project handles all of the interaction with the game master. Using it you can create, update, edit, delete, play and host quizzes. Once at least one playable quiz has been created (please use the frontend to find out how playable quizzes are defined) the game master can choose it from a list of playable quizzes. Once he has chosen to play a quiz, players can use the Raspberry Pis and enter a color code to join the game. As soon as any new players join the game they appear on the screen. Once all players that want to play have joined, the game master can choose to start the game.

Once the game has been started it goes through the following cycle for every question that is available in the quiz being played:

1. Only the question is displayed for 5 seconds.

2. The question along with the answer is displayed for 15 seconds but is dismissed if all players that have joined the game have answered.

3. The correct questions are shown and an opportunity to discuss the correct answers arises. Once the game master wishes to move on they may click the "Next question" button or they can quit the game by using the "Return to home" button.

4. Once the correct answers have been seen the scoreboard is shown. It displays every player in descending order with the scores that they got when answering to the questions.

When the very last question is over, the final scorebaord is displayed with the 3 best players on a podium.

### Backend

The backend is primarily responsible for data management. The starting/ending of quizzes/questions as well as the timing is handled by the frontend. The backend merely generates data such as the id and colors of players and answers. In addition, it does some data validation to notify the frontend and Raspberry Pis of problems. The backend follows REST principles as best as possible, even for the web sockets.
<!-- TODO(joelbieli): Consider adding a more elaborate backend abstract. (Use the web frontend abstract as an example.) -->

### Pi Frontend

<!-- TODO(kian): Add pi frontend abstract. (Use the web frontend abstract as an example.) -->