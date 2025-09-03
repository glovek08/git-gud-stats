![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi&logoColor=white&style=for-the-badge)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-4B8BBE?logo=uvicorn&logoColor=white&style=for-the-badge)
![HTTPX](https://img.shields.io/badge/HTTPX-Async%20HTTP%20Client-007EC6?logo=httpx&logoColor=white&style=for-the-badge)

![Repo License](https://img.shields.io/github/license/glovek08/holbertonschool-hbnb?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/glovek08/holbertonschool-hbnb?style=for-the-badge)

## Contributors

[![glovek08](https://img.shields.io/badge/Gabriel_Barn-181717?style=for-the-badge&logo=github)](https://github.com/glovek08)
[![federico-paganini](https://img.shields.io/badge/Federico_Paganini-181717?style=for-the-badge&logo=github)](https://github.com/federico-paganini)
[![Martin-DMC](https://img.shields.io/badge/Martin_Marrero-181717?style=for-the-badge&logo=github)](https://github.com/Martin-DMC)


Start Developing:
```
pip install -r requirements.txt
```

Run the server:
```
fastapi dev main.py
```


Set up your GH Token in an .env
```
GITHUB_TOKEN=<Your token>
```


# About `git-gud-stats`

## Introduction

`git-gud-stats` is a Python-based backend service built with the high-performance [FastAPI](https://fastapi.tiangolo.com/) framework. Its purpose is to fetch, process, and serve statistics for any GitHub user by leveraging the power of GitHub's public APIs.

This project utilizes both the **GitHub REST API** for basic user data and the **GitHub GraphQL API** for more complex queries, such as retrieving recent repositories and the primary languages used within them.

## Purpose & Vision

This project serves as a foundational training ground for a more ambitious future application. The primary goals of this initial phase are:

1.  **API Integration:** To learn and implement best practices for interacting with both REST and GraphQL APIs from a backend service.
2.  **Authentication:** To handle authenticated requests securely using GitHub Personal Access Tokens (PATs).
3.  **Asynchronous Programming:** To build a responsive and efficient service using Python's `async/await` syntax with FastAPI and HTTPX.

The long-term vision is to evolve this service into a fully-fledged **GitHub App** that will integrate into another full web application. This future web app will provide a specific client without IT background with filtered but rich insightful visualizations of a user's coding activity, helping them track their progress, understand their language preferences, and "get good" at their craft. This project is the first crucial step in building the robust backend required for that vision.

## Technology Stack

The project is built with a modern, asynchronous Python stack, chosen for its performance and developer-friendly features:

*   **[FastAPI](https://fastapi.tiangolo.com/):** A modern, fast (high-performance) web framework for building APIs with Python.
*   **[Uvicorn](https://www.uvicorn.org/):** A lightning-fast ASGI server, used to run the FastAPI application.
*   **[HTTPX](https://www.python-httpx.org/):** A fully featured asynchronous HTTP client for making requests to the GitHub API.
*   **[Python-dotenv](https://pypi.org/project/python-dotenv/):** A library for managing environment variables, used here to securely load the `GITHUB_TOKEN`.

## Current Features

The API currently provides two main endpoints to gather user statistics:

*   `GET /user/{username}`: Fetches basic public user information from the GitHub REST API.
*   `GET /graphql-user/{username}`: Executes a GraphQL query to get the user's name and their 5 most recently pushed repositories, including the top languages used in each.

It also includes a CORS middleware to allow requests from a local development server (like a Svelte or React frontend) and a simple, secure token authentication system that prioritizes a `Bearer` token from the request header before falling back to an environment variable for development.

