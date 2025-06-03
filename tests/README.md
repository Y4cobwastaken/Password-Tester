# Tests

This directory contains comprehensive unit tests for the Password Strength Tester application.

## Test Structure

### `test_password_analysis.py`
Tests core password analysis functionality:
- **TestPasswordAnalysis**: Main password strength scoring
- **TestNameDetection**: Name detection in passwords
- **TestCrackTimeEstimation**: Time estimation calculations
- **TestPasswordSuggestions**: Improvement suggestions

### `test_report_generation.py`
Tests PDF report generation:
- **TestReportGeneration**: PDF file creation and structure
- **TestReportContent**: Report content validation
- **MockReportTests**: Mocked component testing

## Running Tests

### Run All Tests
```bash
# From project root
python -m pytest tests/

# Or run individual test files
python tests/test_password_analysis.py
python tests/test_report_generation.py
```

### Run Specific Test Categories
```bash
# Run only password analysis tests
python -m pytest tests/test_password_analysis.py::TestPasswordAnalysis

# Run only name detection tests
python -m pytest tests/test_password_analysis.py::TestNameDetection

# Run only report generation tests
python -m pytest tests/test_report_generation.py::TestReportGeneration
```

### Verbose Output
```bash
python tests/test_password_analysis.py -v
```

## Test Coverage

### Password Analysis Tests
- ✅ Strength level classification (Very Weak to Very Strong)
- ✅ Length requirements and scoring
- ✅ Character variety validation
- ✅ Pattern detection (123, abc, qwerty, etc.)
- ✅ Repetitive character detection
- ✅ Scoring algorithm accuracy

### Name Detection Tests
- ✅ Common name identification
- ✅ Case-insensitive detection
- ✅ Names with numbers/symbols
- ✅ False positive prevention

### Crack Time Tests
- ✅ Character set size calculation
- ✅ Time estimation accuracy
- ✅ Different complexity levels
- ✅ Edge cases and boundary conditions

### Suggestion Tests
- ✅ Appropriate suggestions for weak passwords
- ✅ Minimal suggestions for strong passwords
- ✅ Specific improvement recommendations

### Report Generation Tests
- ✅ PDF file creation
- ✅ Filename uniqueness
- ✅ Content structure validation
- ✅ Special character handling
- ✅ Table and paragraph generation

## Test Data

### Sample Passwords Used
```python
# Very weak examples
["123", "abc", "pass", "1234567"]

# Weak examples
["password123", "admin2024", "qwerty123"]

# Strong examples
["MySecure#Pass2024!", "Tr0ub4dor&3"]

# Name detection examples
["john123", "MaryPassword", "david2024!"]
```

### Expected Outcomes
Each test validates:
- Correct strength classification
- Appropriate scoring ranges
- Accurate feedback messages
- Proper suggestion generation

## Mock Testing

PDF generation tests use mocking to:
- Avoid actual file creation during testing
- Test component integration
- Validate function calls and parameters
- Ensure error handling

## Test Utilities

### Custom Assertions
- Score range validation
- Strength level verification
- Feedback content checking
- Suggestion relevance testing

### Helper Functions
- Test data generation
- Mock setup and teardown
- Result validation
- Error simulation

## Adding New Tests

### For New Features
1. Create test cases in appropriate test file
2. Include positive and negative test cases
3. Test edge cases and boundary conditions
4. Validate error handling

### Test Naming Convention
```python
def test_feature_description(self):
    """Test specific aspect of functionality"""
    # Test implementation
```

### Test Organization
- Group related tests in test classes
- Use descriptive test method names
- Include docstrings explaining test purpose
- Follow AAA pattern (Arrange, Act, Assert)

## Continuous Testing

### Pre-commit Testing
Run tests before committing changes:
```bash
python tests/test_password_analysis.py && python tests/test_report_generation.py
```

### Integration Testing
Tests work together to validate:
- End-to-end password analysis workflow
- PDF generation with real analysis data
- Error handling across components

## Troubleshooting Tests

### Common Issues
- **Import errors**: Ensure parent directory is in Python path
- **Mock failures**: Check mock setup and expectations
- **File system tests**: Verify permissions and temp directory access

### Debug Mode
Add debug output to tests:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Performance Testing

While not included in unit tests, consider:
- Large password batch processing
- PDF generation performance
- Memory usage with complex reports
- Concurrent usage scenarios

## Security Testing Notes

Tests validate security-focused functionality:
- Password strength calculations
- Name detection accuracy
- Pattern recognition effectiveness
- Crack time estimation reliability

Remember: These tests help ensure the security tool works correctly, but they don't replace security audits of the tool itself.
