# Pihoot Frontend

This is the frontend for the pihoot project that the game master can use to create quizzes and play them once he's ready.

*Note that you will need to have [Node.js](https://nodejs.org) installed.*

This server will refresh automatically as soon as you save the file. You can find the server at [localhost:5000](http://localhost:5000).


## Get started

This project is running on npm, so you'll need to install the dependencies with `npm install` first. Once that's done you go ahead and start [Rollup](https://rollupjs.org).

```bash
npm run dev
```

Navigate to [localhost:5000](http://localhost:5000). You should see your app running. Edit a component file in `src`, save it, and reload the page to see your changes.

By default, the server will only respond to requests from localhost. To allow connections from other computers, edit the `sirv` commands in package.json to include the option `--host 0.0.0.0`.


## Building and running in production mode

To create an optimised version of the app:

```bash
npm run build
```

You can run the newly built app with `npm run start`. This uses [sirv](https://github.com/lukeed/sirv), which is included in your package.json's `dependencies` so that the app will work when you deploy to platforms like [Heroku](https://heroku.com).
