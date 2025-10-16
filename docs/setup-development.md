# Setup and Development Guide 🛠️

Welcome to the comprehensive setup and development guide for our Django REST Framework boilerplate. This guide will walk you through everything you need to get started, from initial setup to advanced development workflows.

## 📚 Table of Contents

1. [🚀 Quick Start](#-quick-start)
2. [📋 Prerequisites](#-prerequisites)
3. [🔧 Installation](#-installation)
4. [⚙️ Configuration](#️-configuration)
5. [🏃‍♂️ Development Workflow](#️‍♂️-development-workflow)
6. [🧪 Testing](#-testing)
7. [🔍 Debugging](#-debugging)
8. [📊 Database Management](#-database-management)
9. [🛠️ Development Tools](#️-development-tools)
10. [🚀 Advanced Development](#-advanced-development)

---

## 🚀 Quick Start

### ⚡ 5-Minute Setup

If you're experienced with Django, here's the quick version:

```bash
# 1. Clone and navigate
git clone <repository-url>
cd drf_boilerplate

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment
echo "DEBUG=True" > .env
echo "SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" >> .env

# 5. Database setup
python manage.py migrate
python manage.py createsuperuser

# 6. Run server
python manage.py runserver

# 🎉 Visit http://127.0.0.1:8000/swagger/
```

---

## 📋 Prerequisites

### 💻 System Requirements

#### **Minimum Requirements**
- **Python**: 3.8 or higher
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM**: 4GB (8GB recommended)
- **Storage**: 2GB free disk space

#### **Recommended Development Setup**
- **Python**: 3.11 (latest stable)
- **RAM**: 16GB or more
- **SSD Storage**: For better performance
- **Multi-core processor**: For faster development

### 🛠️ Required Software

#### **1. Python Installation**

**macOS (using Homebrew):**
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11

# Verify installation
python3 --version
pip3 --version
```

**Windows (using Chocolatey):**
```powershell
# Install Chocolatey (if not already installed)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install Python
choco install python3

# Verify installation
python --version
pip --version
```

**Linux (Ubuntu/Debian):**
```bash
# Update package list
sudo apt update

# Install Python and development tools
sudo apt install python3.11 python3.11-pip python3.11-venv python3.11-dev

# Verify installation
python3.11 --version
pip3 --version
```

#### **2. Git Version Control**

```bash
# macOS
brew install git

# Windows
# Download from https://git-scm.com/download/win

# Linux
sudo apt install git

# Verify installation
git --version
```

#### **3. Database (Optional)**

**PostgreSQL (Recommended for production):**
```bash
# macOS
brew install postgresql
brew services start postgresql

# Windows
# Download from https://www.postgresql.org/download/windows/

# Linux
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

**SQLite (Default for development):**
- Included with Python, no additional installation needed

#### **4. Code Editor (Recommended)**

**Visual Studio Code:**
```bash
# Download from https://code.visualstudio.com/
# Install extensions:
# - Python
# - Django
# - Python Docstring Generator
# - GitLens
# - REST Client
```

**PyCharm (Professional/Community):**
```bash
# Download from https://www.jetbrains.com/pycharm/
# Professional edition has better Django support
```

---

## 🔧 Installation

### 📁 Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/your-username/drf_boilerplate.git
cd drf_boilerplate

# Check the structure
ls -la
```

### 🐍 Step 2: Set Up Virtual Environment

Virtual environments are crucial for Python development as they isolate project dependencies.

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

# Verify activation (should show (venv) in prompt)
which python  # macOS/Linux
where python   # Windows
```

### 📦 Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt

# Install development dependencies (if available)
pip install -r requirements-dev.txt  # Optional

# Verify installation
pip list
```

#### **Understanding Requirements**

**requirements.txt** - Production dependencies:
```
Django==5.2.7
djangorestframework==3.16.1
django-cors-headers==4.5.0
django-filter==25.2
djangorestframework-simplejwt==5.5.1
drf-yasg==1.21.11
python-decouple==3.8
gunicorn==23.0.0
whitenoise==6.11.0
```

**requirements-dev.txt** - Development dependencies (optional):
```
pytest==8.3.3
pytest-django==4.9.0
pytest-cov==6.0.0
black==24.10.0
flake8==7.1.1
isort==5.13.2
django-debug-toolbar==5.0.1
```

### ⚙️ Step 4: Environment Configuration

Create a `.env` file for environment-specific settings:

```bash
# Create environment file
touch .env

# Generate a secret key
python -c "from django.core.management.utils import get_random_secret_key; print(f'SECRET_KEY={get_random_secret_key()}')" >> .env

# Add basic configuration
cat >> .env << EOF

# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings (default uses SQLite)
# DATABASE_URL=sqlite:///db.sqlite3
# For PostgreSQL: postgresql://user:password@localhost/dbname
# For MySQL: mysql://user:password@localhost/dbname

# CORS Settings (for frontend development)
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Email Settings (optional)
# EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EOF
```

### 🗄️ Step 5: Database Setup

```bash
# Run database migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# (Optional) Load initial data if available
# python manage.py loaddata fixtures/initial_data.json
```

### 🏃‍♂️ Step 6: Verify Installation

```bash
# Run Django's built-in checks
python manage.py check

# Start the development server
python manage.py runserver

# Open in browser or test with curl
curl http://127.0.0.1:8000/api/
```

**Expected Output:**
```json
{
    "message": "Welcome to Django REST Framework API",
    "version": "1.0.0",
    "docs": "/swagger/"
}
```

---

## ⚙️ Configuration

### 🌍 Environment Variables

#### **Development Environment (.env)**
```env
# Core Django Settings
DEBUG=True
SECRET_KEY=your-development-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Database Configuration
DATABASE_URL=sqlite:///db.sqlite3

# CORS Configuration
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
CORS_ALLOW_CREDENTIALS=True

# JWT Configuration
JWT_ACCESS_TOKEN_LIFETIME=5
JWT_REFRESH_TOKEN_LIFETIME=1440

# Email Configuration (Development)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Logging Configuration
LOG_LEVEL=DEBUG
```

#### **Production Environment (.env)**
```env
# Core Django Settings
DEBUG=False
SECRET_KEY=your-production-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database Configuration
DATABASE_URL=postgresql://user:password@localhost/dbname

# CORS Configuration
CORS_ALLOWED_ORIGINS=https://yourdomain.com
CORS_ALLOW_CREDENTIALS=True

# Security Settings
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
SECURE_CONTENT_TYPE_NOSNIFF=True
SECURE_BROWSER_XSS_FILTER=True

# Email Configuration (Production)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Logging Configuration
LOG_LEVEL=INFO
```

### 🏛️ Django Settings Configuration

#### **Development Settings (core/settings.py)**
```python
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_filters',
    'drf_yasg',

    # Local apps
    'users',
    'tasks',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

# JWT Configuration
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=config('JWT_ACCESS_TOKEN_LIFETIME', default=5, cast=int)),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=config('JWT_REFRESH_TOKEN_LIFETIME', default=1440, cast=int)),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}

# CORS Configuration
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='').split(',')
CORS_ALLOW_CREDENTIALS = config('CORS_ALLOW_CREDENTIALS', default=False, cast=bool)

# Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': config('LOG_LEVEL', default='INFO'),
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': config('LOG_LEVEL', default='INFO'),
            'propagate': False,
        },
        'users': {
            'handlers': ['console', 'file'],
            'level': config('LOG_LEVEL', default='INFO'),
            'propagate': False,
        },
        'tasks': {
            'handlers': ['console', 'file'],
            'level': config('LOG_LEVEL', default='INFO'),
            'propagate': False,
        },
    },
}

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 🏃‍♂️ Development Workflow

### 🔄 Daily Development Workflow

#### **1. Start Development Server**
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Start development server
python manage.py runserver

# For custom host/port
python manage.py runserver 0.0.0.0:8000
```

#### **2. Database Operations**
```bash
# Create new migrations after model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Check migration status
python manage.py showmigrations

# Show migration SQL
python manage.py sqlmigrate app_name migration_name

# Create superuser (if not exists)
python manage.py createsuperuser
```

#### **3. Development Commands**
```bash
# Start Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Clear cache
python manage.py clear_cache

# Check for issues
python manage.py check

# Validate models
python manage.py validate
```

### 🧪 Testing Workflow

#### **Running Tests**
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test users
python manage.py test tasks

# Run specific test class
python manage.py test tasks.tests.TaskAPITestCase

# Run with coverage (if installed)
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report

# Run tests with verbose output
python manage.py test --verbosity=2

# Run tests with parallel execution (if installed)
pip install parallel-test-runner
python manage.py test --parallel
```

### 📝 Code Quality Tools

#### **Code Formatting (Black)**
```bash
# Install Black
pip install black

# Format code
black .

# Format specific file
black users/views.py

# Check formatting without making changes
black --check .
```

#### **Import Sorting (isort)**
```bash
# Install isort
pip install isort

# Sort imports
isort .

# Sort imports in specific file
isort users/views.py

# Check without making changes
isort --check-only .
```

#### **Linting (flake8)**
```bash
# Install flake8
pip install flake8

# Run linting
flake8 .

# Run linting on specific file
flake8 users/views.py

# Configuration file (.flake8)
[flake8]
max-line-length = 88
exclude = venv,__pycache__,migrations
ignore = E203,W503
```

### 🔧 Git Workflow

#### **Pre-commit Hooks Setup**
```bash
# Install pre-commit
pip install pre-commit

# Create .pre-commit-config.yaml
cat > .pre-commit-config.yaml << EOF
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8
EOF

# Install hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

#### **Git Branching Strategy**
```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "feat: add new feature"

# Push and create pull request
git push origin feature/new-feature

# Merge to main after review
git checkout main
git merge feature/new-feature
git branch -d feature/new-feature
```

---

## 🧪 Testing

### 🏗️ Test Structure

```
tests/
├── test_models.py          # Model tests
├── test_views.py           # View/API tests
├── test_serializers.py     # Serializer tests
├── test_permissions.py     # Permission tests
├── test_utils.py           # Utility function tests
├── factories.py            # Test factories
└── conftest.py             # Test configuration
```

### 📝 Writing Tests

#### **Model Tests**
```python
# tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_task_creation(self):
        """Test creating a task"""
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='Test Description'
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.user, self.user)
        self.assertFalse(task.completed)

    def test_task_str_representation(self):
        """Test task string representation"""
        task = Task.objects.create(
            user=self.user,
            title='Test Task'
        )
        self.assertEqual(str(task), 'Test Task')
```

#### **API Tests**
```python
# tests/test_api.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from tasks.models import Task

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_list_tasks(self):
        """Test listing tasks"""
        Task.objects.create(user=self.user, title='Task 1')
        Task.objects.create(user=self.user, title='Task 2')

        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_create_task(self):
        """Test creating a task"""
        data = {
            'title': 'New Task',
            'description': 'New Description'
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
```

#### **Serializer Tests**
```python
# tests/test_serializers.py
from django.test import TestCase
from users.serializers import UserSerializer
from django.contrib.auth.models import User

class UserSerializerTest(TestCase):
    def test_valid_user_serialization(self):
        """Test serializing valid user data"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        serializer = UserSerializer(user)
        self.assertIn('id', serializer.data)
        self.assertIn('username', serializer.data)

    def test_user_registration_validation(self):
        """Test user registration validation"""
        invalid_data = {
            'username': 'test',  # Too short
            'email': 'invalid-email',  # Invalid email
            'password': '123',  # Too short
            'password_confirm': '456'  # Passwords don't match
        }
        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)
        self.assertIn('email', serializer.errors)
        self.assertIn('password', serializer.errors)
```

### 🎯 Test Fixtures and Factories

#### **Model Factories**
```python
# tests/factories.py
import factory
from django.contrib.auth.models import User
from tasks.models import Task

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')

class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    user = factory.SubFactory(UserFactory)
    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text', max_nb_chars=200)
    completed = factory.Faker('boolean')
```

#### **Using Factories in Tests**
```python
# tests/test_views.py
from django.test import TestCase
from rest_framework.test import APIClient
from tests.factories import UserFactory, TaskFactory

class TaskViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_user_tasks(self):
        """Test that user can only see their own tasks"""
        # Create tasks for different users
        user_tasks = TaskFactory.create_batch(3, user=self.user)
        other_tasks = TaskFactory.create_batch(2)

        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 3)
```

---

## 🔍 Debugging

### 🐛 Django Debug Toolbar

#### **Installation**
```bash
pip install django-debug-toolbar
```

#### **Configuration**
```python
# core/settings.py
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
```

```python
# core/urls.py
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
```

### 🔍 Django Shell

#### **Interactive Debugging**
```bash
# Start Django shell
python manage.py shell

# Example debugging session
>>> from users.models import User
>>> from tasks.models import Task
>>>
>>> # Get user
>>> user = User.objects.get(username='testuser')
>>>
>>> # Create task
>>> task = Task.objects.create(user=user, title='Debug Task')
>>>
>>> # Check task properties
>>> task.title
'Debug Task'
>>> task.user.username
'testuser'
>>>
>>> # Test serializer
>>> from tasks.serializers import TaskSerializer
>>> serializer = TaskSerializer(task)
>>> serializer.data
{'id': 1, 'title': 'Debug Task', ...}
```

#### **Debug Views**
```python
# In your view
from django.http import HttpResponse
import pdb

def debug_view(request):
    pdb.set_trace()  # Debug breakpoint
    # Your code here
    return HttpResponse("Debug point")
```

### 📊 Logging

#### **Advanced Logging Configuration**
```python
# core/settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'format': '{levelname} {asctime} {module} {funcName} {lineno} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs' / 'debug.log',
            'maxBytes': 1024*1024*10,  # 10MB
            'backupCount': 5,
            'formatter': 'detailed',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
```

#### **Using Logging in Code**
```python
import logging

logger = logging.getLogger(__name__)

class TaskViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        logger.info(f"Creating task for user: {request.user.username}")
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            logger.info(f"Task created successfully: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error creating task: {str(e)}")
            raise
```

---

## 📊 Database Management

### 🔄 Database Migrations

#### **Migration Workflow**
```bash
# 1. Make changes to models.py
# 2. Create migration file
python manage.py makemigrations

# 3. Review migration file
python manage.py sqlmigrate app_name migration_name

# 4. Apply migration
python manage.py migrate

# 5. Check migration status
python manage.py showmigrations
```

#### **Advanced Migration Operations**
```python
# Create empty migration for data migrations
python manage.py makemigrations --empty app_name

# Example data migration
# app_name/migrations/0002_populate_data.py
from django.db import migrations

def create_default_tasks(apps, schema_editor):
    Task = apps.get_model('tasks', 'Task')
    User = apps.get_model('auth', 'User')

    default_user = User.objects.first()
    if default_user:
        Task.objects.create(
            user=default_user,
            title='Welcome Task',
            description='This is your first task!'
        )

def reverse_create_default_tasks(apps, schema_editor):
    Task = apps.get_model('tasks', 'Task')
    Task.objects.filter(title='Welcome Task').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_default_tasks,
            reverse_create_default_tasks
        ),
    ]
```

### 🗄️ Database Reset

#### **Reset Development Database**
```bash
# Delete database file (SQLite)
rm db.sqlite3

# Recreate migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

#### **Database Backup and Restore**
```bash
# Backup (PostgreSQL)
pg_dump dbname > backup.sql

# Restore (PostgreSQL)
psql dbname < backup.sql

# Backup (SQLite)
sqlite3 db.sqlite3 ".backup backup.db"

# Restore (SQLite)
cp backup.db db.sqlite3
```

### 🔍 Database Query Optimization

#### **Using Django Debug Toolbar**
- Monitor query count and execution time
- Identify N+1 query problems
- Analyze query performance

#### **Query Optimization Techniques**
```python
# Bad: N+1 queries
tasks = Task.objects.all()
for task in tasks:
    print(task.user.username)  # Separate query for each task

# Good: Using select_related
tasks = Task.objects.select_related('user').all()
for task in tasks:
    print(task.user.username)  # No additional queries

# For reverse relationships
tasks = Task.objects.prefetch_related('comments').all()
```

---

## 🛠️ Development Tools

### 🔧 VS Code Configuration

#### **.vscode/settings.json**
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.sortImports.args": ["--profile", "black"],
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        ".pytest_cache": true,
        ".coverage": true,
        "htmlcov": true
    }
}
```

#### **.vscode/launch.json**
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["runserver", "--noreload"],
            "django": true,
            "justMyCode": false
        },
        {
            "name": "Python: Django Test",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["test"],
            "django": true,
            "justMyCode": false
        }
    ]
}
```

### 📝 API Testing

#### **REST Client for VS Code**
```http
# test-api.http
### User Registration
POST http://127.0.0.1:8000/api/auth/register/
Content-Type: application/json

{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "password_confirm": "testpass123"
}

### User Login
POST http://127.0.0.1:8000/api/auth/login/
Content-Type: application/json

{
    "username": "testuser",
    "password": "testpass123"
}

### Get Tasks (Authorization header will be auto-populated from login response)
GET http://127.0.0.1:8000/api/tasks/
Authorization: Bearer {{login.response.body.access}}

### Create Task
POST http://127.0.0.1:8000/api/tasks/
Authorization: Bearer {{login.response.body.access}}
Content-Type: application/json

{
    "title": "Test Task",
    "description": "Created via API"
}
```

#### **curl Commands**
```bash
# User Registration
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "password_confirm": "testpass123"
  }'

# Get JWT Token
TOKEN=$(curl -s -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}' \
  | jq -r '.access')

# Use Token for API Requests
curl -X GET http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Bearer $TOKEN"
```

### 🐳 Docker Development

#### **Dockerfile for Development**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create logs directory
RUN mkdir -p logs

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### **docker-compose.yml**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=True
      - DATABASE_URL=postgresql://postgres:password@db:5432/dbname
    depends_on:
      - db
    command: python manage.py runserver 0.0.0.0:8000

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=dbname
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

---

## 🚀 Advanced Development

### 🔧 Performance Monitoring

#### **Django Silk (Silk Profiler)**
```bash
pip install django-silk
```

```python
# core/settings.py
MIDDLEWARE = [
    'silk.middleware.SilkyMiddleware',
    # ... other middleware
]

INSTALLED_APPS += ['silk']

SILKY_PYTHON_PROFILER = True
```

#### **Database Query Analysis**
```python
from django.db import connection
from django.conf import settings

def debug_queries(view_func):
    def wrapper(request, *args, **kwargs):
        if settings.DEBUG:
            from django.db import reset_queries
            reset_queries()

        response = view_func(request, *args, **kwargs)

        if settings.DEBUG:
            queries = len(connection.queries)
            print(f"Number of queries: {queries}")
            for query in connection.queries:
                print(f"{query['time']}: {query['sql']}")

        return response
    return wrapper
```

### 🔧 Custom Management Commands

#### **Create Custom Command**
```bash
python manage.py create_command users commands create_sample_data
```

```python
# users/management/commands/create_sample_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task
from faker import Faker

class Command(BaseCommand):
    help = 'Create sample data for testing'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10, help='Number of users to create')
        parser.add_argument('--tasks', type=int, default=5, help='Tasks per user')

    def handle(self, *args, **options):
        fake = Faker()

        # Create users
        for i in range(options['users']):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )

            # Create tasks for each user
            for j in range(options['tasks']):
                Task.objects.create(
                    user=user,
                    title=fake.sentence(nb_words=4),
                    description=fake.text(max_nb_chars=200),
                    completed=fake.boolean()
                )

        self.stdout.write(
            self.style.SUCCESS(f'Created {options["users"]} users with {options["tasks"]} tasks each')
        )
```

### 🔧 Automated Testing with CI/CD

#### **GitHub Actions (.github/workflows/ci.yml)**
```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10, 3.11]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-django pytest-cov

    - name: Run tests
      run: |
        pytest --cov=users --cov=tasks --cov-report=xml

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella
```

---

## 🎉 Summary

This comprehensive setup and development guide covers everything you need to get started with Django REST Framework development:

### ✅ What We've Covered

- **🚀 Quick Start**: Fast setup for experienced developers
- **📋 Prerequisites**: System requirements and software installation
- **🔧 Installation**: Step-by-step setup process
- **⚙️ Configuration**: Environment and Django settings
- **🏃‍♂️ Development Workflow**: Daily development routines
- **🧪 Testing**: Comprehensive testing strategies
- **🔍 Debugging**: Tools and techniques for debugging
- **📊 Database Management**: Migrations, optimization, and maintenance
- **🛠️ Development Tools**: IDE setup, API testing, Docker
- **🚀 Advanced Development**: Performance monitoring, CI/CD

### 🎯 Best Practices

1. **Use Virtual Environments**: Always isolate project dependencies
2. **Version Control**: Commit frequently with meaningful messages
3. **Test-Driven Development**: Write tests before implementing features
4. **Code Quality**: Use formatters, linters, and pre-commit hooks
5. **Documentation**: Document your code and API endpoints
6. **Security**: Never commit secrets or sensitive data
7. **Performance**: Monitor and optimize database queries
8. **Backup**: Regularly backup your database and important files

### 🚀 Next Steps

1. **Read the Full Documentation**: Explore other guides in this documentation
2. **Start Building**: Begin implementing your features
3. **Join the Community**: Participate in Django and DRF communities
4. **Stay Updated**: Keep your dependencies and knowledge current

Happy coding! 🎉

---

## 🆘 Troubleshooting

### 🔧 Common Issues

#### **Virtual Environment Issues**
```bash
# If virtual environment doesn't activate
# macOS/Linux
export PATH="/usr/local/bin:$PATH"
source venv/bin/activate

# Windows
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

#### **Database Migration Errors**
```bash
# If migrations fail
python manage.py migrate --fake-initial
python manage.py migrate --fake

# Reset migrations (last resort)
rm */migrations/0*.py
python manage.py makemigrations
python manage.py migrate
```

#### **Port Already in Use**
```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

If you encounter any issues not covered here, please check the official Django and Django REST Framework documentation or open an issue in the project repository.