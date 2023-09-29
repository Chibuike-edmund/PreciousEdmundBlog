# Precious Edmund Blog Web App with Authentication (Python Django)

## Overview
This is a Blog Web App built using Python Django framework with user authentication. The project idea was inspired by Corey Schafer's Python videos, which provided valuable insights into Django development.

## Features

- **User Authentication**: Users can register, log in, and log out. Password reset functionality is also included.

- **Create, Edit, and Delete Posts**: Authenticated users can create, edit, and delete their own blog posts.

- **View and Comment on Posts**: Users can view all published posts and leave comments on them.

- **Responsive Design**: The app is designed to be mobile-friendly, ensuring a seamless experience across devices.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Chibuike-edmund/PreciousEdmundBlog.git
   ```
   
2. Navigate to the project directory:
   ```
   cd blog-web-app
   ```
   
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use: .\env\Scripts\activate
   ```

4. Install the project dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser (admin account):
   ```
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

8. Visit `http://localhost:8000` in your browser to access the app.

## Usage

- Register a new user or log in with an existing account.
- Once logged in, you can create, edit, and delete your own blog posts.
- View all published posts and leave comments on them.

## Credits

This project was inspired by Corey Schafer's Python videos, which provided valuable guidance on Django development.

- Corey Schafer's YouTube Channel: [Corey Schafer](https://www.youtube.com/user/schafer5)

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to customize and expand upon this base project. Happy coding!