 Garden Planner API

An API for managing users, gardens, plants, and planting schedules.

## Description

This project implements a RESTful API using Flask and SQLAlchemy to manage data for a garden planner application. It supports CRUD operations for users, gardens, plants, planting schedules, and harvests. The application is backed by a PostgreSQL database and managed with Flask-Migrate for schema migrations. Faker is used to seed the database with mock data.

## API Reference

| Endpoint                         | Method | Description                    |
|----------------------------------|--------|--------------------------------|
| `/users`                         | GET    | Get all users                  |
| `/users`                         | POST   | Create a new user              |
| `/users/<id>`                    | GET    | Get a specific user            |
| `/users/<id>`                    | PUT    | Update a user                  |
| `/users/<id>`                    | DELETE | Delete a user                  |
| `/gardens`                       | GET    | Get all gardens                |
| `/gardens`                       | POST   | Create a new garden            |
| `/gardens/<id>`                  | GET    | Get a specific garden          |
| `/gardens/<id>`                  | PUT    | Update a garden                |
| `/gardens/<id>`                  | DELETE | Delete a garden                |
| `/plants`                        | GET    | Get all plants                 |
| `/plants`                        | POST   | Create a new plant             |
| `/plants/<id>`                   | GET    | Get a specific plant           |
| `/plants/<id>`                   | PUT    | Update a plant                 |
| `/plants/<id>`                   | DELETE | Delete a plant                 |
| `/planting_schedule`            | GET    | Get all planting schedules     |
| `/planting_schedule`            | POST   | Create a planting schedule     |
| `/planting_schedule/<id>`       | GET    | Get a specific schedule        |
| `/planting_schedule/<id>`       | PUT    | Update a planting schedule     |
| `/planting_schedule/<id>`       | DELETE | Delete a planting schedule     |
| `/harvests`                      | GET    | Get all harvests               |
| `/harvests`                      | POST   | Create a harvest               |
| `/harvests/<id>`                 | GET    | Get a specific harvest         |
| `/harvests/<id>`                 | PUT    | Update a harvest               |
| `/harvests/<id>`                 | DELETE | Delete a harvest               |

## Retrospective

### How did the project's design evolve over time?

At first, I was just trying to get something working — mostly just gardens and plants. But as I went along, I realized I needed more structure to represent things like planting dates and harvests. So I added those as separate models, even though I wasn't totally sure I was doing it "the right way." I also went back and changed some things as I learned more about how Flask and SQLAlchemy worked. The design definitely became more complex than I expected, but I think it makes more sense now.

### Did you choose to use an ORM or raw SQL? Why?

I used ORM because it seemed like the recommended approach in Flask, and honestly, raw SQL was kind of intimidating. ORM helped me focus more on the structure of the app without worrying about writing queries by hand. I still don’t feel like I fully understand everything it’s doing under the hood, but it let me build the relationships and handle migrations without too much pain. I might come back and learn more about raw SQL later, though.

### What future improvements are in store, if any?

There’s a lot I could add or improve if I had more time or experience. Some ideas:

- Add authentication so not just anyone can mess with the data.
- Include validation so bad data doesn’t break things.
- Maybe build a simple frontend or visualizer so the API is more useful.
- I heard about Marshmallow for schema validation, which sounds cool but I didn’t get to it.
- I’d like to try some data visualization if I can figure out Ngrok and Colab.

Overall, I feel like I got something functional, even if it’s a little rough around the edges. I learned a ton.
