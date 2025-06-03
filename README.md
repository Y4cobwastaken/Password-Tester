# 🔐 Password Strength Tester

A comprehensive Python tool for analyzing password security with detailed reporting capabilities.

## Features

- **Comprehensive Analysis**: Evaluates password length, character variety, patterns, and potential vulnerabilities
- **Name Detection**: Identifies if passwords contain common names (security risk)
- **Crack Time Estimation**: Estimates brute-force attack time based on character set complexity
- **PDF Reports**: Generate downloadable security analysis reports
- **Interactive CLI**: User-friendly command-line interface

## Security Checks

The tool analyzes passwords for:

- ✅ Length requirements (minimum 8 characters, recommended 12+)
- ✅ Character variety (lowercase, uppercase, numbers, special characters)
- ✅ Repetitive character patterns
- ✅ Common password patterns (123, abc, qwerty, etc.)
- ✅ Name detection (checks against common first names)
- ✅ Brute-force crack time estimation

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   poetry install
   ```

## Usage

Run the password tester:

```bash
python main.py
```

The tool will prompt you to:
1. Enter a password for analysis
2. View detailed security feedback
3. Optionally generate a PDF report

### Example Output

```
🔐 Password Strength Tester
========================================

Enter password to test (or 'quit' to exit): MySecureP@ssw0rd2024

📊 Password Analysis Results
------------------------------
Password Length: 20 characters
Strength Score: 10/10
Strength Level: Very Strong
Estimated Crack Time: 2.84e+35 years

📝 Detailed Analysis:
  ✅ Excellent length (20 chars)
  ✅ Contains lowercase letters
  ✅ Contains uppercase letters
  ✅ Contains numbers
  ✅ Contains special characters
  ✅ No repetitive characters
  ✅ No common patterns detected
  ✅ No common names detected

🔍 Character Composition:
  Lowercase: 7
  Uppercase: 3
  Numbers: 4
  Special: 6
```

## Scoring System

The tool uses a 10-point scoring system:

- **Length**: 0-3 points based on character count
- **Lowercase letters**: 1 point
- **Uppercase letters**: 1 point
- **Numbers**: 1 point
- **Special characters**: 1 point
- **No repetitive patterns**: 1 point
- **No common patterns**: 1 point
- **No names detected**: 1 point

## Strength Levels

- **0-3 points**: Very Weak
- **4-5 points**: Weak
- **6-7 points**: Moderate
- **8-9 points**: Strong
- **10 points**: Very Strong

## PDF Reports

Generate detailed PDF reports containing:
- Security analysis summary
- Character composition breakdown
- Specific improvement recommendations
- General security best practices

## Dependencies

- Python 3.10+
- reportlab (for PDF generation)

## Security Note

This tool is for educational and security assessment purposes. Never use real passwords in shared environments or untrusted systems.

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
