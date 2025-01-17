# Simple WebSocket Using FastAPI

This project demonstrates a simple implementation of WebSockets using FastAPI. The primary goal is to test the limit on the number of concurrent WebSocket connections.

## Prerequisites
- Python 3.9 or higher.

- Poetry for dependency management and packaging.

## Installation

1. Clone the repository:

```
git clone https://github.com/ketchup-ash/fastapi-load-test.git
cd fastapi-load-test
```

2. Install dependencies using Poetry:

```
poetry install
```

## Running the Application

To start the WebSocket server locally, use the following command:

```
poetry run fastapi dev app
```