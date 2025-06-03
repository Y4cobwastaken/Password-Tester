
#!/bin/bash

# Password Strength Tester - Setup Script
# This script sets up the development environment and dependencies

set -e  # Exit on any error

echo "🔐 Password Strength Tester - Setup Script"
echo "=========================================="

# Check if Python is installed
check_python() {
    echo "📋 Checking Python installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        echo "✅ Python $PYTHON_VERSION found"
        
        # Check if version is 3.10+
        if python3 -c "import sys; exit(0 if sys.version_info >= (3, 10) else 1)"; then
            echo "✅ Python version meets requirements (3.10+)"
        else
            echo "❌ Python 3.10+ required, found $PYTHON_VERSION"
            exit 1
        fi
    else
        echo "❌ Python 3 not found. Please install Python 3.10+ from https://python.org"
        exit 1
    fi
}

# Check if Poetry is installed
check_poetry() {
    echo "📋 Checking Poetry installation..."
    
    if command -v poetry &> /dev/null; then
        POETRY_VERSION=$(poetry --version 2>&1 | awk '{print $3}')
        echo "✅ Poetry $POETRY_VERSION found"
        return 0
    else
        echo "⚠️ Poetry not found"
        return 1
    fi
}

# Install Poetry
install_poetry() {
    echo "📦 Installing Poetry..."
    
    # Install Poetry using the official installer
    curl -sSL https://install.python-poetry.org | python3 -
    
    # Add Poetry to PATH for current session
    export PATH="$HOME/.local/bin:$PATH"
    
    if command -v poetry &> /dev/null; then
        echo "✅ Poetry installed successfully"
    else
        echo "❌ Poetry installation failed"
        echo "Please add Poetry to your PATH or restart your terminal"
        exit 1
    fi
}

# Install dependencies with Poetry
install_dependencies_poetry() {
    echo "📦 Installing dependencies with Poetry..."
    
    if [ -f "pyproject.toml" ]; then
        poetry install
        echo "✅ Dependencies installed with Poetry"
    else
        echo "❌ pyproject.toml not found"
        exit 1
    fi
}

# Install dependencies with pip (fallback)
install_dependencies_pip() {
    echo "📦 Installing dependencies with pip..."
    
    if [ -f "requirements.txt" ]; then
        python3 -m pip install --user -r requirements.txt
        echo "✅ Dependencies installed with pip"
    else
        echo "❌ requirements.txt not found"
        exit 1
    fi
}

# Set up development tools
setup_dev_tools() {
    echo "🛠️ Setting up development tools..."
    
    # Create .vscode directory if it doesn't exist
    if [ ! -d ".vscode" ]; then
        mkdir -p .vscode
        
        # Create basic VS Code settings
        cat > .vscode/settings.json << EOF
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.testing.unittestEnabled": true,
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests",
        "-p",
        "test_*.py"
    ]
}
EOF
        echo "✅ VS Code settings created"
    fi
    
    # Make scripts executable
    chmod +x scripts/*.sh 2>/dev/null || true
    echo "✅ Scripts made executable"
}

# Verify installation
verify_installation() {
    echo "🧪 Verifying installation..."
    
    # Test basic import
    if python3 -c "import reportlab" &> /dev/null; then
        echo "✅ Dependencies import successfully"
    else
        echo "❌ Dependency import failed"
        exit 1
    fi
    
    # Test main application
    if python3 -c "from main import analyze_password_strength; print('Import test passed')" &> /dev/null; then
        echo "✅ Main application imports successfully"
    else
        echo "❌ Main application import failed"
        exit 1
    fi
    
    # Run quick tests if available
    if [ -f "tests/test_password_analysis.py" ]; then
        echo "🧪 Running quick tests..."
        if python3 tests/test_password_analysis.py &> /dev/null; then
            echo "✅ Basic tests pass"
        else
            echo "⚠️ Some tests failed (this may be normal during development)"
        fi
    fi
}

# Create example environment
create_examples() {
    echo "📝 Setting up examples..."
    
    # Ensure examples directory exists
    mkdir -p examples
    
    # Create quick test script if it doesn't exist
    if [ ! -f "examples/quick_test.py" ]; then
        cat > examples/quick_test.py << 'EOF'
#!/usr/bin/env python3
"""Quick test script to verify installation"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import analyze_password_strength

def quick_test():
    print("🚀 Quick Installation Test")
    print("-" * 25)
    
    test_password = "TestPassword123!"
    score, feedback, strength = analyze_password_strength(test_password)
    
    print(f"Password: {test_password}")
    print(f"Score: {score}/10")
    print(f"Strength: {strength}")
    print("✅ Installation verified!")

if __name__ == "__main__":
    quick_test()
EOF
        chmod +x examples/quick_test.py
        echo "✅ Quick test script created"
    fi
}

# Main setup function
main() {
    echo "Starting setup process..."
    echo
    
    # Check prerequisites
    check_python
    
    # Handle Poetry installation and dependencies
    if check_poetry; then
        install_dependencies_poetry
    else
        echo "Would you like to install Poetry? (recommended) [y/N]"
        read -r response
        if [[ "$response" =~ ^[Yy]$ ]]; then
            install_poetry
            install_dependencies_poetry
        else
            echo "Using pip for dependency installation..."
            install_dependencies_pip
        fi
    fi
    
    # Set up development environment
    setup_dev_tools
    create_examples
    
    # Verify everything works
    verify_installation
    
    echo
    echo "🎉 Setup completed successfully!"
    echo
    echo "Next steps:"
    echo "1. Run the application: python main.py"
    echo "2. Run tests: python tests/test_password_analysis.py"
    echo "3. Try the demo: python examples/demo_script.py"
    echo "4. Quick test: python examples/quick_test.py"
    echo
    echo "For more information, see README.md"
}

# Run main function
main "$@"
