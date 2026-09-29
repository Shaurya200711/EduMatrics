# EduMatrics: VIT Academic Forecaster

**Developer:** Shaurya Gaur (26BCE10791)  
**Course:** Python Essentials Evaluated Course Project  

## Project Overview
EduMatrics is a Python command-line application built to help university students plan their academics. It calculates the exact SGPA needed in future semesters to reach a target CGPA, and it includes an attendance forecaster to make sure students safely maintain their 75% attendance criteria. 

This project was built entirely using core Python concepts taught in the first semester, with absolutely no external libraries, databases, or graphical interfaces.

## Features
* **Immediate CGPA Forecast:** Calculates what you need to score next semester and draws a simple text-based timeline graph directly in the terminal.
* **Long-Term Planning:** Spreads out your required credits to show you the sustained SGPA you need to graduate with your target CGPA.
* **Attendance Engine:** Uses basic math rounding to tell you exactly how many consecutive classes you need to attend, or how many you can safely miss.
* **Dynamic Student Database:** Pre-loaded with over 70 student records. If you type a Registration Number that isn't in the system, the program asks for the details, saves them in active memory, and seamlessly continues to the forecast.

## Technical Stack
This project proves the utility of basic Python data structures:
* **Dictionaries:** Used as an in-memory database for fast lookups of student profiles.
* **Tuples:** Used to securely store curriculum data (ensuring course structures cannot be accidentally modified during runtime).
* **Sets:** Used to track unique user sessions.
* **Math Module:** Uses `math.ceil()` and `math.floor()` for accurate attendance requirement calculations.

## How to Run the Project
This project runs purely in the terminal and requires zero external installations or dependencies. As long as Python 3 is installed on your computer, it will run instantly.

**Step 1: Download the Code**
Open your terminal or command prompt and clone the repository:
```bash
git clone [https://github.com/Shaurya200711/EduMatrics.git](https://github.com/Shaurya200711/EduMatrics.git)