# App Directory Overview

This directory contains the core FastAPI application code for the Git Gud Stats project. Below is a simple explanation of the main modules:

## `main.py`
- **Purpose:**  
  This is the entry point for the FastAPI application.  
  It sets up the app, configures CORS, includes routers for endpoints, and customizes the OpenAPI schema for documentation.

## `dependencies.py`
- **Purpose:**  
  Contains shared utility functions and dependencies used across the app, such as authentication helpers and header builders for GitHub API requests.

## `models.py`
- **Purpose:**  
  Defines Pydantic models (schemas) for request and response data validation.  
  These models ensure that data exchanged through the API is structured and validated.

---

All API endpoints are organized in the `routers/` subdirectory
