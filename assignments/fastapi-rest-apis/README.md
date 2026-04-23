# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework. Students will define data models, create CRUD endpoints, and test requests using JSON inputs and query parameters.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Create a Python file that initializes a FastAPI application and starts the API server.

#### Requirements
Completed program should:

- Import `FastAPI` from the `fastapi` package.
- Create a `FastAPI()` instance named `app`.
- Add a root endpoint (`GET /`) that returns a welcome message.
- Use `uvicorn` to run the app when the file is executed directly.

### 🛠️ Define API Data Models

#### Description
Create Pydantic models for representing inventory items and new item requests.

#### Requirements
Completed program should:

- Define an `Item` model with fields for `id`, `name`, `category`, `price`, and `in_stock`.
- Define a model for creating new items without the `id` field (for POST requests).
- Use the models for request validation and response formatting.

### 🛠️ Add CRUD Endpoints

#### Description
Build endpoints to list items, retrieve a single item, add new items, update items, and delete items.

#### Requirements
Completed program should:

- Implement `GET /items` to return a list of all items.
- Implement `GET /items/{item_id}` to return a specific item by ID.
- Implement `POST /items` to add a new item and return it with a generated ID.
- Implement `PUT /items/{item_id}` to update an existing item by ID.
- Implement `DELETE /items/{item_id}` to remove an item by ID.
- Use an in-memory list or dictionary to store items during runtime.

### 🛠️ Support Query Parameters

#### Description
Add query filtering to the item list endpoint so students can search by category or in-stock status.

#### Requirements
Completed program should:

- Accept optional query parameters on `GET /items`, such as `category` and `in_stock`.
- Filter returned items when query parameters are provided.
- Keep the endpoint working when no filters are supplied.
