# Backend (Flask Application)

This directory contains the Flask backend for the Sales Prospecting Lead Management App.

## Features

- RESTful API for managing leads and notes.
- PostgreSQL database integration.
- Basic CRUD operations for leads and notes.

## Project Structure

- `app.py`: Main Flask application file containing API endpoint definitions.
- `init_db.py`: Script to initialize the database schema.
- `schema.sql`: SQL file defining the database tables and triggers.
- `requirements.txt`: Python dependencies.
- `Procfile`: For deployment on platforms like Heroku (defines how to run the app).
- `.env`: (Not committed, create your own) For environment variables, primarily `DATABASE_URL`.
  Example `.env` content:
  ```
  DATABASE_URL="postgresql://your_db_user:your_db_password@your_db_host:your_db_port/your_db_name"
  FLASK_APP=app.py 
  FLASK_ENV=development 
  ```
- `tests/`: Contains backend unit tests.
  - `test_app.py`: Example tests for API endpoints.

## Setup and Running Locally

1.  **Prerequisites:**
    - Python 3.8+
    - PostgreSQL server running and accessible.
    - Git

2.  **Clone the main repository (if not already done):**
    ```bash
    # Navigate to your projects directory
    git clone <main-repository-url>
    cd <main-repository-directory>/backend
    ```

3.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    # venv\Scripts\activate
    # On macOS/Linux
    # source venv/bin/activate
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure Environment Variables:**
    - Create a `.env` file in the `backend` directory.
    - Add your `DATABASE_URL`. For example:
      `DATABASE_URL="postgresql://postgres:mypassword@localhost:5432/sales_leads_db"`
    - You might also want to set `FLASK_APP=app.py` and `FLASK_ENV=development`.

6.  **Initialize the Database:**
    - Ensure your PostgreSQL server is running and you have created the database specified in `DATABASE_URL`.
    - Run the initialization script:
      ```bash
      python init_db.py
      ```
      This will create the necessary tables if they don't exist.

7.  **Run the Flask Development Server:**
    ```bash
    flask run
    ```
    The backend API should now be running, typically at `http://127.0.0.1:5000`.

## API Endpoints

(Refer to `app.py` for the most up-to-date list and details)
- `GET /leads`: Fetches all leads.
- `POST /leads`: Adds a new lead.
- `GET /leads/<lead_id>`: Fetches a specific lead.
- `PUT /leads/<lead_id>`: Updates a specific lead.
- `DELETE /leads/<lead_id>`: Deletes a specific lead.
- `GET /leads/<lead_id>/notes`: Fetches notes for a specific lead.
- `POST /leads/<lead_id>/notes`: Adds a note to a specific lead.

## Testing

- Placeholder unit tests are located in the `tests/` directory.
- To run tests (requires `pytest` and `pytest-mock` to be installed in your venv):
  ```bash
  # Ensure you are in the 'backend' directory with venv activated
  # You might need to set PYTHONPATH if imports are tricky from root:
  # export PYTHONPATH=. (Linux/macOS) or set PYTHONPATH=. (Windows) from project root
  # Or, more simply from the project root:
  python -m pytest backend/tests 
  ```
  (The exact command might need adjustment based on your project root and how pytest discovers tests).
  The tests in `test_app.py` primarily mock the database connection.

## Deployment

- The application is configured for deployment using Gunicorn (see `Procfile`).
- Ensure `DATABASE_URL` is set correctly in the production environment.
- CORS is enabled. For production, restrict `CORS(app, origins="https://your-frontend-domain.com")` in `app.py`.
- Dependencies are listed in `requirements.txt`.
- Platforms like Heroku, Render, or AWS Elastic Beanstalk can be used.
- Remember to run `init_db.py` (or your migration scripts) in the production environment to set up the database.
```
