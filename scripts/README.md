# Scripts

This directory contains utility scripts for development, testing, and demonstration of the Password Strength Tester.

## Available Scripts

### `setup.sh`
**Purpose**: Complete development environment setup

**Features**:
- ✅ Python version verification (3.10+ required)
- ✅ Poetry installation and configuration
- ✅ Dependency management (Poetry or pip fallback)
- ✅ Development tools setup (VS Code settings)
- ✅ Example environment creation
- ✅ Installation verification

**Usage**:
```bash
# Make executable and run
chmod +x scripts/setup.sh
./scripts/setup.sh

# Or run directly with bash
bash scripts/setup.sh
```

**What it does**:
1. Checks Python installation and version
2. Installs Poetry if not present (optional)
3. Installs project dependencies
4. Sets up development environment
5. Creates example files and VS Code settings
6. Verifies installation with basic tests

### `run_tests.sh`
**Purpose**: Comprehensive test execution with reporting

**Features**:
- ✅ Multiple test execution modes
- ✅ Detailed test reporting
- ✅ Colored output for readability
- ✅ Test report archival
- ✅ pytest integration (if available)
- ✅ Specific test pattern matching

**Usage**:
```bash
# Run all tests (default)
./scripts/run_tests.sh

# Use pytest if available
./scripts/run_tests.sh --pytest

# Run specific tests
./scripts/run_tests.sh --specific password

# Clean old reports
./scripts/run_tests.sh --clean

# Show help
./scripts/run_tests.sh --help
```

**Options**:
- `-a, --all`: Run all tests (default)
- `-p, --pytest`: Use pytest runner if available
- `-s, --specific`: Run tests matching pattern
- `-c, --clean`: Clean old test reports
- `-h, --help`: Show usage information

### `demo.sh`
**Purpose**: Interactive demonstration of all features

**Features**:
- ✅ Guided feature demonstration
- ✅ Interactive menu system
- ✅ Real-time password analysis
- ✅ Educational examples
- ✅ PDF generation demo
- ✅ Best practices showcase

**Usage**:
```bash
# Interactive menu (default)
./scripts/demo.sh

# Run complete demo
./scripts/demo.sh --full

# Show menu options
./scripts/demo.sh --menu
```

**Demo Sections**:
1. **Introduction**: Overview of features
2. **Very Weak Passwords**: Common security failures
3. **Weak Passwords**: Basic improvements
4. **Name Detection**: Personal information risks
5. **Strong Passwords**: Good security practices
6. **Very Strong Passwords**: Excellent security
7. **Interactive Mode**: User testing
8. **PDF Generation**: Report creation

## Script Capabilities

### Environment Setup
- **Dependency Management**: Handles both Poetry and pip workflows
- **Development Tools**: Sets up VS Code configuration
- **Verification**: Tests installation integrity
- **Cross-platform**: Works on Linux, macOS, and Windows (with bash)

### Test Execution
- **Comprehensive Testing**: Runs all unit tests
- **Report Generation**: Creates timestamped test reports
- **Flexible Execution**: Supports different test runners
- **Pattern Matching**: Run specific test categories

### Demonstration
- **Educational Content**: Shows security concepts
- **Real Examples**: Demonstrates actual password analysis
- **Interactive Learning**: Hands-on testing experience
- **Best Practices**: Security guideline examples

## Making Scripts Executable

### Linux/macOS
```bash
chmod +x scripts/*.sh
```

### Windows (Git Bash/WSL)
```bash
# Git Bash
chmod +x scripts/*.sh

# Or run with bash directly
bash scripts/setup.sh
```

## Script Dependencies

### System Requirements
- **Bash**: Version 4.0+ recommended
- **Python**: 3.10+ (verified by setup script)
- **Standard Tools**: grep, awk, find, curl

### Optional Tools
- **Poetry**: For advanced dependency management
- **pytest**: For enhanced test reporting
- **VS Code**: For development environment setup

## Customization

### Modifying Setup
Edit `setup.sh` to customize:
- Python version requirements
- Additional development tools
- Custom VS Code settings
- Additional verification steps

### Test Configuration
Edit `run_tests.sh` to modify:
- Test file patterns
- Report retention policy
- Output formatting
- Test execution order

### Demo Content
Edit `demo.sh` to customize:
- Example passwords
- Demonstration flow
- Educational content
- Interactive elements

## Troubleshooting

### Common Issues

#### Permission Denied
```bash
chmod +x scripts/script_name.sh
```

#### Python Not Found
```bash
# Install Python 3.10+ from python.org
# Or use package manager:
sudo apt install python3.10  # Ubuntu
brew install python@3.10     # macOS
```

#### Poetry Installation Fails
```bash
# Use pip fallback in setup script
# Or install Poetry manually:
curl -sSL https://install.python-poetry.org | python3 -
```

#### Test Reports Not Generated
```bash
# Check permissions
mkdir -p test_reports
chmod 755 test_reports
```

### Debug Mode
Enable verbose output in scripts:
```bash
# Add to beginning of script
set -x  # Enable debug mode
```

### Log Files
Scripts generate logs in:
- `test_reports/`: Test execution reports
- `.vscode/`: Development environment settings
- `examples/`: Generated example files

## Integration with CI/CD

### GitHub Actions Example
```yaml
- name: Setup Environment
  run: ./scripts/setup.sh

- name: Run Tests
  run: ./scripts/run_tests.sh --pytest
```

### Development Workflow
1. **Initial Setup**: Run `setup.sh` once
2. **Regular Testing**: Use `run_tests.sh` before commits
3. **Feature Demo**: Use `demo.sh` for presentations
4. **Documentation**: Update scripts with new features

## Contributing to Scripts

### Adding New Scripts
1. Follow naming convention: `action_name.sh`
2. Include help/usage functions
3. Add error handling with `set -e`
4. Use consistent output formatting
5. Document in this README

### Script Standards
- **Error Handling**: Exit on errors, provide meaningful messages
- **User Feedback**: Clear progress indicators and results
- **Flexibility**: Support multiple execution modes
- **Documentation**: Include usage examples and options

### Testing Scripts
Test scripts on multiple platforms:
- Linux (Ubuntu, CentOS)
- macOS (with Homebrew)
- Windows (Git Bash, WSL)

Remember: These scripts are part of the development workflow and should be maintained alongside the main application code.
