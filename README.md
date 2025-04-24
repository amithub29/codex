# Codex - Lightweight & Digital Notebook

**This is a simple note-taking API built using Python + Flask. It is containerized using Docker for easy development and deployment.**

---

![Image](https://github.com/user-attachments/assets/346ffaf3-adce-4bc0-a424-009dfbd92d2f)

## Project Structure

- `app.py` – Main Flask application
- `requirements.txt` – Python dependencies
- `Dockerfile` – Build instructions for Docker image
- `README.md` – Project documentation

## How to Set Up the Project

### Prerequisites

- Docker installed

### Steps

1. Clone the repository or download the files.

2. Open a terminal and navigate to the project directory.

3. Build the Docker image:

   `docker build -t codex-app .`

4. Run the container:

   `docker run -p 5100:5500 codex-app`

   This maps port 5500 inside the container to 5100 on your machine.

## Usage

Once the app is running, you can access it at:

`http://localhost:5100/`

### Available Endpoints

- `/` – Returns the homepage/index

- `/version` – Returns the current version of the API

## Example Requests

`curl http://localhost:5100/`

`curl http://localhost:5100/version`

## Coming Soon

- _Other endpoints for full functionality_
- _Persistent storage (e.g., SQLite, PostgreSQL)_
- _User authentication_
- _Frontend UI for managing notes_
