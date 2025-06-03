# Usage Examples

## Basic Password Testing

### Example 1: Weak Password
```bash
Enter password to test: password123

📊 Password Analysis Results
------------------------------
Password Length: 11 characters
Strength Score: 4/10
Strength Level: Weak
Estimated Crack Time: 12.34 hours

📝 Detailed Analysis:
  ⚠️ Short length (11 chars) - consider 12+ characters
  ✅ Contains lowercase letters
  ❌ Missing uppercase letters
  ✅ Contains numbers
  ❌ Missing special characters
  ✅ No repetitive characters
  ⚠️ Contains common patterns
  ✅ No common names detected

💡 Suggestions for improvement:
  • Add uppercase letters (A-Z)
  • Add special characters (!@#$%^&*)
  • Use at least 12-16 characters
  • Avoid common patterns like '123', 'abc', 'qwerty'
```

### Example 2: Strong Password
```bash
Enter password to test: MySecure#Pass2024!

📊 Password Analysis Results
------------------------------
Password Length: 17 characters
Strength Score: 10/10
Strength Level: Very Strong
Estimated Crack Time: 4.56e+28 years

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
```

### Example 3: Password with Names
```bash
Enter password to test: John2024!

📊 Password Analysis Results
------------------------------
Password Length: 9 characters
Strength Score: 5/10
Strength Level: Weak
Estimated Crack Time: 2.1 minutes

📝 Detailed Analysis:
  ⚠️ Short length (9 chars) - consider 12+ characters
  ✅ Contains lowercase letters
  ✅ Contains uppercase letters
  ✅ Contains numbers
  ✅ Contains special characters
  ✅ No repetitive characters
  ✅ No common patterns detected
  ❌ Contains potential names: John

💡 Suggestions for improvement:
  • Use at least 12-16 characters
  • Avoid using names or personal information
```

## PDF Report Generation

When you choose to generate a PDF report, the system creates a comprehensive document including:

### Report Sections:
1. **Analysis Summary Table**
   - Report timestamp
   - Password length
   - Strength score and level
   - Estimated crack time

2. **Character Composition Analysis**
   - Breakdown by character type
   - Count of each category

3. **Detailed Security Analysis**
   - All feedback points
   - Security warnings and confirmations

4. **Improvement Recommendations**
   - Specific suggestions based on weaknesses
   - Actionable improvement steps

5. **General Security Best Practices**
   - Industry-standard security guidelines
   - Additional security measures

### Example PDF Generation:
```bash
📄 Would you like to generate a PDF report? (y/n): y
✅ PDF report generated successfully: password_analysis_report_20241201_143052.pdf
```

## Common Password Patterns to Avoid

### Sequential Patterns
- `123456789` - Number sequences
- `abcdefgh` - Letter sequences
- `qwertyuiop` - Keyboard patterns

### Dictionary Words
- `password` - Common words
- `admin` - System terms
- `login` - Access-related terms

### Personal Information
- Names: `john`, `mary`, `michael`
- Dates: `1990`, `2024`
- Common substitutions: `@` for `a`, `3` for `e`

## Best Practices Demonstrated

### Good Password Examples:
- `Tr0ub4dor&3` - Mix of cases, numbers, symbols
- `correct#horse$battery9` - Passphrase with symbols
- `MyF@v0rite_B00k_2024!` - Personal but complex

### Password Improvement Process:
1. Start with a base phrase
2. Add uppercase letters
3. Include numbers
4. Add special characters
5. Ensure adequate length (12+ chars)
6. Avoid personal information
7. Test with this tool!

## Command Line Tips

- Type `quit` to exit the program
- Press Enter without typing to skip empty passwords
- Generate PDF reports for record-keeping
- Test multiple variations to find the strongest option
