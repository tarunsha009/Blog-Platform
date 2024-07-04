# Blog Platform

## Description
A RESTful API for a blog platform built with Flask and PostgreSQL.

## Features
- User authentication
- Blog post management
- Comment system
- Notifications
- Reporting system
- Localization and Internationalization

## Getting Started
- Clone the repository: `git clone https://github.com/yourusername/your-repository.git`
- Set up your environment: `venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

## Running the App
- Start the app: `python blog_platform/manage.py runserver`

## Contributing
- Create a branch for your feature or bug fix.
- Submit a pull request with a description of your changes.

<!-- ## Code Coverage

[![codecov](https://codecov.io/gh/yourusername/yourrepository/branch/main/graph/badge.svg?token=YOUR_CODECOV_TOKEN)](https://codecov.io/gh/yourusername/yourrepository) -->

## User Authentication

### User Login

**Endpoint:** `POST /blog/User/login`

**Description:** Allows users to log in by providing their username and password. Upon successful login, a JWT token is issued for authentication in subsequent requests.

**Request Body:**

```json
{
    "username": "testuser",
    "password": "testpassword"
}

**Responses:**

200 OK
Content: {"token": "jwt_token_here"}

400 Bad Request
Content: {"message": "Invalid username or password"}
Content: {"message": "Username and password are required"}