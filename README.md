# Foundation Platform

## Core Technologies

- **Backend:** Python
- **Web Framework:** Django
- **API Framework:** FastAPI
- **Development Database:** SQLite3

---

## Architecture Overview

1.  **Django (The Core Application - Port 8000):** This is the heart of the platform, handling all structured data, user management, and server-rendered pages. It excels at tasks requiring security, database integrity, and rapid development of traditional web features.

2.  **FastAPI (The AI & High-Performance Service - Port 8001):** This is a specialized service for tasks that are slow or require high concurrency. Its asynchronous nature makes it perfect for handling I/O-bound operations like third-party API calls (e.g., to an LLM) without blocking the rest of the application.

---

## Local Development Setup

Follow these steps to get a local copy of the project up and running.

### 1. Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads/)

### 2. Installation

1.  **Clone the repository:**

    ```bash
    git clone <yhttps://github.com/SelbinyyazS/Foundation.git>
    cd Foundation # Or your actual project folder name
    ```

2.  **Create and activate a virtual environment:**

    - **On Windows (cmd):**
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - **On macOS/Linux:**
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the database:**
    This command reads all migration files and creates the database schema.

    ```bash
    python manage.py migrate
    ```

5.  **There is a step of creating superuser(admin)**
    **But we already have one:**
    username: selbinyyaz
    password: selbi05

    ```bash
    python manage.py createsuperuser
    ```

    **Create an administrative superuser:**
    Follow the prompts to create an admin account for accessing the Django admin panel.

    ```bash
    python manage.py createsuperuser
    ```

### 3. Running the Servers

For development, you must run both services simultaneously in **two separate terminals**.

- **Terminal 1: Start the Django Server**

  ```bash
  python manage.py runserver
  # Django is now available at http://127.0.0.1:8000/
  ```

- **Terminal 2: Start the FastAPI Server**
  ```bash
  uvicorn api.main:app --reload --port 8001
  # FastAPI is now available at http://127.0.0.1:8001/
  ```

### 4. Accessing Key Endpoints

- **Main Site:** `http://127.0.0.1:8000/`
- **Admin Panel:** `http://127.0.0.1:8000/admin/`
- **API Documentation (Swagger UI):** `http://127.0.0.1:8001/docs`

---

## Detailed Project Structure

### `core/` - Django Project Configuration

This directory is the central configuration hub for the Django application.

- `settings.py`: The main settings file. It defines `INSTALLED_APPS` (registering our `users` and `content` apps), database configuration, `AUTH_USER_MODEL` to specify our custom user, and `MEDIA_URL`/`MEDIA_ROOT` for handling file uploads.
- `urls.py`: The root URLconf. This file is the primary URL router. It directs incoming requests to the appropriate app's `urls.py` file (e.g., requests to `/accounts/` are forwarded to `users.urls`) or to a specific view.
- `wsgi.py` / `asgi.py`: Configuration files for deploying the application on production web servers.

### `users/` - User Management App

This Django app encapsulates all functionality related to users.

- `models.py`: Defines the `CustomUser` model, which extends Django's `AbstractUser`. We've overridden the `email` field here to enforce `unique=True`, ensuring no two users can register with the same email address.
- `views.py`: Contains the logic for user-facing pages. The `SignUpView` (a `CreateView`) handles the user registration form.
- `forms.py`: Defines the `CustomUserCreationForm`, which is based on our `CustomUser` model and is used by the `SignUpView`.
- `urls.py`: Contains URLs specific to the `users` app, like `/signup/`. It is included by `core/urls.py` under the `/accounts/` path.
- `admin.py`: Registers the `CustomUser` model with the Django admin site, allowing administrators to manage users through the UI.

### `content/` - Content Management App

This Django app handles everything related to the learning materials.

- `models.py`: Defines the `Content` model. This is the blueprint for our learning materials, including fields like `title`, `description`, a `FileField` for the upload, and a crucial `ForeignKey` to the `CustomUser` model to establish ownership (`creator`).
- `views.py`:
  - `home_view`: Renders the main homepage, querying the database for all `Content` objects to display them.
  - `ContentCreateView`: A `LoginRequiredMixin` protected view that handles the file upload form. It overrides `form_valid` to automatically assign the currently logged-in user as the `creator` of the new content.
- `forms.py`: Defines the `ContentForm`, a `ModelForm` built directly from the `Content` model for creating and uploading new material.
- `urls.py`: Defines content-specific URLs, such as `/upload/`.
- `admin.py`: Registers the `Content` model, making it manageable via the Django admin panel.

### `api/` - FastAPI Service

This directory contains our separate, high-performance API.

- `main.py`: The entry point for the FastAPI service. It initializes the FastAPI `app` instance. Currently, it has a simple root endpoint (`/`) for health checks. This is where we will build out endpoints for the AI mentor and recommendation system. These endpoints will be called by our Django frontend or other services.

### `templates/` - HTML Files

This top-level directory contains all the HTML templates rendered by Django.

- `home.html`: The main homepage. It uses Django's template language to conditionally display content based on user authentication status (`{% if user.is_authenticated %}`) and loops through a list of content to display it (`{% for item in content_list %}`).
- `content_upload.html`: The template for the content upload form. Crucially, its `<form>` tag includes `enctype="multipart/form-data"`, which is required for file uploads.
- `registration/`: This sub-directory holds templates related to authentication.
  - `login.html`: The user login form.
  - `signup.html`: The user registration form.
