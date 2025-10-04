# Employee Management System

A Django-based Employee Management System that allows you to manage employee information efficiently.

## Features

- Add, edit, and delete employees
- View employee details
- Responsive design with Bootstrap
- Modal-based interactions for better UX

## Tech Stack

- Django
- Bootstrap 5
- SQLite (Development) / PostgreSQL (Production)
- Bootstrap Icons

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/yourusername/employee-management.git
cd employee-management
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Run the development server
```bash
python manage.py runserver
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=False
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432
```

## Deployment

This project is configured for deployment on Render.com. Follow these steps:

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Add the environment variables
4. Deploy!

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.