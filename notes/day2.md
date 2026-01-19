# Day 2 – Python Basics + Arrays Practice

## What I worked on

Focused on strengthening Python fundamentals using HackerRank and array-based problems from LeetCode. Also practiced real-world tooling with Git and VS Code.

---

## Concepts Learned / Revised

### 1. Python Input & Output

* Used `input()` and converted input to integers with `int()`
* Learned that Python reads **only user input**, not terminal commands

### 2. Integer vs Float Division

* `a // b` → integer (floor) division
* `a / b` → float division

### 3. Loops

* Used `for i in range(n)` to iterate from `0` to `n-1`
* Printed results line-by-line as required by HackerRank

### 4. Print Control

* Used `print(value, end="")` to print output on the same line
* Avoided string methods as per problem constraints

### 5. Arrays & Bit Manipulation (LeetCode)

* Learned XOR trick:

  * `a ^ a = 0`
  * `a ^ 0 = a`
* Used XOR to find a single non-duplicate number efficiently

### 6. Two Pointer Technique

* Merged two sorted arrays **in-place**
* Started filling from the back to avoid overwriting values

### 7. Git & Terminal Basics

* Understood the difference between:

  * Running a Python program
  * Providing input to the program
  * Running Git commands
* Learned that:

  * `git commit` works offline
  * `git push` requires internet
* Fixed untracked file issues using `git add`

---

## Mistakes & Fixes

* ❌ Typed Git commands while Python was waiting for input
  ✅ Fixed by separating program execution and Git workflow
* ❌ VS Code error: `List is not defined`
  ✅ Fixed by adding `from typing import List`
* ❌ Used Linux commands (`touch`, `pip`) on Windows
  ✅ Switched to PowerShell equivalents

---

## Overall Takeaway

Today helped me understand not just Python syntax, but **how real development workflows work** using terminal, Git, and editors. Fundamentals are getting clearer.
