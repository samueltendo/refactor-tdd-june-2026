const express = require('express')
const app = express()


const { randomUUID } = require('crypto')
const todoStore = {}

app.use(express.json())


app.get('/health', (req, resp) => {
    resp.sendStatus(200);
})

function validateTitle(title) {
    if (typeof title !== "string") return false;
    return title.trim().length > 0;
}

app.post("/todos", (req, res) => {
  const { title } = req.body;

  if (!validateTitle(title)) {
    return res.status(400).json({ error: "invalid title" });
  }

  const id = randomUUID();
  todoStore[id] = { id, title, completed: false };
  res.status(201).json(todoStore[id]);
});

app.get("/todos", (req, res) => {
  res.status(200).json(Object.values(todoStore));
});

module.exports = app;
module.exports.validateTitle = validateTitle;
