# Flask + Redis Multi-Container Docker App
Flask + Redis app containerised with Docker Compose, using Docker's internal networking to connect services.

---

## What It Does
| Route | Description |
| --- | --- |
| `/` | Returns a welcome message |
| `/count` | Increments and returns a visit counter, stored in Redis so it persists across requests |

---

## Tech Stack
Python / Flask · Redis · Docker · Docker Compose

---

## Project Structure
```
Flask-app/
├── app.py                 # Flask app with / and /count routes
├── requirements.txt       # Python dependencies (flask, redis)
├── Dockerfile              # Flask container build instructions
├── redis/
│   └── Dockerfile         # Redis container (FROM redis)
└── docker-compose.yml      # Orchestrates both services
```

---

## Running the App
Requires Docker and Docker Compose.

```
git clone https://github.com/JaydenMukasa1/Flask-app.git
cd Flask-app
docker compose up --build
```

App runs at `http://localhost:5001`. Stop with `docker compose down`.

---

## Example Output
```
GET /        → Welcome to my Flask app!
GET /count   → Visit count: 1, 2, 3...
```

---

## How It Works
- Docker Compose spins up two services: `flask-app` and `redis`
- Both share a Docker network, so Flask reaches Redis via the hostname `redis`
- `depends_on` ensures Redis starts first
- `r.incr('count')` atomically increments the counter, creating the key on first visit
