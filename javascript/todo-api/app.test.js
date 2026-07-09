// npm install express
// npm install --save-dev jest supertest
//  npm test -- todo-api/app.test.js

const request = require('supertest')
const app = require("./app")
const { validateTitle } = require('./app')

test("Get /health returns 200", async () => {
    const response = await request(app).get("/health");
    expect(response.statusCode).toBe(200);
})

// Validate title tests
test("validateTitle rejects empty string", () => {
  expect(validateTitle("")).toBe(false);
});

test("validateTitle rejects non-string", () => {
  expect(validateTitle(123)).toBe(false);
});

test("validateTitle rejects missing", () => {
  expect(validateTitle(undefined)).toBe(false);
});

test("validateTitle accepts nonempty string", () => {
  expect(validateTitle("Buy milk")).toBe(true);
});

// Creating and retrieving your todos
test("POST /todos valid returns 201", async () => {
  const response = await request(app).post("/todos").send({ title: "Buy milk" });
  expect(response.statusCode).toBe(201);
  expect(response.body.title).toBe("Buy milk");
  expect(response.body.completed).toBe(false);
  expect(response.body).toHaveProperty("id");
});

test("POST /todos invalid title returns 400", async () => {
  const response = await request(app).post("/todos").send({ title: "" });
  expect(response.statusCode).toBe(400);
});

test("GET /todos returns list", async () => {
  await request(app).post("/todos").send({ title: "Buy milk" });
  const response = await request(app).get("/todos");
  expect(response.statusCode).toBe(200);
  expect(Array.isArray(response.body)).toBe(true);
});
