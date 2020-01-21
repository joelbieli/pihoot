# Backend

## Abstract

The backend is primarily responsible for data management. The starting/ending of quizzes/questions as well as the timing is handled by the frontend. The backend merely generates data such as the id and colors of players and answers. In addition, it does some data validation to notify the frontend and Raspberry Pis of problems. The backend follows REST principles as best as possible, even for the web sockets.

## Quick Start Guide

1. Import the project as a Gradle project into your IDE, IntelliJ is recommended.
2. Make sure all the dependencies have been imported, if not reimport the Gradle project.
3. Execute the `bootRun` Gradle task. This task has to be run at least once for Gradle to generate important code. It is recommended that the application is always run in this fashion.
