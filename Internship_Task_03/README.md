# Inventory Management System – OOP Models

## 1. Project Overview

The Inventory Management System is a Python-based application developed as part of Task 3 of the Python Developer Internship.

It demonstrates object-oriented programming concepts by managing different types of products using classes, inheritance, encapsulation, and polymorphism-related method overriding.

## 2. Objective

The main objective is to design reusable object-oriented data models that manage mock inventory records while validating product information through property setters.

## 3. Technologies Used

- Python 3.11.9
- Visual Studio Code
- Pytest
- Python Object-Oriented Programming

## 4. OOP Concepts Implemented

- **Classes and Objects:** Represent products and inventory.
- **Inheritance:** Electronics and Clothing inherit from Product.
- **Encapsulation:** Private attributes protect product data.
- **Property Setters:** Validate product information.
- **Method Overriding:** Child classes provide their own string and representation methods.
- **Magic Methods:** `__str__()` and `__repr__()` provide readable object representations.

## 5. Project Structure

```text
Internship_Task_03/
├── data/
├── screenshots/
├── src/
│   └── inventory/
│       ├── __init__.py
│       └── models.py
├── tests/
│   └── test_models.py
├── main.py
└── README.md
```

## 6. How to Run

Execute the application from the project directory:

```powershell
python main.py
```

## 7. How to Run Tests

Execute:

```powershell
python -m pytest tests/test_models.py -v
```

## 8. Testing Results

All 14 automated test cases passed successfully.

## 9. Conclusion

This project demonstrates practical implementation of object-oriented programming concepts using Python to build reusable and validated inventory data models.