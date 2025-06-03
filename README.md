# 🔐 Password Strength Tester

A comprehensive Python tool for analyzing password security with detailed reporting capabilities and crack time estimation.

## 🌟 Features

### Core Analysis
- **🔍 Comprehensive Security Analysis**: Evaluates length, character variety, patterns, and vulnerabilities
- **👤 Name Detection**: Identifies common names in passwords (major security risk)
- **⏱️ Advanced Crack Time Estimation**: Shows realistic time ranges for different attack scenarios
- **📊 Character Composition Analysis**: Detailed breakdown of password components
- **💡 Smart Suggestions**: Actionable recommendations for password improvement

### Reporting & Output
- **📄 PDF Report Generation**: Professional security analysis reports with ReportLab
- **🎯 10-Point Scoring System**: Clear strength rating from Very Weak to Very Strong
- **📈 Attack Scenario Modeling**: Shows crack times for basic, modern, and advanced hardware
- **💻 Interactive CLI**: User-friendly command-line interface

### Advanced Features
- **🔍 Pattern Detection**: Identifies common sequences (123, abc, qwerty, etc.)
- **🔄 Repetitive Character Detection**: Flags patterns like "aaa" or "111"
- **🎭 Name Database**: Checks against 70+ common first names
- **⚡ Multi-Scenario Analysis**: Basic/Modern/Advanced hardware crack time estimates

## 🚀 Quick Start

### Installation
```bash
# Clone and install dependencies
git clone <your-repo-url>
cd password-strength-tester
pip install -r requirements.txt
```

### Basic Usage
```bash
python main.py
```

### Example Session
```
🔐 Password Strength Tester
========================================

Enter password to test (or 'quit' to exit): MySecure#Pass2024!

📊 Password Analysis Results
------------------------------
Password Length: 17 characters
Strength Score: 10/10
Strength Level: Very Strong
Estimated Crack Time:
  Range: 1.23e+28 years - 2.46e+28 years
  Fast attack: 1.23e+27 years

📝 Detailed Analysis:
  ✅ Excellent length (17 chars)
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
  Special: 3

⚡ Attack Scenarios:
  • Basic hardware: ~100M attempts/sec
  • Modern hardware: ~1B attempts/sec
  • Advanced/GPU: ~10B attempts/sec
```

## 📊 Scoring System

The tool uses a comprehensive **10-point scoring system**:

| Criteria | Points | Requirements |
|----------|--------|-------------|
| **Length** | 0-3 | 8-11 chars (1pt), 12-15 chars (2pts), 16+ chars (3pts) |
| **Lowercase** | 1 | Contains a-z characters |
| **Uppercase** | 1 | Contains A-Z characters |
| **Numbers** | 1 | Contains 0-9 digits |
| **Special Characters** | 1 | Contains punctuation/symbols |
| **No Repetition** | 1 | No 3+ consecutive identical chars |
| **No Common Patterns** | 1 | Avoids 123, abc, qwerty, password, etc. |
| **No Names** | 1 | No common first names detected |

### Strength Levels
- **🔴 0-3 points**: Very Weak - Easily crackable
- **🟠 4-5 points**: Weak - Poor security
- **🟡 6-7 points**: Moderate - Acceptable for low-risk
- **🟢 8-9 points**: Strong - Good security
- **💚 10 points**: Very Strong - Excellent security

## 🎯 Security Checks

### ✅ What We Analyze
- **Length Requirements**: Minimum 8 chars, recommends 12+
- **Character Variety**: Lowercase, uppercase, numbers, special characters
- **Pattern Detection**: Common sequences and keyboard patterns
- **Name Detection**: 70+ common first names database
- **Repetitive Characters**: Flags obvious repetition
- **Dictionary Patterns**: Common words and phrases

### ⚡ Crack Time Estimation
Our advanced estimation considers:
- **Character Set Complexity**: Based on actual password composition
- **Multiple Attack Scenarios**: 
  - Basic hardware: ~100M attempts/sec
  - Modern hardware: ~1B attempts/sec  
  - Advanced/GPU: ~10B attempts/sec
- **Realistic Ranges**: Shows average to worst-case scenarios
- **Human-Readable Format**: Seconds to years conversion

## 📄 PDF Reports

Generate comprehensive security reports containing:

### 📋 Report Sections
1. **Executive Summary**: Score, strength level, crack time
2. **Character Analysis**: Detailed composition breakdown
3. **Security Assessment**: All feedback points and warnings
4. **Improvement Plan**: Specific, actionable recommendations
5. **Best Practices**: Industry-standard security guidelines

### 📁 Report Features
- **Timestamped Filenames**: Unique report identification
- **Professional Formatting**: Clean tables and structured layout
- **Special Character Handling**: Proper Unicode support
- **Comprehensive Content**: All analysis details included

## 🛠️ Development & Testing

### Run Tests
```bash
# Run all tests
python tests/test_password_analysis.py
python tests/test_report_generation.py

# Or use the test script
bash scripts/run_tests.sh
```

### Demo Script
```bash
# Interactive demonstration
python examples/demo_script.py

# Shell-based demo
bash scripts/demo.sh
```

### Project Structure
```
📁 password-strength-tester/
├── 📄 main.py                    # Core application
├── 📁 tests/                     # Unit tests
│   ├── test_password_analysis.py
│   └── test_report_generation.py
├── 📁 examples/                  # Demos and samples
│   ├── demo_script.py
│   └── sample_passwords.txt
├── 📁 docs/                      # Documentation
│   ├── api-reference.md
│   ├── examples.md
│   └── security-guide.md
├── 📁 scripts/                   # Utility scripts
└── 📄 README.md                  # This file
```

## 🔧 Technical Details

### Dependencies
- **Python 3.10+**: Core runtime
- **ReportLab**: PDF generation library
- **Standard Library**: re, string, math, datetime

### Character Sets Supported
- **Lowercase**: a-z (26 characters)
- **Uppercase**: A-Z (26 characters) 
- **Digits**: 0-9 (10 characters)
- **Special**: All ASCII punctuation + space (33 characters)

### Name Detection Database
Includes 70+ common first names with:
- Case-insensitive matching
- Pattern variations (John123, mary!)
- False positive prevention

## 🌐 Deployment on Replit

This tool is designed to work seamlessly on Replit:

1. **Fork/Import** this repository to Replit
2. **Run** the main.py file directly
3. **Generate PDFs** within the Replit environment
4. **Access files** through the Replit file browser

## 🔒 Security & Privacy

### ⚠️ Important Notes
- **Educational Purpose**: This tool is for security assessment and education
- **No Data Storage**: Passwords are not saved or transmitted
- **Local Analysis**: All processing happens locally
- **Test Passwords Only**: Never use real passwords in shared environments

### 🛡️ Best Practices
- Use this tool to test password candidates before setting real passwords
- Generate PDF reports for security documentation
- Regular password strength audits
- Follow organizational password policies

## 🤝 Contributing

We welcome contributions! Areas for improvement:
- Additional pattern detection
- More language support for names
- Enhanced crack time algorithms
- UI/UX improvements

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For questions, issues, or suggestions:
- 🐛 **Bug Reports**: Use the issues tracker
- 💡 **Feature Requests**: Submit enhancement ideas
- 📖 **Documentation**: Check the `/docs` folder
- 🧪 **Testing**: Run the test suite for validation

---

**🎯 Ready to test your password security? Run `python main.py` and get started!**
