# Social Network API (Django Backend)

This project is a RESTful API backend for a simple social network application, built with Django and Django REST Framework. It allows users to register, log in, create posts, comment on posts, like posts, and more.

## Key Features

* **User Authentication:** User registration and JWT-based login (access and refresh tokens).
* **Post Management (CRUD):** Create, Read, Update, and Delete posts. Only authors can edit/delete their own posts.
* **Title for Posts:** Posts include a `title` field in addition to content.
* **Likes:** Users can like and unlike posts.
* **Comments (CRUD):** Users can add comments to posts. Only comment authors can edit/delete their own comments.
* **Filtering & Ordering:** API endpoints support filtering (e.g., by author, by post) and ordering of results.
* **Search:** Search functionality for posts (e.g., by content, title, author).
* **Permissions:** Custom permissions to ensure data integrity and proper access control.

## Tech Stack

* **Python** (version 3.11.9)
* **Django** (version 5.2.1)
* **Django REST Framework (DRF)** (version 5.16.0)
* **Django REST Framework Simple JWT:** For JSON Web Token authentication.
* **django-filter:** For easy filtering of querysets.
* **django-cors-headers:** For handling Cross-Origin Resource Sharing.
* **SQLite:** Default database for development (can be configured for other databases like PostgreSQL for production).

## Prerequisites

Before you begin, ensure you have the following installed:

* Python (3.8+ recommended)
* pip (Python package installer)
* Git (Version control system)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
Replace YOUR_USERNAME/YOUR_REPOSITORY_NAME with your actual GitHub username and repository name.2. Create and Activate a Virtual EnvironmentIt's highly recommended to use a virtual environment to manage project dependencies.# Create the virtual environment (e.g., named 'venv')
python -m venv venv

# Activate the virtual environment
# On Windows:
# .\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install DependenciesInstall all the required packages using the requirements.txt file.(If you haven't created one yet, do so with pip freeze > requirements.txt after installing packages manually for the first time).pip install -r requirements.txt
If requirements.txt is not yet present, you'll need to install the packages listed in the "Tech Stack" section (e.g., pip install django djangorestframework djangorestframework-simplejwt django-filter django-cors-headers). Then, generate the requirements.txt file.4. Apply Database MigrationsThis will create the necessary database tables based on your Django models.python manage.py makemigrations api
python manage.py migrate
(Replace api with the name of your Django app if it's different).5. Create a Superuser (Optional)This allows you to access the Django admin interface.python manage.py createsuperuser
Follow the prompts to create a username, email (optional), and password.6. Configure CORS (Cross-Origin Resource Sharing)If you are developing a separate frontend (e.g., on http://localhost:3000), you'll need to configure CORS in settings.py. Refer to the django-cors-headers documentation or the setup instructions provided previously (allowing http://localhost:3000 in CORS_ALLOWED_ORIGINS).7. Run the Development Serverpython manage.py runserver
The API will typically be available at http://127.0.0.1:8000/. The main API endpoints will be under /api/ (e.g., http://127.0.0.1:8000/api/posts/).API Endpoints OverviewThe API provides endpoints for user management, posts, and comments. All field names in requests and responses are in English.User Registration: POST /api/users/register/User Login (Get Token): POST /api/token/Refresh Access Token: POST /api/token/refresh/Posts (CRUD, Like, List Likers):GET, POST /api/posts/GET, PUT, PATCH, DELETE /api/posts/{id}/POST /api/posts/{id}/like-unlike/GET /api/posts/{id}/who-liked/Comments (CRUD):GET, POST /api/comments/GET, PUT, PATCH, DELETE /api/comments/{id}/For detailed information on each endpoint, request/response formats, required fields for POST/PUT, and query parameters, please refer to the API Documentation (You should create this separate, more detailed documentation file, like the one we worked on previously with id social_api_documentation).Running Tests(This section can be expanded once tests are written)To run the automated tests for this project (if available):python manage.py test
or for a specific app:python manage.py test api
ContributingContributions are welcome! If you'd like to contribute, please follow these steps:Fork the Project.Create your Feature Branch (git checkout -b feature/AmazingFeature).Commit your Changes (git commit -m 'Add some AmazingFeature').Push to the Branch (git push origin feature/AmazingFeature).Open a Pull Request.Please ensure your code adheres to the project's coding standards and includes tests for new features.LicenseDistributed under the MIT License. See LICENSE file