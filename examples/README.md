# Examples

This directory contains examples and demonstrations of the Password Strength Tester.

## Files

### `sample_passwords.txt`
A collection of sample passwords organized by strength level:
- Very Weak passwords (common patterns)
- Weak passwords (basic improvements)
- Moderate passwords (some complexity)
- Strong passwords (good security)
- Very Strong passwords (excellent security)
- Bad examples (names, patterns)

**⚠️ WARNING**: These are example passwords for testing only. Never use these as real passwords!

### `demo_script.py`
Interactive demonstration script that showcases:
- Password strength analysis across different security levels
- Name detection functionality
- Crack time estimation
- Character composition analysis

## Running the Examples

### Basic Demo
```bash
python examples/demo_script.py
```

### Testing with Sample Passwords
Use the sample passwords from `sample_passwords.txt` with the main application:

```bash
python main.py
```

Then copy passwords from the sample file to test different scenarios.

### Manual Testing Examples

#### Test Weak Password
```
Enter password: password123
```
Expected: Weak rating, missing uppercase/special chars

#### Test Name Detection
```
Enter password: John2024!
```
Expected: Detection of name "John" in feedback

#### Test Strong Password
```
Enter password: MySecure#Pass2024!
```
Expected: Strong or Very Strong rating

## What Each Example Demonstrates

### Very Weak Examples
- **Purpose**: Show passwords that fail basic security requirements
- **Learning**: Understand minimum security standards
- **Common Issues**: Too short, common patterns, dictionary words

### Weak Examples
- **Purpose**: Passwords with some improvements but still vulnerable
- **Learning**: See incremental security improvements
- **Common Issues**: Missing character types, predictable patterns

### Moderate Examples
- **Purpose**: Passwords meeting basic requirements
- **Learning**: Understand baseline security expectations
- **Characteristics**: Multiple character types, reasonable length

### Strong Examples
- **Purpose**: Passwords with good security practices
- **Learning**: See effective password construction
- **Characteristics**: Length, complexity, unpredictability

### Very Strong Examples
- **Purpose**: Demonstrate excellent password security
- **Learning**: Understand optimal password practices
- **Characteristics**: Long, complex, unique patterns

## Educational Use Cases

### For Security Training
1. Show progression from weak to strong passwords
2. Demonstrate impact of different security measures
3. Illustrate real-world attack resistance

### For Development Testing
1. Test edge cases and boundary conditions
2. Validate scoring algorithm accuracy
3. Ensure consistent analysis results

### For Security Audits
1. Benchmark against known password standards
2. Compare organizational passwords against examples
3. Identify common password weaknesses

## Contributing Examples

When adding new examples:
1. Ensure they demonstrate specific security concepts
2. Include clear categorization by strength level
3. Add explanatory comments for educational value
4. Never include real passwords or personal information

## Security Notes

- All examples are publicly available and should never be used as real passwords
- Examples are designed for educational and testing purposes only
- Some examples intentionally demonstrate poor security practices
- Always follow your organization's password policies for real accounts
