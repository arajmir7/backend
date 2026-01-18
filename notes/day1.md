# Day 1 – Variables & Control Flow

## Date

18-01-2026

## Focus of the Day

* Python variables
* Basic control flow
* Input/output handling
* Error handling with try/except
* Simple file persistence using CSV

---

## What I Learned Today

### 1. Variables in Python

* Variables store data values and are dynamically typed.
* Common data types used today:

  * `int`
  * `float`
  * `str`

Example:

```python
price = float(input())
gst_rate = float(input())
```

---

### 2. Control Flow

* Used `if` conditions to validate inputs.
* Prevented negative values for price and GST rate.

Example:

```python
if price < 0 or gst_rate < 0:
    print("Values must be non-negative")
```

---

### 3. Error Handling

* Used `try/except` to handle invalid (non-numeric) inputs.
* Prevents program crash and improves user experience.

Example:

```python
try:
    price = float(input())
except ValueError:
    print("Invalid input")
```

---

### 4. File Handling with CSV

* Learned how to:

  * Create a CSV file if it doesn’t exist
  * Append new records
  * Read and display previous records (history)

Key functions used:

* `open()`
* `csv.writer`
* `csv.reader`
* `os.path.exists()`

---

## Project Built Today

### GST Calculator (CLI Tool)

**Features:**

* Accepts product price and GST rate
* Calculates GST amount and final price
* Saves each calculation to a CSV file
* Displays calculation history on startup
* Handles invalid inputs gracefully

---

## Problems Faced

* Initially forgot to print output in HackerRank problems
* Understood that platforms require **exact output format**
* Learned the difference between local execution and platform submission

---

## Key Takeaway

> Writing small but complete programs builds confidence faster than watching tutorials.

Consistency beats intensity.

---

## Status

✅ Day 1 completed
✅ Project delivered
✅ LeetCode + HackerRank progress maintained
