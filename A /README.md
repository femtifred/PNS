# Sales Prospecting Lead Management App

This web application helps users find and manage leads for sales prospecting. It automatically searches for potential leads based on user-defined criteria, stores them in a database, and provides a user-friendly interface for browsing, filtering, and updating leads.

## Features

- Automated lead generation from public data sources, APIs, or web scraping.
- Storage of lead information, including company name, contact person, organization number, industry, website, status, and summary.
- User-friendly interface for managing leads, including updating statuses and adding notes.
- Tracking of lead sources to identify the most effective ones.
- User interface and all generated text in Norwegian.

## Project Structure

- `frontend/`: Contains the React (Vite) frontend application code. See `frontend/README.md` for details.
- `backend/`: Contains the Flask backend application code. See `backend/README.md` for details.

## Core Technologies

- **Backend:** Python, Flask, PostgreSQL
- **Frontend:** JavaScript, React, Vite, Axios
- **Styling:** Plain CSS

## Getting Started

Detailed setup and running instructions are available in the README files within the `frontend` and `backend` directories.

### Prerequisites

- Python 3.8+
- Node.js (latest LTS version recommended, for npm/yarn)
- PostgreSQL server
- Git

### General Setup Outline

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Backend Setup:**
    - Navigate to the `backend` directory.
    - Create a Python virtual environment and activate it.
    - Install dependencies: `pip install -r requirements.txt`.
    - Set up your PostgreSQL database and configure the `DATABASE_URL` in a `.env` file (see `backend/.env.example` if provided, or `backend/.env` structure).
    - Initialize the database: `python init_db.py`.
    - Run the backend server: `flask run`.
    (See `backend/README.md` for more details)

3.  **Frontend Setup:**
    - Navigate to the `frontend` directory.
    - Install dependencies: `yarn install` (or `npm install`).
    - Run the frontend development server: `yarn dev` (or `npm run dev`).
    (See `frontend/README.md` for more details)

4.  **Access the application:**
    - The frontend will typically be available at `http://localhost:5173` (Vite's default).
    - The backend API will be at `http://localhost:5000`. The frontend is configured to proxy requests to this backend during development.

## Features Implemented

- **Lead Management:**
    - Create, Read, Update, Delete (CRUD) operations for leads.
    - Fields: Company Name, Contact Person, Organization Number, Industry, Website, Status, Summary.
    - Status options: Innkommende, Booked, Nei, Ikke svar, Mail, Pass.
- **Notes Management:**
    - Add notes to leads.
    - View notes for leads.
- **User Interface:**
    - All UI text and labels are in Norwegian.
    - Table view for leads with sorting and basic filtering.
    - Forms for adding leads and notes.
    - Inline status updates for leads.
- **Search:** Basic client-side search for leads by company name, contact person, or industry.
- **API:** RESTful API for managing leads and notes.

## Lead Searching (Future Enhancement)

The initial request included automatic searching for leads. This feature is not yet implemented. It would involve:
- Identifying public data sources (e.g., business registries, funding announcement sites, news APIs).
- Developing web scraping or API integration logic in the backend.
- Potentially a new table for `search_tasks` or similar.
- UI for users to define search criteria and trigger searches.

## Testing

- **Backend:** Placeholder unit tests are in `backend/tests/test_app.py` using `pytest`. These mock database interactions.
- **Frontend:** Placeholder component tests are in `frontend/src/__tests__/App.test.jsx` using Vitest and React Testing Library.
- To run tests, refer to the specific READMEs in the `backend` and `frontend` directories.

## Deployment

The application is structured for separate deployment of frontend and backend.
- **Backend (Flask):** Can be deployed to platforms like Heroku, Render, AWS Elastic Beanstalk using Gunicorn. A `Procfile` is included. CORS is configured.
- **Frontend (React/Vite):** Can be deployed as a static site to platforms like Netlify, Vercel, AWS S3. A `netlify.toml` example is provided for proxying API requests.
- Environment variables (e.g., `DATABASE_URL` for backend, `VITE_API_BASE_URL` for frontend API endpoint) need to be configured on the deployment platforms.

See individual `README.md` files in `backend` and `frontend` for more specific deployment considerations.
