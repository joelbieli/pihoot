# Pihoot Frontend

## Abstract

The frontend of the pihoot project handles all of the interaction with the game master. Using it you can create, update, edit, delete, play and host quizzes. Once at least one playable quiz has been created (please use the frontend to find out how playable quizzes are defined) the game master can choose it from a list of playable quizzes. Once he has chosen to play a quiz, players can use the Raspberry Pis and enter a color code to join the game. As soon as any new players join the game they appear on the screen. Once all players that want to play have joined, the game master can choose to start the game.

Once the game has been started it goes through the following cycle for every question that is available in the quiz being played:

1. Only the question is displayed for 5 seconds.

2. The question along with the answer is displayed for 15 seconds but is dismissed if all players that have joined the game have answered.

3. The correct questions are shown and an opportunity to discuss the correct answers arises. Once the game master wishes to move on they may click the "Next question" button or they can quit the game by using the "Return to home" button.

4. Once the correct answers have been seen the scoreboard is shown. It displays every player in descending order with the scores that they got when answering to the questions.

When the very last question is over, the final scorebaord is displayed with the 3 best players on a podium.

## Quick Start Guide

*Note that you will need to have [Node.js](https://nodejs.org) installed.*

This server will refresh automatically as soon as you save the file. You can find the server at [localhost:5000](http://localhost:5000).

### Get started

This project is running on npm, so you'll need to install the dependencies with `npm install` first. Once that's done you go ahead and start [Rollup](https://rollupjs.org).

```bash
npm run dev
```

Navigate to [localhost:5000](http://localhost:5000). You should see your app running. Edit a component file in `src`, save it, and reload the page to see your changes.

By default, the server will only respond to requests from localhost. To allow connections from other computers, edit the `sirv` commands in package.json to include the option `--host 0.0.0.0`.

### Building and running in production mode

To create an optimised version of the app:

```bash
npm run build
```

It's recommended that you run the newly built app with `npm run start`. This uses [sirv](https://github.com/lukeed/sirv), which is included in your package.json's `dependencies` so that the app will work when you deploy to platforms like [Heroku](https://heroku.com).<br>
If you would just like to deploy the files to a server, copy the contents of the public folder to the server running the website.
