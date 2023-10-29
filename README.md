# Group-13

## CampusEats

CampusEats is a web application for [briefly describe what the app does and its purpose // TODO].

## Table of Contents
1. [Getting Started](#2)
2. Prerequisites
3. Installation
4. Running the App
5. Features
6. Directory Structure
7. Development Guidelines
8. Contributors
9. License

## <a id="2">Getting Started</a>
### Prerequisites

    Before you begin, ensure you have met the following requirements:

    [Python 3.x]

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/yourusername/CampusEats.git

    ```

2. Navigate to the project directory:
    ```python
    cd CampusEats
    ```

3. Set up a virtual environment (recommended):
    ```python
    python -m venv venv
    ```

4. Activate the virtual environment:

    ```python
        On Windows (Command Prompt):
        venv\Scripts\activate
        On macOS and Linux:
        source venv/bin/activate
    ```

5. Install project dependencies:
    ```python
    pip install -r requirements.txt
    Installation
    ```
## Running the App
Run the following commands in steps:

```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata apps/restaurants/fixtures/restaurants.json
python manage.py loaddata apps/review/fixtures/reactions_fixture.json
python manage.py runserver

## Features
[Describe the app's features and functionality. List any user roles and their interactions with the app.]

## Directory Structure
```
CampusEats/
├── campus_eats/
├── apps/
│   ├── user/
│   ├── restaurants/
    |...
├── templates/
├── static/
├── media/
├── requirements.txt
├── manage.py
```


- campus_eats/: Contains the core Django project configuration and settings.

- apps/: Houses individual Django applications (e.g., "user" and "restaurants") that encapsulate specific features and functionality of the project.

- templates/: Stores HTML template files used for rendering dynamic web pages.

- static/: Holds static files (e.g., CSS, JavaScript, images) used by the project's web pages.

- media/: Reserved for user-uploaded media files (e.g., user avatars, restaurant images) separate from static assets.

- requirements.txt: Lists project dependencies and their versions, enabling easy installation and replication of the development environment.

- manage.py: A Django management script that facilitates various project-related tasks, including running the development server, managing database migrations, and more.

## Development Guidelines
[Provide guidelines and best practices for development. Include information on coding style, commit messages, and any other development standards your team should follow.]

## Contributors
1. Tisha Jhabak
2. Vivian Ha
3. Olivia Smith
4. Amanda
5. Roy

## Licence



