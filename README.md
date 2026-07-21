# Task API (FastAPI CRUD)

A lightweight, high-performance REST API built with Python and FastAPI to manage a to-do list in memory. This project demonstrates full CRUD (Create, Read, Update, Delete) operations, automatic input validation, and HTTP status code handling.

## 🚀 Features & Operations

- **Root & Health Monitoring**: Endpoints for basic API identification and server status verification.
- **In-Memory Storage**: Fast, lightweight task management using native Python data structures.
- **Automatic Validation**: Schema validation powered by Pydantic models.
- **Interactive Documentation**: Auto-generated OpenAPI / Swagger UI testing suite.

---

## 🛠️ Tech Stack & Prerequisites

- **Language**: Python 3.10+
- **Framework**: FastAPI
- **ASGI Server**: Uvicorn
- **Data Validation**: Pydantic

---
---



## 📋 API Endpoints Summary

| HTTP Method | Path | Description | Expected Status Code |
|---|---|---|---|
| `GET` | `/` | API metadata & routes info | `200 OK` |
| `GET` | `/health` | Server health check | `200 OK` |
| `GET` | `/task` | List all tasks | `200 OK` |
| `GET` | `/task/{task_id}` | Fetch a single task by ID | `200 OK` / `404 Not Found` |
| `POST` | `/task` | Create a new task | `201 Created` / `400 Bad Request` |
| `PUT` | `/task/{task_id}` | Update an existing task | `200 OK` / `404 Not Found` |
| `DELETE` | `/task/{task_id}` | Delete a task by ID | `204 No Content` / `404 Not Found` |

---

## 💻 How to Install & Run

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/todo-api-python.git](https://github.com/YOUR_USERNAME/todo-api-python.git)
   cd todo-api-python
2.  install dependencies:
     ```bash
     pip install fastapi uvicorn pydantic

3. Start the server:
     ```bash
      uvicorn main:app --reload

The API will be available at http://localhost:8000.

Access Swagger UI Docs:
Navigate to http://localhost:8000/docs in your browser to test endpoints interactively.

Sample Terminal Testing (curl)
$ curl -i http://localhost:8000/health

HTTP/1.1 200 OK
date: Tue, 21 Jul 2026 11:38:00 GMT
server: uvicorn
content-length: 15
content-type: application/json

{"status":"ok"}


## 🤖 Stage 7: AI Rematch Analysis

### 1. Code Comparison (`git diff`)
- **Structure**: How did the AI structure the model definitions and route order compared to mine?
- **Error Handling**: Did the AI use `HTTPException` natively or standard dictionary returns?
- **Pydantic Methods**: Did the AI use modern Pydantic v2 syntax (`model_dump()`) or legacy methods (`dict()`)?

### 2. What the AI Did Better
- [e.g., "The AI added type hinting across all functions and auto-generated docstrings for route methods."]

### 3. What the AI Got Wrong or Ignored
- [e.g., "The AI used `dict()` instead of `model_dump()`, which triggers deprecation warnings in Pydantic v2."]

### 4. Prompt Refinement Note
- **Initial Prompt**: Specified 5 routes and status codes.
- **Improved Prompt**: *"Ensure Pydantic v2 syntax (`model_dump`) is strictly used instead of legacy `dict()`."*

diff --git a/main.py b/ai-version/ai_version.py
index 9461284..a5137c2 100644
--- a/main.py
+++ b/ai-version/ai_version.py
@@ -1,66 +1,111 @@
-from fastapi import FastAPI,HTTPException,status
-from pydantic import BaseModel
+from typing import Dict, List
+
+from fastapi import FastAPI, HTTPException, status
:
