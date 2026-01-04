# Lecture 01: Environment Setup & Hello Data

Welcome to your first lecture in **Intro to Data Engineering: Python Fundamentals**! In this lecture, you'll set up your Python environment and write your first data-focused Python program.

---

## Learning Objectives

By the end of this lecture, you will be able to:

- Set up a Python development environment (browser-based or local)
- Write and run a simple Python program
- Use the `print()` function to display output
- Understand how data engineering uses Python to process information
- Write your first data-focused program

---

## What is Data Engineering?

**Data Engineering** is the practice of designing and building systems that collect, process, and transform raw data into usable formats for analysis. Data engineers are the bridge between raw data sources and data analysts/scientists.

Think of it like this:
- **Raw Data**: A messy pile of transaction records
- **Data Engineer**: Organizes, cleans, and structures the data
- **Result**: Clean, organized data ready for analysis

In this course, you'll learn Python skills specifically for data engineering tasks like:
- Reading data from files (CSV, JSON)
- Cleaning and validating data
- Transforming data formats
- Preparing data for databases

---

## Environment Setup

### Option 1: Replit (Recommended for Beginners)

1. Go to [replit.com](https://replit.com)
2. Sign up for a free account (or sign in)
3. Click "Create Repl"
4. Select "Python" as the language
5. Name it "data-engineering-course"
6. Click "Create Repl"

You're ready to code! Replit provides a complete Python environment in your browser.

### Option 2: Google Colab

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Sign in with your Google account
3. Click "New Notebook"
4. You're ready to code!

**Note**: Colab uses Jupyter notebooks, so code cells work slightly differently than regular Python files.

### Option 3: Local Python Installation

If you prefer to work locally:

1. Download Python 3.9+ from [python.org](https://www.python.org/downloads/)
2. Install Python (check "Add Python to PATH" during installation)
3. Open a terminal/command prompt
4. Verify installation: `python --version`
5. Use any text editor (VS Code, PyCharm, Sublime Text, etc.)

---

## Your First Python Program

Let's start with the classic "Hello, World!" program, but with a data engineering twist.

### Example 1: Hello, World!

```python
print("Hello, World!")
```

**What's happening?**
- `print()` is a built-in Python function that displays text
- The text inside quotes is a **string** (text data)
- When you run this, it displays: `Hello, World!`

### Example 2: Hello, Data!

Now let's make it data-focused:

```python
print("Hello, Data Engineering!")
print("Today we're learning Python for data processing.")
print("Let's process some banking transactions!")
```

**Output:**
```
Hello, Data Engineering!
Today we're learning Python for data processing.
Let's process some banking transactions!
```

### Example 3: Displaying Transaction Data

Let's display some sample banking transaction data:

```python
print("=== Banking Transaction Data ===")
print("Transaction ID: TX001")
print("Account: 12345")
print("Amount: $150.00")
print("Type: Deposit")
print("Date: 2024-01-15")
```

**Output:**
```
=== Banking Transaction Data ===
Transaction ID: TX001
Account: 12345
Amount: $150.00
Type: Deposit
Date: 2024-01-15
```

---

## Understanding the Code

### The `print()` Function

- **Purpose**: Displays output to the console/screen
- **Syntax**: `print(value)`
- **Can print**: Text (strings), numbers, variables, and more

### Strings (Text Data)

- Text in Python is called a **string**
- Strings are enclosed in quotes: `"double quotes"` or `'single quotes'`
- Both work the same way in Python

### Comments

You can add notes to your code using comments:

```python
# This is a comment - Python ignores this line
print("This code runs")  # Comments can be on the same line too
```

Comments help explain what your code does and are essential for data engineering projects!

---

## Running Your Code

### In Replit:
1. Write your code in the editor
2. Click the green "Run" button
3. See output in the console below

### In Google Colab:
1. Write code in a cell
2. Press `Shift + Enter` to run
3. Output appears below the cell

### Locally:
1. Save your file as `hello_data.py`
2. Open terminal in that directory
3. Run: `python hello_data.py`
4. See output in terminal

---

## Hands-On Challenge

Now it's your turn! Complete the following challenge:

### Challenge: Display Account Information

Create a Python program that displays information for a bank account. Your program should:

1. Display a header: "=== Account Information ==="
2. Display the account number: "Account Number: 98765"
3. Display the account holder name: "Account Holder: Jane Smith"
4. Display the account balance: "Current Balance: $2,500.00"
5. Display the account type: "Account Type: Checking"

**Requirements:**
- Use the `print()` function for each line
- Add comments explaining what each section does
- Make sure your code runs without errors

### Challenge Template

Create a new file called `account_info.py` and write your solution there.

**Hint**: Look at Example 3 above for the structure, but customize it for account information instead of transactions.

---

## Solution Review

After you've attempted the challenge, check the `challenge_solution.py` file to see a complete solution. Don't peek until you've tried it yourself!

### Key Takeaways

1. **`print()` is your friend** - It's how you display output in Python
2. **Strings are text data** - Use quotes around text
3. **Comments help** - Explain what your code does
4. **Data engineering starts simple** - Even displaying data is a data engineering task!

---

## Common Mistakes to Avoid

❌ **Forgetting quotes around strings**
```python
print(Hello, World!)  # ERROR - missing quotes
print("Hello, World!")  # CORRECT
```

❌ **Using wrong quote types**
```python
print("Hello, World!")  # CORRECT
print("Hello, World!")  # CORRECT (both work)
print("Hello, World!")  # ERROR - mixing quotes
```

❌ **Forgetting parentheses**
```python
print "Hello, World!"  # ERROR in Python 3
print("Hello, World!")  # CORRECT
```

---

## What's Next?

In the next lecture, we'll learn about:
- **Variables** - Storing data in memory
- **Data Types** - Different kinds of data (numbers, text, etc.)
- How to work with banking transaction data using variables

---

## Practice Exercises

Try these additional exercises to reinforce what you learned:

1. **Exercise 1**: Display your own name and a favorite number
2. **Exercise 2**: Display three different transaction records (use the format from Example 3)
3. **Exercise 3**: Create a "receipt" that displays:
   - Store name
   - Item purchased
   - Price
   - Date

---

## Summary

In this lecture, you learned:

✅ How to set up a Python environment  
✅ How to use the `print()` function  
✅ How to display text (strings)  
✅ How to add comments to your code  
✅ How to write your first data-focused Python program  

**Congratulations!** You've written your first Python program for data engineering. In the next lecture, we'll learn how to store and manipulate data using variables.

---

## Additional Resources

- [Python.org Official Tutorial](https://docs.python.org/3/tutorial/)
- [Replit Python Guide](https://docs.replit.com/programming-ide/getting-started-python)
- [Google Colab Introduction](https://colab.research.google.com/notebooks/intro.ipynb)

---

**Ready for the next lecture?** Head to [Lecture 02: Variables & Data Types](../lecture02/README.md)
