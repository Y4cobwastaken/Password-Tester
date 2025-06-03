#!/bin/bash

# Password Strength Tester - Test Runner Script
# Runs all tests with comprehensive reporting

set -e  # Exit on any error

echo "🧪 Password Strength Tester - Test Runner"
echo "========================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Test configuration
TEST_DIR="tests"
REPORTS_DIR="test_reports"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create reports directory
mkdir -p "$REPORTS_DIR"

# Function to print colored output
print_color() {
    printf "${1}%s${NC}\n" "$2"
}

# Function to check if test files exist
check_test_files() {
    print_color $BLUE "📋 Checking test files..."
    
    if [ ! -d "$TEST_DIR" ]; then
        print_color $RED "❌ Tests directory not found: $TEST_DIR"
        exit 1
    fi
    
    test_files=(
        "$TEST_DIR/test_password_analysis.py"
        "$TEST_DIR/test_report_generation.py"
    )
    
    for file in "${test_files[@]}"; do
        if [ -f "$file" ]; then
            print_color $GREEN "✅ Found: $file"
        else
            print_color $YELLOW "⚠️ Missing: $file"
        fi
    done
}

# Function to run individual test file
run_test_file() {
    local test_file=$1
    local test_name=$(basename "$test_file" .py)
    
    print_color $BLUE "🔬 Running $test_name..."
    
    # Create individual report file
    local report_file="$REPORTS_DIR/${test_name}_${TIMESTAMP}.txt"
    
    if python3 "$test_file" > "$report_file" 2>&1; then
        print_color $GREEN "✅ $test_name passed"
        
        # Extract summary from report
        if grep -q "All tests passed" "$report_file"; then
            local test_count=$(grep "Tests run:" "$report_file" | awk '{print $3}')
            print_color $GREEN "   → $test_count tests completed successfully"
        fi
        
        return 0
    else
        print_color $RED "❌ $test_name failed"
        
        # Show error summary
        echo "   Error details in: $report_file"
        tail -n 10 "$report_file" | sed 's/^/   /'
        
        return 1
    fi
}

# Function to run all tests
run_all_tests() {
    print_color $BLUE "🚀 Running all tests..."
    
    local total_tests=0
    local passed_tests=0
    local failed_tests=0
    
    # Test files to run
    test_files=(
        "$TEST_DIR/test_password_analysis.py"
        "$TEST_DIR/test_report_generation.py"
    )
    
    # Run each test file
    for test_file in "${test_files[@]}"; do
        if [ -f "$test_file" ]; then
            ((total_tests++))
            
            if run_test_file "$test_file"; then
                ((passed_tests++))
            else
                ((failed_tests++))
            fi
            
            echo # Empty line for readability
        else
            print_color $YELLOW "⚠️ Skipping missing test file: $test_file"
        fi
    done
    
    # Print summary
    echo "=" * 50
    print_color $BLUE "📊 Test Summary"
    echo "  Total test files: $total_tests"
    print_color $GREEN "  Passed: $passed_tests"
    print_color $RED "  Failed: $failed_tests"
    
    # Overall result
    if [ $failed_tests -eq 0 ]; then
        print_color $GREEN "🎉 All tests passed!"
        return 0
    else
        print_color $RED "💥 Some tests failed!"
        return 1
    fi
}

# Function to run with pytest if available
run_with_pytest() {
    print_color $BLUE "🔬 Running tests with pytest..."
    
    if command -v pytest &> /dev/null; then
        local report_file="$REPORTS_DIR/pytest_report_${TIMESTAMP}.txt"
        
        # Run pytest with detailed output
        if pytest "$TEST_DIR" -v --tb=short > "$report_file" 2>&1; then
            print_color $GREEN "✅ pytest completed successfully"
            
            # Show summary
            grep -E "(PASSED|FAILED|ERROR)" "$report_file" | tail -n 5
            
            return 0
        else
            print_color $RED "❌ pytest found issues"
            echo "Full report in: $report_file"
            return 1
        fi
    else
        print_color $YELLOW "⚠️ pytest not available, using standard test runner"
        return 1
    fi
}

# Function to run specific test
run_specific_test() {
    local test_pattern=$1
    
    print_color $BLUE "🎯 Running tests matching: $test_pattern"
    
    # Find matching test files
    matching_files=$(find "$TEST_DIR" -name "*${test_pattern}*" -type f)
    
    if [ -z "$matching_files" ]; then
        print_color $RED "❌ No test files found matching: $test_pattern"
        exit 1
    fi
    
    # Run matching tests
    for file in $matching_files; do
        run_test_file "$file"
    done
}

# Function to clean old reports
clean_reports() {
    print_color $BLUE "🧹 Cleaning old test reports..."
    
    if [ -d "$REPORTS_DIR" ]; then
        # Keep only last 10 reports
        if ls "$REPORTS_DIR"/*.txt 1> /dev/null 2>&1; then
            local report_count=$(ls "$REPORTS_DIR"/*.txt | wc -l)
            
            if [ "$report_count" -gt 10 ]; then
                ls -t "$REPORTS_DIR"/*.txt | tail -n +11 | xargs rm -f
                print_color $GREEN "✅ Cleaned old reports (kept 10 most recent)"
            else
                print_color $GREEN "✅ No cleanup needed ($report_count reports)"
            fi
        else
            print_color $GREEN "✅ No reports to clean"
        fi
    fi
}

# Function to show usage
show_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo
    echo "Options:"
    echo "  -a, --all         Run all tests (default)"
    echo "  -p, --pytest      Use pytest runner if available"
    echo "  -s, --specific    Run specific test (e.g., password_analysis)"
    echo "  -c, --clean       Clean old test reports"
    echo "  -h, --help        Show this help message"
    echo
    echo "Examples:"
    echo "  $0                    # Run all tests"
    echo "  $0 --pytest          # Run with pytest"
    echo "  $0 -s password        # Run password-related tests"
    echo "  $0 --clean           # Clean old reports"
}

# Main function
main() {
    case "${1:-}" in
        -h|--help)
            show_usage
            exit 0
            ;;
        -c|--clean)
            clean_reports
            exit 0
            ;;
        -p|--pytest)
            check_test_files
            run_with_pytest || run_all_tests
            ;;
        -s|--specific)
            if [ -z "$2" ]; then
                print_color $RED "❌ Please specify test pattern"
                show_usage
                exit 1
            fi
            check_test_files
            run_specific_test "$2"
            ;;
        -a|--all|"")
            check_test_files
            run_all_tests
            ;;
        *)
            print_color $RED "❌ Unknown option: $1"
            show_usage
            exit 1
            ;;
    esac
}

# Cleanup on exit
cleanup() {
    echo
    print_color $BLUE "📁 Test reports saved in: $REPORTS_DIR"
}

trap cleanup EXIT

# Run main function with all arguments
main "$@"
