# README.md
# FastAPI CRUD Application

This is a simple CRUD application built with FastAPI.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Kaushik123k/FastApi.git
2. Navigate to the project directory:
    cd FastApi
3. Install the dependencies:
    pip install -r requirements.txt
4. Running the Application
    uvicorn app.main:app --reload
5. Endpoints
    GET /items/ - Retrieve a list of items
    POST /items/ - Create a new item
    GET /items/{item_id} - Retrieve an item by ID
    PUT /items/{item_id} - Update an item by ID
    DELETE /items/{item_id} - Delete an item by ID
