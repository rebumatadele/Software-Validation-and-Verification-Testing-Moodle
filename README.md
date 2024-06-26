## Description

Moodle Learning Manangement Tests

## Overview

This project demonstrates how to interact with the Moodle demo site, including logging in, navigating to a course, submitting and evaluating assignments, enrollments and taking a quiz.

## Prerequisites

- Python 3.x
- Selenium WebDriver (e.g., ChromeDriver, GeckoDriver)

## Installation

1. Clone the repository:

```
git clone https://github.com/rebumatadele/Software-Validation-and-Verification-Testing-Moodle.git
```

2. Install the required Python packages:

```
pip install selenium
```

3. Download the appropriate Selenium WebDriver for your browser and make sure it's in your system's PATH.

## Usage

1. Navigate to the project directory:

```
cd Software-Validation-and-Verification-Testing-Moodle/Login_test_suit
```

2. Run the test script:

```
python user_login_test.py
```

## Test Script Explanation

Example:
The `test_quiz_taking()` function in the `take_quiz_verify_result_test.py` file demonstrates the following steps:

1. Navigate to the Moodle demo site: `https://school.moodledemo.net/login/index.php`
2. Wait for the page to load and find the login fields
3. Enter the student login credentials (username: `student`, password: `moodle`)
4. Click the login button
5. Wait for the dashboard page to load
6. Navigate to the "Test Course"
7. Navigate to the "Test Quiz"
8. Wait for the quiz page to load
9. Answer the question
10. Submit the quiz
11. Wait for the results page to load
12. Verify the quiz result

After the test is complete, the `tearDown()` function closes the browser.

## Limitations

- This script is designed to work with the specific Moodle demo site and might not be repeated because the demo site refreshes the page every 40 minutes so the field names might change after
- The script assumes that the Selenium WebDriver is properly configured and accessible in the system's PATH.

## Contributing

- If you find any issues or have suggestions for improvements, please feel free to open a new issue or submit a pull request.
- Also Consider, this project is performed for a software validation and verification course in accelerated masters program at AASTU,
- Instructed by Dr. Girma Neshir
