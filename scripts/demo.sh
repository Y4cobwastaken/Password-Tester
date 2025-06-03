#!/bin/bash

# Password Strength Tester - Demo Script
# Interactive demonstration of all features

set -e  # Exit on any error

echo "🔐 Password Strength Tester - Interactive Demo"
echo "============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print colored output
print_color() {
    printf "${1}%s${NC}\n" "$2"
}

# Function to wait for user input
wait_for_user() {
    echo
    print_color $CYAN "Press Enter to continue..."
    read -r
}

# Function to run password test
test_password() {
    local password=$1
    local description=$2
    
    print_color $BLUE "🔍 Testing: $description"
    print_color $YELLOW "Password: $password"
    echo
    
    # Run the analysis
    python3 -c "
import sys
import os
sys.path.append('.')
from main import analyze_password_strength, estimate_crack_time, detect_names_in_password

password = '$password'
score, feedback, strength = analyze_password_strength(password)
crack_time = estimate_crack_time(password)
names = detect_names_in_password(password)

print(f'📊 Results:')
print(f'  Length: {len(password)} characters')
print(f'  Score: {score}/10')
print(f'  Strength: {strength}')
print(f'  Crack Time: {crack_time}')

if names:
    print(f'  Names Detected: {', '.join(names)}')

print(f'\\n📝 Analysis:')
for item in feedback:
    print(f'  {item}')
"
}

# Function to demonstrate features
demo_introduction() {
    clear
    print_color $GREEN "Welcome to the Password Strength Tester Demo!"
    echo
    print_color $BLUE "This tool analyzes password security and provides:"
    echo "  ✅ Comprehensive strength scoring (0-10 points)"
    echo "  ✅ Character composition analysis"
    echo "  ✅ Common pattern detection"
    echo "  ✅ Name detection in passwords"
    echo "  ✅ Crack time estimation"
    echo "  ✅ PDF report generation"
    echo "  ✅ Improvement suggestions"
    
    wait_for_user
}

# Demo very weak passwords
demo_very_weak() {
    clear
    print_color $RED "Demo 1: Very Weak Passwords"
    print_color $RED "============================"
    echo
    print_color $YELLOW "These passwords fail basic security requirements:"
    echo
    
    test_password "123456" "Common number sequence"
    wait_for_user
    
    test_password "password" "Dictionary word"
    wait_for_user
    
    test_password "abc" "Too short"
    wait_for_user
}

# Demo weak passwords
demo_weak() {
    clear
    print_color $YELLOW "Demo 2: Weak Passwords"
    print_color $YELLOW "======================"
    echo
    print_color $YELLOW "These passwords have some improvements but remain vulnerable:"
    echo
    
    test_password "password123" "Dictionary word + numbers"
    wait_for_user
    
    test_password "admin2024" "Common word + year"
    wait_for_user
    
    test_password "qwerty123" "Keyboard pattern + numbers"
    wait_for_user
}

# Demo name detection
demo_names() {
    clear
    print_color $CYAN "Demo 3: Name Detection"
    print_color $CYAN "====================="
    echo
    print_color $YELLOW "The tool detects common names in passwords (security risk):"
    echo
    
    test_password "John2024!" "Contains common name"
    wait_for_user
    
    test_password "MaryPassword" "Name + common word"
    wait_for_user
    
    test_password "david123!" "Lowercase name"
    wait_for_user
    
    test_password "SecurePass123" "No names detected"
    wait_for_user
}

# Demo strong passwords
demo_strong() {
    clear
    print_color $GREEN "Demo 4: Strong Passwords"
    print_color $GREEN "========================"
    echo
    print_color $YELLOW "These passwords demonstrate good security practices:"
    echo
    
    test_password "MySecure#Pass2024!" "Good complexity and length"
    wait_for_user
    
    test_password "Tr0ub4dor&3" "Creative substitutions"
    wait_for_user
    
    test_password "correct#horse\$battery9" "Passphrase with symbols"
    wait_for_user
}

# Demo very strong passwords
demo_very_strong() {
    clear
    print_color $GREEN "Demo 5: Very Strong Passwords"
    print_color $GREEN "============================="
    echo
    print_color $YELLOW "These passwords represent excellent security:"
    echo
    
    test_password "Th3_Qu1ck_Br0wn_F0x_Jump5!" "Long passphrase with complexity"
    wait_for_user
    
    test_password "MyUltr@Secure\$P@ssw0rd#2024" "Maximum complexity"
    wait_for_user
    
    test_password "Ungu3ss@ble_P@ssw0rd_W1th_L3ngth!" "Excellent length and variety"
    wait_for_user
}

# Demo interactive mode
demo_interactive() {
    clear
    print_color $BLUE "Demo 6: Interactive Mode"
    print_color $BLUE "========================"
    echo
    print_color $YELLOW "Now you can test your own passwords!"
    print_color $CYAN "Try entering different passwords to see how they score."
    print_color $RED "Note: Never use real passwords in shared environments!"
    echo
    
    print_color $GREEN "Starting interactive mode..."
    wait_for_user
    
    # Run the main application
    python3 main.py
}

# Demo PDF generation
demo_pdf() {
    clear
    print_color $BLUE "Demo 7: PDF Report Generation"
    print_color $BLUE "============================="
    echo
    print_color $YELLOW "The tool can generate detailed PDF reports."
    print_color $CYAN "Let's create a sample report..."
    echo
    
    # Create a sample PDF report
    python3 -c "
import sys
import os
sys.path.append('.')
from main import analyze_password_strength, estimate_crack_time, get_password_suggestions, generate_pdf_report

password = 'DemoPassword123!'
score, feedback, strength = analyze_password_strength(password)
crack_time = estimate_crack_time(password)
suggestions = get_password_suggestions(feedback)

print(f'Generating PDF report for: {password}')
print(f'Score: {score}/10, Strength: {strength}')

try:
    filename = generate_pdf_report(password, score, feedback, strength, crack_time, suggestions)
    print(f'✅ PDF report generated: {filename}')
    print('The report includes:')
    print('  • Security analysis summary')
    print('  • Character composition breakdown')
    print('  • Detailed feedback')
    print('  • Improvement suggestions')
    print('  • Security best practices')
except Exception as e:
    print(f'❌ Error generating PDF: {e}')
"
    
    wait_for_user
}

# Demo conclusion
demo_conclusion() {
    clear
    print_color $GREEN "Demo Complete!"
    print_color $GREEN "=============="
    echo
    print_color $BLUE "You've seen all the key features:"
    echo "  🔍 Password strength analysis"
    echo "  🎭 Name detection"
    echo "  ⏱️ Crack time estimation"
    echo "  📄 PDF report generation"
    echo "  💡 Improvement suggestions"
    echo
    print_color $YELLOW "Best Practices Demonstrated:"
    echo "  • Use 12+ characters"
    echo "  • Mix uppercase, lowercase, numbers, symbols"
    echo "  • Avoid names and personal information"
    echo "  • Avoid common patterns and dictionary words"
    echo "  • Use unique passwords for each account"
    echo
    print_color $CYAN "To use the tool:"
    echo "  python main.py              # Interactive mode"
    echo "  python examples/demo_script.py  # Automated demo"
    echo "  python tests/test_*.py      # Run tests"
    echo
    print_color $GREEN "Thank you for trying the Password Strength Tester!"
}

# Function to show demo menu
show_menu() {
    clear
    print_color $CYAN "🔐 Password Strength Tester Demo Menu"
    print_color $CYAN "===================================="
    echo
    echo "1. Introduction"
    echo "2. Very Weak Passwords"
    echo "3. Weak Passwords"
    echo "4. Name Detection"
    echo "5. Strong Passwords"
    echo "6. Very Strong Passwords"
    echo "7. Interactive Mode"
    echo "8. PDF Generation"
    echo "9. Run Full Demo"
    echo "0. Exit"
    echo
    print_color $YELLOW "Enter your choice (0-9): "
}

# Interactive menu
interactive_menu() {
    while true; do
        show_menu
        read -r choice
        
        case $choice in
            1) demo_introduction ;;
            2) demo_very_weak ;;
            3) demo_weak ;;
            4) demo_names ;;
            5) demo_strong ;;
            6) demo_very_strong ;;
            7) demo_interactive ;;
            8) demo_pdf ;;
            9) run_full_demo ;;
            0) 
                print_color $GREEN "Thanks for using the demo!"
                exit 0
                ;;
            *)
                print_color $RED "Invalid choice. Please try again."
                sleep 2
                ;;
        esac
    done
}

# Run full demo
run_full_demo() {
    demo_introduction
    demo_very_weak
    demo_weak
    demo_names
    demo_strong
    demo_very_strong
    demo_pdf
    demo_conclusion
}

# Main function
main() {
    # Check if main.py exists
    if [ ! -f "main.py" ]; then
        print_color $RED "❌ main.py not found. Please run from project root directory."
        exit 1
    fi
    
    case "${1:-}" in
        --full)
            run_full_demo
            ;;
        --menu)
            interactive_menu
            ;;
        *)
            print_color $BLUE "Password Strength Tester Demo"
            echo
            echo "Usage:"
            echo "  $0           # Interactive menu"
            echo "  $0 --full    # Run complete demo"
            echo "  $0 --menu    # Show menu options"
            echo
            print_color $YELLOW "Starting interactive menu..."
            sleep 2
            interactive_menu
            ;;
    esac
}

# Run main function
main "$@"
