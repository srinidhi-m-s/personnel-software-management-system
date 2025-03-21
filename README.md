# HRMS - Human Resource Management System

## 📌 Project Description
This is a **Human Resource Management System (HRMS)** built using **Django**. It includes features like employee management, payroll management, and leave requests. The system allows admins to manage employees.

---

## 🚀 Features
### ✅ **Employee Management**
- Add, edit, and delete employees
- Store employee details 

### ✅ **Payroll Management**
- Admins can add payroll details for employees
- Employees can view the payroll

### ✅ **Leave Management**
- Employees can request leaves
- Admins can **approve/reject** leave requests

---

## 📂 **Installation**
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/srinidhi-m-s/personnel-software-management-system.git
cd hrms
```

### 2️⃣ Create a Virtual Environment(optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install django
```bash
pip install django
```

### 4️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Server
```bash
python manage.py runserver
```

Now, visit **`http://127.0.0.1:8000/admin/`** to log in as an admin.

---

## 🎮 **Usage**
- **Employees:** Can check in/out, request leaves.
- **Admin Panel (`/admin/`):** Manage employees, attendance, payroll, and leave requests.
- **Payroll Page (`/payroll/`):** View employee salary details.

---

## 🔥 **Future Improvements**
- Login authentication for employees
- Generate **Payroll Slips automatically**
- **Attendance tracking**
- Add **Automated Leave Balance Calculation**

---

## 🛠️ **Tech Stack**
- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap
---


