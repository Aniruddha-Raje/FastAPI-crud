# 🚀 FastAPI App Template

A scalable and modular FastAPI application using PostgreSQL and SQLAlchemy (async), with:

- ✅ PostgreSQL models for User, Profile, and Post
- ✅ 1:1, 1:N, M:1 associations
- ✅ CRUD APIs
- ✅ CORS support
- ✅ Daily log file rotation
- ✅ Swagger documentation
- ✅ Healthcheck and version endpoints

---

# 📁 Project Structure

```
fastapi_project/
├── app/
│ ├── api/ # Route handlers (users, posts, profiles, meta)
│ ├── core/ # Settings, DB connection, logging
│ ├── models/ # SQLAlchemy ORM models
│ ├── schemas/ # Pydantic models
│ ├── services/ # Business logic
│ └── main.py # App entrypoint
├── .env # Environment config
├── requirements.txt
└── README.md
```
---

# 🧪 Setup Instructions

## 1. 📦 Install dependencies


`pip install -r requirements.txt`

## 2. ⚙️ Setup environment
Create a .env file in the root directory:

DATABASE_URL=postgresql+asyncpg://your_user:your_password@localhost/your_db

## 3. 🚀 Run the app
`uvicorn app.main:app --reload`

# 🔌 API Endpoints

| Method | Endpoint                       | Description              |
| ------ | ------------------------------ | ------------------------ |
| GET    | `/api/healthcheck`          | Health check             |
| GET    | `/api/version`              | Returns app version      |
| GET    | `/api/users`                | List all users           |
| POST   | `/api/users`                | Create a new user        |
| GET    | `/api/users/{id}`           | Get a user by ID         |
| DELETE | `/api/users/{id}`           | Delete a user            |
| GET    | `/api/posts`                | List all posts           |
| POST   | `/api/posts?user_id={user}` | Create a post for a user |
| GET    | `/api/profiles/{user_id}`   | Get profile by user ID   |

# 📜 Swagger UI
Once the app is running, visit:

http://localhost:8000/docs – Interactive API documentation
http://localhost:8000/redoc – ReDoc documentation

# 🛠 Developer Scripts
uvicorn app.main:app --reload
