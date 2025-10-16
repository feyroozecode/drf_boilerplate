# Django REST Framework Boilerplate 🚀

A comprehensive, production-ready Django REST Framework boilerplate project designed to help you build scalable REST APIs quickly and efficiently.

## 📚 Table of Contents

1. [🏗️ Project Overview](#-project-overview)
2. [🛠️ Technology Stack](#️-technology-stack)
3. [🏛️ Architecture](#️-architecture)
4. [🚀 Quick Start](#-quick-start)
5. [📁 Project Structure](#-project-structure)
6. [🔐 Authentication](#-authentication)
7. [📊 API Documentation](#-api-documentation)
8. [🧪 Testing](#-testing)
9. [🚀 Deployment](#-deployment)
10. [🤝 Contributing](#-contributing)

---

## 🏗️ Project Overview

This Django REST Framework boilerplate provides a solid foundation for building modern REST APIs. It includes best practices, common patterns, and essential features that you'd need in most API projects.

### ✨ Key Features

- **🔐 JWT Authentication**: Secure JSON Web Token-based authentication
- **📋 Task Management**: Complete CRUD operations with user-specific data
- **🔍 Advanced Filtering**: Search, filter, and pagination capabilities
- **📚 Auto-generated Docs**: Interactive Swagger/OpenAPI documentation
- **🛡️ Security**: Built-in security best practices
- **⚙️ Admin Interface**: Full Django admin integration
- **🧪 Test Coverage**: Comprehensive test suite included
- **🚀 Production Ready**: Configured for easy deployment

---

## 🛠️ Technology Stack

| Component | Version | Description |
|-----------|---------|-------------|
| **Django** | 5.2.7 | Python web framework |
| **Django REST Framework** | 3.16.1 | Powerful and flexible toolkit for building Web APIs |
| **Simple JWT** | 5.5.1 | JWT authentication for DRF |
| **drf-yasg** | 1.21.11 | Yet another Swagger generator for Django REST Framework |
| **django-filter** | 25.2 | Filtering support for Django REST Framework |
| **python-decouple** | 3.8 | Organize settings for different environments |
| **gunicorn** | 23.0.0 | WSGI HTTP Server for production |
| **whitenoise** | 6.11.0 | Static file serving for web apps |

---

## 🏛️ Architecture

### 🎯 Design Principles

1. **Separation of Concerns**: Clear separation between different app functionalities
2. **RESTful Design**: Follows REST conventions and best practices
3. **Security First**: Authentication, authorization, and data validation
4. **Scalability**: Modular structure that can grow with your needs
5. **Developer Experience**: Comprehensive documentation and testing

### 🏢 Application Structure

The project follows Django's app-based architecture with two main applications:

- **👥 Users App**: Handles user registration and authentication
- **📋 Tasks App**: Manages task-specific functionality

### 🔄 Request Flow

```mermaid
graph TD
    A[Client Request] --> B[Django URL Router]
    B --> C[Authentication Middleware]
    C --> D[Permission Check]
    D --> E[View/ViewSet]
    E --> F[Serializer Validation]
    F --> G[Database Operations]
    G --> H[Response Serialization]
    H --> I[JSON Response]
```

---

## 🚀 Quick Start

### 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### ⚡ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd drf_boilerplate
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   touch .env
   ```

   Add your environment variables:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access your API**
   - API Base URL: http://127.0.0.1:8000/api/
   - Swagger Docs: http://127.0.0.1:8000/swagger/
   - Django Admin: http://127.0.0.1:8000/admin/

---

## 📁 Project Structure

```
drf_boilerplate/
├── 📂 core/                   # Django project configuration
│   ├── __init__.py
│   ├── settings.py           # Main settings file
│   ├── urls.py               # Root URL configuration
│   ├── wsgi.py               # WSGI deployment configuration
│   └── asgi.py               # ASGI deployment configuration
├── 📂 users/                 # User management app
│   ├── __init__.py
│   ├── apps.py
│   ├── admin.py              # Django admin configuration
│   ├── models.py             # User models
│   ├── serializers.py        # User data serialization
│   ├── views.py              # User views and API endpoints
│   ├── tests.py              # User app tests
│   └── 📂 migrations/        # Database migrations
├── 📂 tasks/                 # Task management app
│   ├── __init__.py
│   ├── apps.py
│   ├── admin.py              # Task admin configuration
│   ├── models.py             # Task models
│   ├── serializers.py        # Task data serialization
│   ├── views.py              # Task views and API endpoints
│   ├── tests.py              # Task app tests
│   └── 📂 migrations/        # Database migrations
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not tracked by git)
├── .gitignore               # Git ignore rules
├── db.sqlite3               # SQLite database file
└── README.md                # This file
```

---

## 🔐 Authentication

### 🎫 JWT-Based Authentication

This project uses JSON Web Token (JWT) authentication for secure, stateless authentication.

#### **How JWT Authentication Works**

1. **User Registration**: Create an account with email and password
2. **Token Request**: Send credentials to obtain JWT tokens
3. **Access Token**: Include in Authorization header for API requests
4. **Token Refresh**: Use refresh token to get new access token

#### **Authentication Flow**

```mermaid
sequenceDiagram
    participant Client
    participant API

    Client->>API: POST /api/auth/register/ (Register)
    API-->>Client: User created successfully

    Client->>API: POST /api/auth/login/ (Login)
    API-->>Client: Access Token + Refresh Token

    Client->>API: GET /api/tasks/ (with Access Token)
    API-->>Client: Protected data

    Note over Client,API: Access Token expires
    Client->>API: POST /api/auth/token/refresh/
    API-->>Client: New Access Token
```

#### **Using the Authentication**

**Register a new user:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password123",
    "password_confirm": "secure_password123"
  }'
```

**Login and get tokens:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "secure_password123"
  }'
```

**Access protected endpoints:**
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE"
```

**Refresh access token:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "YOUR_REFRESH_TOKEN_HERE"
  }'
```

---

## 📊 API Documentation

### 🔍 Interactive Documentation

Visit **http://127.0.0.1:8000/swagger/** for interactive API documentation where you can:
- View all available endpoints
- Test API calls directly in your browser
- See request/response schemas
- Understand authentication requirements

### 📋 Available Endpoints

#### **Authentication Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/register/` | Register a new user |
| `POST` | `/api/auth/login/` | Login and get JWT tokens |
| `POST` | `/api/auth/token/refresh/` | Refresh access token |

#### **Task Management Endpoints**

| Method | Endpoint | Description | Authentication Required |
|--------|----------|-------------|------------------------|
| `GET` | `/api/tasks/` | List user's tasks | ✅ Yes |
| `POST` | `/api/tasks/` | Create a new task | ✅ Yes |
| `GET` | `/api/tasks/{id}/` | Get specific task | ✅ Yes |
| `PUT` | `/api/tasks/{id}/` | Update task completely | ✅ Yes |
| `PATCH` | `/api/tasks/{id}/` | Partial update task | ✅ Yes |
| `DELETE` | `/api/tasks/{id}/` | Delete task | ✅ Yes |

### 🔍 Query Parameters

**Task List Filtering:**
```bash
# Filter by completion status
GET /api/tasks/?completed=true

# Search in title and description
GET /api/tasks/?search=important

# Pagination
GET /api/tasks/?page=2

# Combine filters
GET /api/tasks/?completed=false&search=urgent&page=1
```

### 📝 Response Format

**Success Response (200 OK):**
```json
{
  "count": 25,
  "next": "http://127.0.0.1:8000/api/tasks/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Complete project documentation",
      "description": "Write comprehensive README and API docs",
      "completed": false,
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

**Error Response (401 Unauthorized):**
```json
{
  "detail": "Authentication credentials were not provided."
}
```

**Error Response (400 Bad Request):**
```json
{
  "title": ["This field is required."],
  "description": ["This field may not be blank."]
}
```

---

## 🧪 Testing

### 🏃‍♂️ Running Tests

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test users
python manage.py test tasks

# Run tests with verbosity
python manage.py test --verbosity=2

# Run tests and generate coverage report (if coverage is installed)
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### 📝 Test Structure

**Users App Tests (`users/tests.py`):**
- User registration validation
- Duplicate email/username prevention
- Password confirmation requirements

**Tasks App Tests (`tasks/tests.py`):**
- Task CRUD operations
- User ownership validation
- Filtering and search functionality
- Authentication requirements

### 🧪 Writing New Tests

Here's an example of how to write tests for your API:

```python
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tasks.models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        data = {
            'title': 'Test Task',
            'description': 'This is a test task'
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_get_tasks(self):
        Task.objects.create(
            user=self.user,
            title='Task 1',
            description='Description 1'
        )
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
```

---

## 🚀 Deployment

### 🐳 Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
```

Create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - SECRET_KEY=your-production-secret-key
      - DATABASE_URL=postgresql://user:password@db:5432/dbname
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=dbname
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### ☁️ Heroku Deployment

1. **Install Heroku CLI**
2. **Login to Heroku**
   ```bash
   heroku login
   ```
3. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```
4. **Set environment variables**
   ```bash
   heroku config:set DEBUG=False SECRET_KEY=your-production-key
   ```
5. **Deploy**
   ```bash
   git push heroku main
   heroku run python manage.py migrate
   ```

### 🔧 Production Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Configure proper database (PostgreSQL recommended)
- [ ] Set secure `SECRET_KEY`
- [ ] Configure CORS settings
- [ ] Set up proper logging
- [ ] Configure static file serving
- [ ] Set up monitoring and alerting
- [ ] Configure backup strategy
- [ ] Review security settings

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### 🍴 Fork and Clone

1. Fork the repository
2. Clone your fork locally
3. Create a feature branch

```bash
git checkout -b feature/your-feature-name
```

### 📝 Development Workflow

1. **Make your changes**
2. **Add tests** for new functionality
3. **Ensure all tests pass**
   ```bash
   python manage.py test
   ```
4. **Check code quality** (if using linters)
5. **Commit your changes**
   ```bash
   git commit -m "feat: add your feature description"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

### 📋 Code Style Guidelines

- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Write tests for new features

### 🐛 Bug Reports

When reporting bugs, please include:
- Description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python version, OS, etc.)

---

## 📞 Support & Contact

If you have questions or need help:

- 📧 Email: [your-email@example.com]
- 💬 Discord: [Your Discord Server]
- 🐛 Issues: [GitHub Issues Page]
- 📚 Documentation: [Link to detailed docs]

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Django REST Framework team for the amazing framework
- Django community for continuous inspiration
- All contributors who help improve this project

---

**Happy Coding! 🎉**

Built with ❤️ using Django REST Framework