# Authentication and Permissions 🔐

In this comprehensive guide, we'll explore the authentication and authorization system in our Django REST Framework application. Security is paramount when building APIs, and understanding how to properly implement authentication and permissions is crucial for protecting your application and user data.

## 📚 Table of Contents

1. [🏗️ Overview](#️-overview)
2. [🔐 Authentication System](#-authentication-system)
3. [🎫 JWT (JSON Web Tokens)](#-jwt-json-web-tokens)
4. [👥 User Registration](#-user-registration)
5. [🔑 Login and Token Management](#-login-and-token-management)
6. [🛡️ Permission Classes](#️-permission-classes)
7. [🎯 Custom Permissions](#-custom-permissions)
8. [🔒 Security Best Practices](#-security-best-practices)
9. [🧪 Testing Authentication](#-testing-authentication)
10. [🚀 Advanced Authentication](#-advanced-authentication)

---

## 🏗️ Overview

### 🎯 Authentication vs Authorization

**Authentication (Who are you?)**: The process of verifying who a user is.

**Authorization (What can you do?)**: The process of determining what an authenticated user is allowed to do.

### 🏛️ Our Security Architecture

```mermaid
graph TD
    A[Client Request] --> B[Authentication Middleware]
    B --> C{Valid JWT Token?}
    C -->|No| D[401 Unauthorized]
    C -->|Yes| E[Permission Classes]
    E --> F{Has Permission?}
    F -->|No| G[403 Forbidden]
    F -->|Yes| H[Process Request]
    H --> I[Response]
```

### 🔐 Security Layers in Our Application

1. **JWT Authentication**: Stateless token-based authentication
2. **Permission Classes**: Object-level and view-level permissions
3. **User Isolation**: Users can only access their own data
4. **CORS Protection**: Cross-origin request security
5. **Input Validation**: Data validation through serializers
6. **Security Headers**: Built-in Django security middleware

---

## 🔐 Authentication System

### 🎫 JWT (JSON Web Token) Authentication

We use **Simple JWT** for token-based authentication. JWT provides a secure, stateless way to authenticate users across requests.

#### **How JWT Works**

```mermaid
sequenceDiagram
    participant Client
    participant API
    participant JWT Service

    Client->>API: POST /api/auth/login/ (credentials)
    API->>JWT Service: Generate tokens
    JWT Service-->>API: Access + Refresh tokens
    API-->>Client: Return tokens

    Client->>API: GET /api/tasks/ (with Access Token)
    API->>JWT Service: Validate token
    JWT Service-->>API: Token valid
    API-->>Client: Protected data

    Note over Client,API: Access Token expires
    Client->>API: POST /api/auth/token/refresh/ (Refresh Token)
    API->>JWT Service: Generate new Access Token
    JWT Service-->>API: New Access Token
    API-->>Client: New Access Token
```

#### **JWT Configuration**

```python
# core/settings.py
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}
```

### 🔧 JWT Token Structure

A JWT token consists of three parts separated by dots:

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyMjI0NjAwLCJqdGkiOiJlNz... (signature)
```

1. **Header** (Algorithm and token type)
2. **Payload** (Claims: user data, expiration, etc.)
3. **Signature** (Cryptographic signature)

#### **JWT Payload Example**

```json
{
    "token_type": "access",
    "exp": 1642224600,
    "jti": "e7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2",
    "user_id": 1,
    "username": "john_doe"
}
```

---

## 👥 User Registration

### 📝 Registration View Implementation

```python
# users/views.py
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    """
    View for user registration.
    Creates a new user account and returns user data.
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]  # No authentication required
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Return user data without password
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'date_joined': user.date_joined
        }, status=status.HTTP_201_CREATED)
```

### 📋 Registration Serializer

```python
# users/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration and profile data.
    """
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirm', 'date_joined')
        read_only_fields = ('id', 'date_joined')

    def validate_email(self, value):
        """
        Validate that email is unique and properly formatted.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, data):
        """
        Validate that passwords match.
        """
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        """
        Create user with hashed password.
        """
        # Remove password_confirm as it's not needed for user creation
        validated_data.pop('password_confirm')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
```

### 🧪 Registration Process

#### **Step 1: Client sends registration data**

```json
POST /api/auth/register/
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password123",
    "password_confirm": "secure_password123"
}
```

#### **Step 2: Server validates and creates user**

```python
# Validation checks performed:
# 1. Username uniqueness
# 2. Email uniqueness and format
# 3. Password complexity (min_length=8)
# 4. Password confirmation match
# 5. Required fields present
```

#### **Step 3: Server returns user data**

```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "date_joined": "2024-01-15T10:30:00.123456Z"
}
```

---

## 🔑 Login and Token Management

### 🔑 JWT Login View

We use Django REST Framework Simple JWT's built-in `TokenObtainPairView`:

```python
# users/urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### 🔐 Custom Token Claims (Optional)

You can customize JWT token claims to include additional user data:

```python
# users/jwt_serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom JWT serializer that includes additional user data in token.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        token['user_id'] = user.id

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom response data
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'is_staff': self.user.is_staff,
        }

        return data
```

### 🔄 Token Refresh Process

#### **Access Token Expiration**

Access tokens are short-lived (5 minutes by default) for security:

```bash
# When access token expires:
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Bearer EXPIRED_ACCESS_TOKEN"

# Response:
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid"
}
```

#### **Refresh Token Usage**

```bash
# Use refresh token to get new access token:
curl -X POST http://127.0.0.1:8000/api/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }'

# Response:
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 🚪 Logout Implementation

Since JWT is stateless, we implement token blacklisting for logout:

```python
# users/views.py
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class LogoutView(APIView):
    """
    Logout view that blacklists the refresh token.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

            return Response(
                {"message": "Successfully logged out"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": "Invalid token"},
                status=status.HTTP_400_BAD_REQUEST
            )
```

---

## 🛡️ Permission Classes

### 🎯 Built-in Permission Classes

Django REST Framework provides several built-in permission classes:

#### **1. IsAuthenticated**

```python
from rest_framework import permissions

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
```

*Requires user to be authenticated.*

#### **2. IsAdminUser**

```python
class AdminOnlyView(APIView):
    permission_classes = [permissions.IsAdminUser]
```

*Requires user to be staff and authenticated.*

#### **3. IsAuthenticatedOrReadOnly**

```python
class PublicTaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

*Authenticated users have full access, unauthenticated users have read-only access.*

#### **4. AllowAny**

```python
class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
```

*Allows any user, authenticated or not.*

### 🏛️ Global Permission Configuration

You can set default permissions globally:

```python
# core/settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

### 🎯 View-level vs Object-level Permissions

#### **View-level Permissions** (`has_permission`)

Called before the view is executed:

```python
class IsOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # This is called for every request
        return request.user.is_authenticated
```

#### **Object-level Permissions** (`has_object_permission`)

Called after the object is retrieved (for retrieve, update, delete):

```python
class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # This is called only for object-level operations
        return obj.user == request.user
```

---

## 🎯 Custom Permissions

### 🔒 IsOwnerPermission Implementation

Our custom permission class ensures users can only access their own tasks:

```python
# tasks/permissions.py
from rest_framework import permissions

class IsOwnerPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Read-only access is allowed for any authenticated user.
    """

    def has_permission(self, request, view):
        """
        Return True if the request should be permitted.
        This runs before checking object permissions.
        """
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Return True if the request should be permitted for the given object.
        This runs after has_permission passes.
        """
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the task
        return obj.user == request.user
```

### 🛡️ Permission Usage in Views

```python
# tasks/views.py
from rest_framework import viewsets, permissions
from .permissions import IsOwnerPermission

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing tasks with owner-based permissions.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        permissions.IsAuthenticated,  # Must be logged in
        IsOwnerPermission             # Must own the resource
    ]
```

### 🎯 Multiple Permission Classes

Permissions are evaluated in order. All must pass:

```python
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,  # 1st check: User must be authenticated
        IsOwnerPermission,           # 2nd check: User must own the object
    ]
```

### 📝 Permission Flow Diagram

```mermaid
graph TD
    A[Request] --> B{IsAuthenticated?}
    B -->|No| C[401 Unauthorized]
    B -->|Yes| D{Method in SAFE_METHODS?}
    D -->|Yes| E[Allow Read Access]
    D -->|No| F{User owns object?}
    F -->|No| G[403 Forbidden]
    F -->|Yes| H[Allow Write Access]
```

### 🔧 Advanced Custom Permissions

#### **Time-based Permissions**

```python
class IsOwnerOrReadOnlyDuringBusinessHours(permissions.BasePermission):
    """
    Allow owners to edit anytime, others read-only during business hours.
    """

    def has_object_permission(self, request, view, obj):
        # Owners can always edit
        if obj.user == request.user:
            return True

        # Others can only read during business hours (9 AM - 5 PM)
        from datetime import datetime
        now = datetime.now()
        if 9 <= now.hour < 17 and request.method in permissions.SAFE_METHODS:
            return True

        return False
```

#### **Role-based Permissions**

```python
class IsAdminOrOwner(permissions.BasePermission):
    """
    Allow admin users or owners to access.
    """

    def has_object_permission(self, request, view, obj):
        # Admin users can access any object
        if request.user.is_staff:
            return True

        # Owners can access their own objects
        return obj.user == request.user
```

---

## 🔒 Security Best Practices

### 🛡️ JWT Security

#### **1. Token Lifetime Management**

```python
# Short-lived access tokens for security
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,  # Issue new refresh token on refresh
    'BLACKLIST_AFTER_ROTATION': True,  # Blacklist old refresh token
}
```

#### **2. Secure Token Storage**

**Client-side:**
- Store tokens in `localStorage` or `sessionStorage`
- Consider using secure, httpOnly cookies for additional security
- Implement automatic token refresh before expiration

**Server-side:**
- Use strong signing keys
- Implement token blacklisting for logout
- Monitor for suspicious token usage

### 🔐 Password Security

#### **1. Password Hashing**

Django automatically hashes passwords using PBKDF2:

```python
# Django automatically handles password hashing
user = User.objects.create_user(
    username='john_doe',
    password='plaintext_password'  # This gets hashed automatically
)
```

#### **2. Password Validation**

Configure password validators in settings:

```python
# core/settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```

### 🔒 CORS and Headers

#### **CORS Configuration**

```python
# core/settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React development server
    "http://127.0.0.1:3000",
]

# For production, use more restrictive settings
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://yourdomain\.com$",
]
```

#### **Security Headers**

Django provides built-in security headers:

```python
# core/settings.py
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000  # In production with HTTPS
```

### 🔍 Rate Limiting

Implement rate limiting to prevent abuse:

```python
# Install django-ratelimit
pip install django-ratelimit

# views.py
from django_ratelimit.decorators import ratelimit

class LoginView(APIView):
    @ratelimit(key='ip', rate='5/m', block=True)
    def post(self, request):
        # Login logic
        pass
```

---

## 🧪 Testing Authentication

### 🧪 Authentication Testing Setup

```python
# users/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'password_confirm': 'testpass123'
        }

    def test_user_registration(self):
        """Test user registration endpoint."""
        response = self.client.post('/api/auth/register/', self.user_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(response.data['username'], 'testuser')

        # Verify user was created in database
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_login(self):
        """Test user login endpoint."""
        # First, register a user
        User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Then login
        login_data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post('/api/auth/login/', login_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_protected_endpoint_without_token(self):
        """Test accessing protected endpoint without token."""
        response = self.client.get('/api/tasks/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_protected_endpoint_with_token(self):
        """Test accessing protected endpoint with valid token."""
        # Create and login user
        user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Get token
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        token = response.data['access']

        # Access protected endpoint
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get('/api/tasks/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_refresh(self):
        """Test token refresh endpoint."""
        # Create and login user
        user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Get tokens
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        refresh_token = response.data['refresh']

        # Refresh token
        response = self.client.post('/api/auth/token/refresh/', {
            'refresh': refresh_token
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
```

### 🧪 Permission Testing

```python
# tasks/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class PermissionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create two users
        self.user1 = User.objects.create_user(
            username='user1',
            password='pass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='pass123'
        )

        # Create task for user1
        self.task1 = Task.objects.create(
            user=self.user1,
            title='User 1 Task'
        )

        # Create task for user2
        self.task2 = Task.objects.create(
            user=self.user2,
            title='User 2 Task'
        )

    def test_user_can_access_own_task(self):
        """Test that user can access their own tasks."""
        # Login as user1
        self.client.force_authenticate(user=self.user1)

        # Access own task
        response = self.client.get(f'/api/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_access_others_task(self):
        """Test that user cannot access other users' tasks."""
        # Login as user1
        self.client.force_authenticate(user=self.user1)

        # Try to access user2's task
        response = self.client.get(f'/api/tasks/{self.task2.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_task(self):
        """Test that user can update their own tasks."""
        # Login as user1
        self.client.force_authenticate(user=self.user1)

        # Update own task
        response = self.client.patch(f'/api/tasks/{self.task1.id}/', {
            'title': 'Updated Title'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_others_task(self):
        """Test that user cannot update other users' tasks."""
        # Login as user1
        self.client.force_authenticate(user=self.user1)

        # Try to update user2's task
        response = self.client.patch(f'/api/tasks/{self.task2.id}/', {
            'title': 'Updated Title'
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
```

---

## 🚀 Advanced Authentication

### 🔐 Social Authentication

Implement OAuth2 social authentication:

```python
# Install required packages
pip install social-auth-app-django

# settings.py
INSTALLED_APPS = [
    # ...
    'social_django',
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

# Google OAuth2 settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-google-client-id'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-google-client-secret'
```

### 📱 API Key Authentication

For service-to-service communication:

```python
# api_auth/authentication.py
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIKey

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-Key')
        if not api_key:
            return None

        try:
            key = APIKey.objects.get(key=api_key, is_active=True)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API key')

        return (key.user, None)
```

### 🔄 Two-Factor Authentication (2FA)

Implement TOTP-based 2FA:

```python
# Install required packages
pip install django-otp

# settings.py
INSTALLED_APPS = [
    # ...
    'django_otp',
    'django_otp.plugins.otp_totp',
]

# views.py
import pyotp
from django_otp.util import random_hex
from rest_framework.views import APIView
from rest_framework.response import Response

class Setup2FAView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Generate secret key
        secret = pyotp.random_base32()

        # Save secret to user profile
        request.user.profile.totp_secret = secret
        request.user.profile.save()

        # Generate QR code URL
        totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(
            name=request.user.email,
            issuer_name="Your App"
        )

        return Response({
            'secret': secret,
            'qr_code_url': totp_uri
        })
```

### 🔐 Role-Based Access Control (RBAC)

Implement roles and permissions:

```python
# models.py
from django.contrib.auth.models import User
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField('Permission')

class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    codename = models.CharField(max_length=100, unique=True)

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'role']

# permissions.py
class HasRolePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        required_permission = getattr(view, 'required_permission', None)
        if not required_permission:
            return True

        return request.user.userrole_set.filter(
            role__permissions__codename=required_permission
        ).exists()

# views.py
@permission_classes([HasRolePermission])
@method_decorator(name='required_permission', 'delete_tasks')
class TaskViewSet(viewsets.ModelViewSet):
    # ViewSet implementation
    pass
```

---

## 🎉 Summary

In this comprehensive guide, we've covered:

- **🔐 Authentication System**: JWT-based stateless authentication
- **👥 User Registration**: Secure user account creation
- **🔑 Token Management**: Login, refresh, and logout processes
- **🛡️ Permission Classes**: View-level and object-level permissions
- **🎯 Custom Permissions**: Tailored authorization logic
- **🔒 Security Best Practices**: Token security, password policies, CORS
- **🧪 Testing**: Comprehensive authentication and permission testing
- **🚀 Advanced Features**: Social auth, API keys, 2FA, RBAC

### 🎯 Key Takeaways

1. **Defense in Depth**: Use multiple layers of security
2. **Principle of Least Privilege**: Users should only have access they need
3. **Token Security**: Keep access tokens short-lived and refresh tokens secure
4. **Comprehensive Testing**: Test all authentication and permission scenarios
5. **Monitor and Log**: Track authentication attempts and security events

### 🚀 Next Steps

1. **Implement Rate Limiting**: Protect against brute force attacks
2. **Add Audit Logging**: Track who accessed what and when
3. **Implement Password Policies**: Enforce strong password requirements
4. **Add Security Headers**: Implement additional security measures
5. **Regular Security Reviews**: Periodically review and update security measures

This authentication and authorization system provides a robust, secure foundation for your Django REST API that you can extend and customize based on your specific security requirements.