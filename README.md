# Simple Weather Station

This project simulates weather data, provides a REST API for access, and includes a basic frontend display with a perfectly centered div :P. Built using Python, Node.js, and Docker.

## Prerequisites

- Docker
- Docker Compose
- Node.js and npm (if working on the frontend or modifying the API)
- Python (if working on the weather data generator)

## Setup

### Clone the repository:

```bash
git clone https://github.com/josh-tracey/weather-station.git
```

### Building and Running

Build the Docker images:
```bash
docker-compose build
```

Run the containers:
```bash
docker-compose up -d
```

## Accessing the Application

- Weather API: Available at http://localhost:3000/weather
- Frontend: Available at http://localhost/

Stopping the Application

```bash
docker-compose down
```

