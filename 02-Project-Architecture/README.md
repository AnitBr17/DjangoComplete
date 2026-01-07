# 🚀 Django Setup & Run Guide

This guide explains how to install **Django**, verify the installation, create a project, and start the Django development server using command-line instructions.

---

## 📌 Prerequisites

* Python installed on your system
* Basic knowledge of command line / terminal

---

## 🧩 Step 1: Check Python Installation

Make sure Python is installed on your system.

```bash
python --version
```

or

```bash
python3 --version
```

---

## 🔄 Step 2: Upgrade pip (Recommended)

```bash
python -m pip install --upgrade pip
```

---

## 📦 Step 3: Install Django

Install Django using pip.

```bash
pip install django
```

---

## ✅ Step 4: Verify Django Installation

Check whether Django is installed correctly.

```bash
django-admin --version
```

---

## 🏗️ Step 5: Create a Django Project

Create a new Django project named **myProject**.

```bash
django-admin startproject myProject
```

---

## 📁 Step 6: Navigate to Project Directory

Move into the project folder.

```bash
cd myProject
```

---

## ▶️ Step 7: Run Django Development Server

Start the Django development server.

```bash
python manage.py runserver
```

---

## 🌐 Step 8: Open in Browser

After running the server, open the following URL in your browser:

```
http://127.0.0.1:8000/
```

You should see the **Django welcome page**, confirming the setup is successful 🎉

---

## 🧾 Summary of Commands Used

```bash
python --version
python -m pip install --upgrade pip
pip install django
django-admin --version
django-admin startproject myProject
cd myProject
python manage.py runserver
```

---

## 🎯 Conclusion

You have successfully:

* ✅ Installed Django
* ✅ Verified the Django version
* ✅ Created a Django project
* ✅ Started the development server

You are now ready to build Django applications 🚀✨
