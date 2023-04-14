const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  
  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  for (const userId in completedTasksByUser) {
    console.log(`User ${userId} completed ${completedTasksByUser[userId]} tasks`);
  }
});
