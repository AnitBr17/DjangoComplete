# 📂 Django Template Folder Setup (Project & App Level)

This guide explains **what Django templates are**, the **types of template setups**, and how to configure templates correctly using both **Project-level** and **App-level** approaches.

---

## 🔹 What is a Template in Django?

A **template** is an HTML file used to display **dynamic data** in a Django web application.

Django templates allow you to:

* Display data sent from views
* Use template logic (`if`, `for`, etc.)
* Reuse common UI components (navbar, footer, layouts)

---

## 🔹 Types of Templates in Django

Django supports **two template setup approaches**:

1. **Project-Level Template (Centralized)**
2. **App-Level Template (Modular – Recommended)**

---

## 1️⃣ Project-Level Template (Centralized)

👉 All templates are stored in **one common folder** for the entire project.

### ✅ When to Use?

* Small projects
* Single-page applications
* Beginner-level projects

---

### 📁 Folder Structure (Project Level)

```
myproject/
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   └── home.html
│
└── manage.py
```

---

### ⚙️ Project-Level Template Setup

#### 1️⃣ Import `os` in `settings.py`

```python
import os
```

---

#### 2️⃣ Update `TEMPLATES` in `settings.py`

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

#### 3️⃣ Create a View (`views.py`)

```python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```

---

#### 4️⃣ Configure URLs (`urls.py`)

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
```

---

#### 5️⃣ Create HTML File

**Path:**

```
myproject/templates/home.html
```

**Code:**

```html
<h1>Welcome to Django Project-Level Template</h1>
```

---

## 2️⃣ App-Level Template (Recommended)

👉 Each app manages **its own templates**, making the project more modular and scalable.

---

### ✅ When to Use?

* Large projects
* Multiple apps
* Industry-standard applications

---

### 📁 Folder Structure (App Level)

```
myproject/
│
├── blog/
│   ├── templates/
│   │   └── blog/
│   │       └── post_list.html
│   └── views.py
│
├── shop/
│   ├── templates/
│   │   └── shop/
│   │       └── product_list.html
│   └── views.py
│
├── myproject/
│   ├── settings.py
│   └── urls.py
│
└── manage.py
```

---

### ⚙️ App-Level Template Setup

#### 1️⃣ Create Project & Apps

```bash
django-admin startproject myproject
cd myproject
python manage.py startapp blog
python manage.py startapp shop
```

---

#### 2️⃣ Register Apps in `settings.py`

```python
INSTALLED_APPS = [
    ...
    'blog',
    'shop',
]
```

---

#### 3️⃣ Use Templates DIR (Optional but Safe)

```python
'DIRS': [BASE_DIR / 'templates'],
```

---

#### 4️⃣ Create HTML Files

📄 **blog/templates/blog/post_list.html**

```html
<h1>Blog Post List</h1>
```

📄 **shop/templates/shop/product_list.html**

```html
<h1>Product List</h1>
```

---

#### 5️⃣ Render Templates in Views

📄 **blog/views.py**

```python
from django.shortcuts import render

def post_list(request):
    return render(request, "blog/post_list.html")
```

📄 **shop/views.py**

```python
from django.shortcuts import render

def product_list(request):
    return render(request, "shop/product_list.html")
```

---

## 🧠 Key Difference (Quick Comparison)

| Feature           | Project-Level  | App-Level      |
| ----------------- | -------------- | -------------- |
| Template Folder   | Single         | Multiple       |
| Best For          | Small projects | Large projects |
| Reusability       | Low            | High           |
| Scalability       | Limited        | Excellent      |
| Industry Standard | ❌              | ✅              |

---

## 📝 Summary

* Django supports **project-level** and **app-level** templates
* Project-level is simple but not scalable
* App-level templates are modular and reusable
* App-level setup is **recommended for real-world projects**

---

## 🎯 Conclusion

Choosing the correct template structure is critical for **clean architecture and scalability**.
For professional and production-ready Django applications, **App-Level Templates are the best practice** 🚀

