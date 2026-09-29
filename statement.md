# Problem Statement: EduMatrics

**Project Title:** EduMatrics - Academic Performance & Attendance Forecaster  
**Developer:** Shaurya Gaur (26BCE10791)  
**Course:** Python Essentials Evaluated Course Project  

## 1. The Problem
University students frequently face two major academic challenges that cause unnecessary stress:
1. **The 75% Attendance Rule:** Manually tracking and calculating how many classes can be safely missed (or must be continuously attended) to maintain the strict 75% university criteria is confusing and prone to calculation errors, which can lead to debarment.
2. **CGPA/SGPA Management:** Students often set a target CGPA for placements or higher studies, but struggle to calculate exactly what SGPA they need to achieve in their immediate upcoming semester, or across their remaining degree, to mathematically hit that exact target. 

## 2. The Solution
EduMatrics is a purely Python-based Command-Line Interface (CLI) application designed to solve these issues programmatically. It acts as an algorithmic academic companion that:
* Evaluates current attendance and uses mathematical functions to tell the student exactly how many upcoming classes they need to attend consecutively, or how many they can safely skip.
* Calculates the exact SGPA required for a single upcoming semester to reach a specific target CGPA, generating a visual ASCII graph of the progress.
* Distributes credit requirements across multiple remaining semesters for long-term, 4-year degree planning.

## 3. Technical Scope and Constraints
To demonstrate a strong grasp of foundational programming, this project was developed strictly within the scope of first-semester Python concepts:
* **Data Structures:** Utilizes Dictionaries as an in-memory database for fast student record retrieval, Tuples for immutable course data, and Sets for unique session tracking.
* **Logic:** Implements standard `while` loops, nested `if/elif` conditional routing, and `math.ceil`/`math.floor` rounding for precise class-count calculations.
* **Dependencies:** Built entirely with Python standard libraries. It relies on zero external dependencies, web frameworks, or graphical user interfaces (GUIs).