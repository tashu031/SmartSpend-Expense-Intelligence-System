# Smart Expense Intelligence System

## Project Overview

Smart Expense Intelligence System is a Python and SQL Server based personal finance management application. The system helps users track their income and expenses, analyze spending patterns, monitor budgets, and generate financial summaries.

The project is developed as part of an internship program to demonstrate the integration of Python programming with SQL Server database management.

---

## Technologies Used

* Python 
* SQL Server
* pyodbc
* Git & GitHub
* VS Code

---

## Features

### User Management

* User Registration
* User Login & Logout
* Session Management
* Duplicate Email & Email Format Validation
* Password Length Validation

### Income Management

* Add Income
* Update Income
* Delete Income
* View Income History

### Expense Management

* Add Expense
* Update Expense
* delete Expense
* View Expense History

### Financial Analytics

* Monthly Financial Summary
* Savings Calculation
* Savings Percentage Analysis
* Financial Health Status
* Expense Category Analysis
* Top Spending Category Identification
* Budget Monitoring & Alerts

### Input Validation

* Email Validation
* Password Length Validation
* Empty Field Validation
* Positive Amount Validation
* Login Authentication

---

## Database Design

The project uses three main tables:

### Users

Stores user account information.

| Column   | Description   |
| -------- | ------------- |
| user_id  | Primary Key   |
| name     | User Name     |
| email    | User Email    |
| password | User Password |

### Income

Stores user income records.

| Column      | Description   |
| ----------- | ------------- |
| income_id   | Primary Key   |
| user_id     | Foreign Key   |
| amount      | Income Amount |
| source      | Income Source |
| income_date | Income Date   |

### Expense

Stores user expense records.

| Column       | Description         |
| ------------ | ------------------- |
| expense_id   | Primary Key         |
| user_id      | Foreign Key         |
| amount       | Expense Amount      |
| category     | Expense Category    |
| description  | Expense Description |
| expense_date | Expense Date        |

---

## Project Workflow

1. User registers an account.
2. User logs into the system.
3. User can add, update, and delete income records.
4. User can add, update, and delete expense records.
5. User views financial reports and analytics.
6. System generates summaries and budget insights.
7. User can logout securely.

---

## How to Run the Project

1. Clone the repository.
2. Create the database in SQL Server.
3. Execute the table creation SQL scripts.
4. Install required dependency:

```bash
pip install pyodbc
```

5. Update database connection settings in `database.py`.
6. Run the application:

```bash
python main.py
```

---

## Future Enhancements

* Password Encryption
* Export Reports to PDF/Excel
* Graphical Dashboard
* Data Visualization Charts

---

## Author

Tashu Gupta

Smart Expense Intelligence System

