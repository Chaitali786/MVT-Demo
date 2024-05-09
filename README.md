# MVT-Demo
Django - Model-View-Template 


---

# Django User Management Project

This Django project is created to demonstrate the basic concepts of user management, including model creation, database population, admin interface usage, and URL routing.

## Project Structure

- **Project Name:** Django User Management Project
- **Author:** Chaitali Deore
- **Date:** 8 MAY 2024

## Project Overview

This project consists of the following components:

1. **Model:**
   - The `User` model is defined with the following fields:
     - First Name
     - Last Name
     - Email

2. **Database Migration:**
   - Database migrations are generated and applied to create the necessary database tables based on the model definition.

3. **Database Population:**
   - A script is created to populate the database with fake user data for testing purposes.

4. **Admin Interface:**
   - Users can be managed through the Django admin interface, allowing for CRUD operations on user records.

5. **Views and URL Routing:**
   - A view is created to render a web page displaying a list of user names and emails.
   - The URL pattern `/users` is configured to route requests to this view.

## Installation and Setup

To set up and run the project locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your_username/django-user-management.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django-user-management
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the project in your web browser at `http://127.0.0.1:8000/`

## Usage

- To access the Django admin interface, go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.
- Navigate to the `/users` page to view the list of user names and emails.



---

