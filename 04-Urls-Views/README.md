# 🔗 Views & URLs Basics in Django

This guide explains the **basics of Django Views and URL routing**, including how to create a simple view, configure URLs at the project level, and display output in the browser.

---

## 📚 Topics Covered

* Introduction to Views & URLs
* Creating a Simple Function-Based View
* Configuring URLs at Project Level
* Registering an App
* Final Output

---

## 📖 What is a View?

A **View** in Django is responsible for handling a web request and returning a web response.

* A view can be **function-based** or **class-based**
* It receives an HTTP request
* It returns an HTTP response (HTML, text, JSON, etc.)

---

## 🏗️ Step 1: Create a Django Project

Create a new Django project named `URL_Views`.

```bash
django-admin startproject URL_Views
```

---

## 📦 Step 2: Create an App

Navigate into the project folder and create an app named `blog`.

```bash
cd URL_Views
python manage.py startapp blog
```

---

## ✍️ Step 3: Create a Function-Based View

Open the following file:

```
blog/views.py
```

Add a simple view with the required import:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi Welcome to my blog home page")
```

---

## 🔀 Step 4: Configure URLs (Project Level)

Open the project’s `urls.py` file:

```
URL_Views/urls.py
```

Import the view and create URL routes:

```python
from django.contrib import admin
from django.urls import path
from blog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', home, name="home"),
]
```

---

## ⚙️ Step 5: Register App in Settings

Open the settings file:

```
URL_Views/settings.py
```

Add your app inside `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',
]
```

---

## ▶️ Run the Development Server

```bash
python manage.py runserver
```

---

## 🌐 Final Output

Open your browser and visit:

```
http://127.0.0.1:8000/blog/
```

### ✅ Output Displayed

```
Hi Welcome to my blog home page
```

---

## 📝 Summary

* Created a Django project and app
* Built a simple function-based view
* Connected the view using URL routing
* Registered the app in settings
* Successfully displayed output in the browser

---

## 🎯 Conclusion

Understanding **Views and URLs** is the foundation of Django development.
They control **how requests are handled** and **what responses are sent**, forming the backbone of every Django application 🚀

