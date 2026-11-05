# CyberVault Lite 🔐

**A beginner-friendly terminal-based password safety learning project**  
**Course:** Python Programming (CSE1005-I)  
**University:** D Y Patil International University, Pune  
**Scope:** Modules I–V

## About
CyberVault Lite checks sample password characteristics, generates passwords with Python's `secrets` module, records scores (not passwords), and displays statistics. It is a first-semester educational project, **not a professional password manager**.

## Features
1. **Password strength checker:** Five basic checks (12+ characters, upper/lowercase, digits, symbols).
2. **Password generator:** Generates 12–64 character passwords using cryptographically secure randomness.
3. **Check history:** Stores only dates, scores, and ratings in a local JSON file.
4. **Statistics:** Counts weak, medium, and strong checks.
5. **Input handling:** Handles invalid menu options and password lengths.

**Note:** A score of 5/5 does not guarantee a password is secure. The checker does not test breached passwords, predictability, or password reuse. Do not enter real passwords: the terminal input is visible.

## Requirements
- Python 3.9 or newer
- No third-party packages

## Run
```bash
python main.py
```
On some systems use `python3 main.py`.

## Run tests
From the project folder:
```bash
python -m unittest discover -s tests -v
```

## Folder structure
```
CyberVault-Lite/
├── main.py
├── tests/
│   └── test_main.py
├── README.md
├── .gitignore
└── LICENSE
```
The `history.json` file is created when a check is saved and is excluded from Git.

## Module-wise syllabus mapping
| Module | Concepts demonstrated | Where |
|---|---|---|
| I: Basics and I/O | variables, strings, operators, `input`, `print`, conversion | `main()`, `check()` |
| II: Control Flow and Functions | `if/elif/else`, `while`, `for`, `break`, functions, default arguments | `main()`, `generate_password()` |
| III: Data Structures | lists, dictionaries, iteration, `enumerate`, dictionary methods | `generate_password()`, `check()`, `show_history()`, `show_statistics()` |
| IV: Files, Exceptions and OOP | JSON files, `with`, `try/except`, classes, constructors via default initialization | `load_history()`, `save_result()`, `PasswordChecker` |
| V: Advanced OOP | inheritance, `super()`, overriding, special method `__str__` | `AdvancedPasswordChecker` |

This project demonstrates representative concepts from all five modules, **not every subtopic** (e.g. multiple inheritance and recursion are not needed for this small application).

## Example session
```
=== CYBERVAULT LITE ===
1. Check password strength
2. Generate password
3. View check history
4. View statistics
5. Exit
Choose (1-5): 1
Use only fictional/test passwords. Input is visible on screen.
Enter sample password: Example123!Password
Rating: STRONG (basic rules only) | Score: 5/5
```

## Privacy and limitations
- Never use real passwords when testing the checker.
- Generated passwords are shown on screen and not stored by the program.
- Only check metadata is saved locally; it is not encrypted.
- Password ratings are a simple classroom demonstration, not a security certification.

## GitHub submission
1. Create a new GitHub repository called `CyberVault-Lite`.
2. Upload `main.py`, `tests/test_main.py`, `README.md`, `.gitignore`, and `LICENSE`.
3. Run the application and tests locally.
4. Submit your repository URL in your professor's Google Form.

## Author
First-year BTech CSE (Cyber Security & Forensics) student, DYPIU. Add your preferred name and GitHub profile before submission.
