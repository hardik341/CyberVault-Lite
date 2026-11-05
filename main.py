"""CyberVault Lite: a beginner-friendly password safety learning project."""
from datetime import datetime
from pathlib import Path
import json
import secrets
import string

HISTORY_FILE = Path(__file__).parent / 'history.json'


class PasswordChecker:
    """Check basic properties of a sample password (not a security guarantee)."""

    def check(self, password):
        checks = {
            'At least 12 characters': len(password) >= 12,
            'Uppercase letter': any(char.isupper() for char in password),
            'Lowercase letter': any(char.islower() for char in password),
            'Number': any(char.isdigit() for char in password),
            'Symbol': any(char in string.punctuation for char in password),
        }
        score = sum(checks.values())
        return score, checks

    def label(self, score):
        if score <= 2:
            return 'WEAK'
        elif score <= 4:
            return 'MEDIUM'
        return 'STRONG (basic rules only)'


class AdvancedPasswordChecker(PasswordChecker):
    """Demonstrates inheritance and method overriding."""

    def label(self, score):
        return super().label(score)

    def __str__(self):
        return 'CyberVault password checker'


def generate_password(length=16):
    """Generate a password using cryptographically secure randomness."""
    if not 12 <= length <= 64:
        raise ValueError('Length must be between 12 and 64.')
    groups = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    characters = [secrets.choice(group) for group in groups]
    alphabet = ''.join(groups)
    characters += [secrets.choice(alphabet) for _ in range(length - len(characters))]
    # Fisher-Yates shuffle using secrets rather than random.
    for i in range(len(characters) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        characters[i], characters[j] = characters[j], characters[i]
    return ''.join(characters)


def load_history(path=HISTORY_FILE):
    if not path.exists():
        return []
    try:
        with path.open('r', encoding='utf-8') as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError('History must be a list.')
        return data
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f'Could not read history: {error}')
        return []


def save_result(score, label, path=HISTORY_FILE):
    history = load_history(path)
    history.append({'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
                    'score': score, 'rating': label})
    try:
        with path.open('w', encoding='utf-8') as file:
            json.dump(history, file, indent=2)
    except OSError as error:
        print(f'Could not save history: {error}')


def show_history():
    history = load_history()
    if not history:
        print('No history yet.')
        return
    for number, record in enumerate(history, 1):
        print(f"{number}. {record['date']} | {record['score']}/5 | {record['rating']}")


def show_statistics():
    history = load_history()
    if not history:
        print('No checks recorded yet.')
        return
    counts = {'WEAK': 0, 'MEDIUM': 0, 'STRONG': 0}
    for record in history:
        rating = record.get('rating', '')
        if rating.startswith('STRONG'):
            counts['STRONG'] += 1
        elif rating in counts:
            counts[rating] += 1
    print(f'Total checks: {len(history)}')
    for name, count in counts.items():
        print(f'{name}: {count}')


def main():
    checker = AdvancedPasswordChecker()
    while True:
        print('\n=== CYBERVAULT LITE ===')
        print('1. Check password strength')
        print('2. Generate password')
        print('3. View check history')
        print('4. View statistics')
        print('5. Exit')
        choice = input('Choose (1-5): ').strip()
        if choice == '1':
            print('Use only fictional/test passwords. Input is visible on screen.')
            password = input('Enter sample password: ')
            score, checks = checker.check(password)
            rating = checker.label(score)
            print(f'Rating: {rating} | Score: {score}/5')
            for description, passed in checks.items():
                print(f"{'PASS' if passed else 'MISS'} - {description}")
            save_result(score, rating)
        elif choice == '2':
            try:
                length = int(input('Password length (12-64, default 16): ').strip() or '16')
                print('Generated password:', generate_password(length))
                print('This password is not saved by CyberVault.')
            except ValueError as error:
                print('Invalid length:', error)
        elif choice == '3':
            show_history()
        elif choice == '4':
            show_statistics()
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Please enter a number from 1 to 5.')


if __name__ == '__main__':
    main()
