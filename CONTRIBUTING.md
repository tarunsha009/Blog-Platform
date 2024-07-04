# Contributing to Blog Platform

First off, thanks for taking the time to contribute! Your help is greatly appreciated.

## How Can You Contribute?

There are several ways you can help make this project better:
1. Reporting bugs.
2. Suggesting new features or enhancements.
3. Writing code for new features or bug fixes.
4. Improving documentation.
5. Reviewing pull requests and offering feedback.

## Getting Started

### Fork and Clone the Repository

1. Fork the repository by clicking the "Fork" button on the GitHub page.
2. Clone your fork to your local machine:
    ```bash
    git clone https://github.com/your-username/blog_platform.git
    cd blog_platform
    ```

### Set Up Your Development Environment

1. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the environment variables. Create a `.env` file in the project root and add your configuration:
    ```env
    FLASK_APP=manage.py
    FLASK_ENV=development
    DATABASE_URL=postgresql://user:password@localhost:5432/blog_platform
    ```

4. Set up the database:
    ```bash
    flask db upgrade
    ```

### Running the Application

To run the application locally:
```bash
flask run
