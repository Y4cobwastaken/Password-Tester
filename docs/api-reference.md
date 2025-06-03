# API Reference

## Core Functions

### `analyze_password_strength(password)`

Performs comprehensive password strength analysis.

**Parameters:**
- `password` (str): The password to analyze

**Returns:**
- `score` (int): Strength score (0-10)
- `feedback` (list): List of analysis feedback strings
- `strength` (str): Strength level description

**Example:**
```python
score, feedback, strength = analyze_password_strength("MyPassword123!")
# Returns: (8, ['✅ Good length (13 chars)', ...], 'Strong')
```

### `detect_names_in_password(password)`

Detects common names in passwords.

**Parameters:**
- `password` (str): Password to check for names

**Returns:**
- `detected_names` (list): List of detected names

**Example:**
```python
names = detect_names_in_password("john123")
# Returns: ['John']
```

### `estimate_crack_time(password)`

Estimates brute-force crack time based on character set complexity.

**Parameters:**
- `password` (str): Password to analyze

**Returns:**
- `crack_time` (str): Human-readable time estimate

**Example:**
```python
time = estimate_crack_time("ComplexP@ssw0rd!")
# Returns: "1.23e+12 years"
```

### `get_password_suggestions(feedback)`

Generates improvement suggestions based on analysis feedback.

**Parameters:**
- `feedback` (list): Analysis feedback from `analyze_password_strength()`

**Returns:**
- `suggestions` (list): List of improvement suggestions

### `generate_pdf_report(password, score, feedback, strength, crack_time, suggestions)`

Generates a comprehensive PDF security report.

**Parameters:**
- `password` (str): Original password
- `score` (int): Strength score
- `feedback` (list): Analysis feedback
- `strength` (str): Strength level
- `crack_time` (str): Estimated crack time
- `suggestions` (list): Improvement suggestions

**Returns:**
- `filename` (str): Generated PDF filename

## Character Sets

The tool recognizes these character types:

- **Lowercase**: `a-z` (26 characters)
- **Uppercase**: `A-Z` (26 characters)
- **Digits**: `0-9` (10 characters)
- **Special**: All ASCII punctuation + space (33 characters total)

## Scoring System

Total possible score: **10 points**

| Criteria | Points | Description |
|----------|--------|-------------|
| Length 8-11 chars | 1 | Minimum acceptable |
| Length 12-15 chars | 2 | Good length |
| Length 16+ chars | 3 | Excellent length |
| Lowercase letters | 1 | Contains a-z |
| Uppercase letters | 1 | Contains A-Z |
| Numbers | 1 | Contains 0-9 |
| Special characters | 1 | Contains punctuation/symbols |
| No repetitive chars | 1 | No 3+ consecutive same chars |
| No common patterns | 1 | Avoids 123, abc, qwerty, etc. |
| No names detected | 1 | No common first names |

## Strength Levels

| Score | Level | Description |
|-------|-------|-------------|
| 0-3 | Very Weak | Easily crackable |
| 4-5 | Weak | Poor security |
| 6-7 | Moderate | Acceptable for low-risk |
| 8-9 | Strong | Good security |
| 10 | Very Strong | Excellent security |
