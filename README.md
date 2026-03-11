# Flask + Redis Multi-Container Docker App

A multi-container application built with **Flask** and **Redis**, orchestrated using **Docker Compose**. This project demonstrates containerisation of a Python web application with a separate database service, connected via Docker's internal networking.

---

## What It Does

The Flask app exposes two routes:

| Route | Description |
|-------|-------------|
| `/` | Returns a welcome message |
| `/count` | Increments and displays a persistent visit counter stored in Redis |

The visit count persists across requests because it is stored in Redis — not in memory. Each time `/count` is hit, Redis atomically increments the value.

---

## Tech Stack

- **Python / Flask** — Web framework
- **Redis** — In-memory key-value store
- **Docker** — Containerisation
- **Docker Compose** — Multi-container orchestration

---

## Project Structure

```
docker-challenge/
├── app.py                 # Flask app with / and /count routes
├── requirements.txt       # Python dependencies (flask, redis)
├── Dockerfile             # Flask container build instructions
├── redis/
│   └── Dockerfile         # Redis container (FROM redis)
└── docker-compose.yml     # Orchestrates both services
```

---

## Running the App

**Prerequisites:** Docker and Docker Compose installed.

```bash
# Clone the repo
git https://github.com/JaydenMukasa1/Flask-app.git
cd docker-challenge

# Build and start both containers
docker compose up --build
```

The app will be available at `http://localhost:5001`.

To stop the app:

```bash
docker compose down
```

---

## Example Output

**`GET /`**
```
Welcome to my Flask app!
```

**`GET /count`** (increments on each visit)
```
Visit count: 1
Visit count: 2
Visit count: 3
```

---

## How It Works

- Docker Compose spins up two services: `flask-app` and `redis`
- Both containers share a Docker network, allowing Flask to reach Redis using the service name `redis` as the hostname
- The `depends_on` directive ensures Redis starts before the Flask app
- `r.incr('count')` atomically increments the counter in Redis, creating the key automatically on first visit
