# Installation Guide

## Prerequisites

### System Requirements
- **Python**: 3.10 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 512MB RAM
- **Storage**: 50MB free space

### Check Python Version
```bash
python --version
# or
python3 --version
```

If Python is not installed, download from [python.org](https://python.org).

## Installation Methods

### Method 1: Using Poetry (Recommended)

Poetry provides better dependency management and isolation.

1. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/password-strength-tester.git
   cd password-strength-tester
   ```

3. **Install dependencies**:
   ```bash
   poetry install
   ```

4. **Run the application**:
   ```bash
   poetry run python main.py
   ```

### Method 2: Using pip

Standard Python package installation.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/password-strength-tester.git
   cd password-strength-tester
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

### Method 3: Virtual Environment (Recommended for Development)

Isolates project dependencies from system packages.

1. **Create virtual environment**:
   ```bash
   python -m venv password-tester-env
   ```

2. **Activate virtual environment**:
   
   **On Windows**:
   ```bash
   password-tester-env\Scripts\activate
   ```
   
   **On macOS/Linux**:
   ```bash
   source password-tester-env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## Dependency Details

### Core Dependencies
- **reportlab** (>=4.4.1): PDF generation library
  - Used for creating detailed security reports
  - Includes fonts, graphics, and table formatting

### Development Dependencies (Optional)
For contributors and developers:

```bash
# Install development dependencies
poetry install --group dev

# Or with pip
pip install pytest black flake8 mypy
```

## Verification

### Test Installation
Run the application to verify everything works:

```bash
python main.py
```

You should see:
```
🔐 Password Strength Tester
========================================

Enter password to test (or 'quit' to exit):
```

### Test PDF Generation
1. Enter a test password (e.g., "TestPassword123!")
2. When prompted, generate a PDF report
3. Verify the PDF file is created in the project directory

## Troubleshooting

### Common Issues

#### Issue: "reportlab not found"
**Solution**: Reinstall reportlab
```bash
pip install --upgrade reportlab
```

#### Issue: PDF generation fails
**Symptoms**: Error when generating PDF reports
**Solutions**:
1. Check write permissions in the project directory
2. Ensure sufficient disk space
3. Verify reportlab installation:
   ```python
   import reportlab
   print(reportlab.__version__)
   ```

#### Issue: "Python command not found"
**Solutions**:
- Use `python3` instead of `python`
- Add Python to your system PATH
- Reinstall Python with "Add to PATH" option

#### Issue: Permission denied errors
**On Unix systems**:
```bash
chmod +x main.py
```

**On Windows**: Run terminal as administrator

### Platform-Specific Notes

#### Windows
- Use PowerShell or Command Prompt
- May need to use `py` instead of `python`
- Install Visual C++ Build Tools if compilation errors occur

#### macOS
- Install Xcode Command Line Tools:
  ```bash
  xcode-select --install
  ```
- Use `python3` explicitly

#### Linux
- Install development packages:
  ```bash
  # Ubuntu/Debian
  sudo apt update
  sudo apt install python3-pip python3-venv
  
  # CentOS/RHEL
  sudo yum install python3-pip
  ```

## Configuration

### Environment Variables (Optional)
Create a `.env` file for custom settings:

```bash
# Default output directory for PDF reports
REPORT_OUTPUT_DIR=./reports

# Custom name database file
NAMES_DATABASE=./custom_names.txt
```

### Custom Configuration
Modify settings in `main.py` if needed:

```python
# Adjust minimum password length
MIN_PASSWORD_LENGTH = 8

# Modify crack time calculation
ATTEMPTS_PER_SECOND = 1_000_000_000
```

## Uninstallation

### Remove with Poetry
```bash
poetry env remove python
```

### Remove with pip
```bash
pip uninstall reportlab
```

### Remove Virtual Environment
```bash
# Deactivate first
deactivate

# Remove directory
rm -rf password-tester-env  # Linux/macOS
rmdir /s password-tester-env  # Windows
```

## Next Steps

After successful installation:

1. Read the [Usage Examples](examples.md)
2. Review [Security Best Practices](security-guide.md)
3. Check the [API Reference](api-reference.md) for customization
4. Consider setting up automated password auditing

## Getting Help

If you encounter issues:

1. Check this troubleshooting section
2. Review the [API Reference](api-reference.md)
3. Submit an issue on GitHub
4. Check for updated dependencies

## Updates

Keep your installation current:

```bash
# With Poetry
poetry update

# With pip
pip install --upgrade -r requirements.txt
```

Check for application updates regularly for new features and security improvements.
