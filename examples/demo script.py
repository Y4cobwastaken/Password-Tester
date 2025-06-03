#!/usr/bin/env python3
"""
Demo script for Password Strength Tester
Demonstrates all features and capabilities
"""

import sys
import os

# Add parent directory to path to import main module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import analyze_password_strength, estimate_crack_time, detect_names_in_password, generate_pdf_report, get_password_suggestions

def demo_password_analysis():
    """Demonstrate password analysis with various examples"""
    
    print("🔐 Password Strength Tester - Demo Script")
    print("=" * 50)
    
    # Sample passwords with different strength levels
    test_passwords = [
        ("123456", "Very Weak - Common pattern"),
        ("password123", "Weak - Dictionary word with numbers"),
        ("John2024!", "Moderate - Contains name"),
        ("MySecure#Pass2024!", "Strong - Good complexity"),
        ("Th3_Qu1ck_Br0wn_F0x_Jump5!", "Very Strong - Excellent security")
    ]
    
    for password, description in test_passwords:
        print(f"\n📝 Testing: {description}")
        print("-" * 40)
        print(f"Password: {'*' * len(password)} (length: {len(password)})")
        
        # Analyze the password
        score, feedback, strength = analyze_password_strength(password)
        crack_time = estimate_crack_time(password)
        detected_names = detect_names_in_password(password)
        suggestions = get_password_suggestions(feedback)
        
        # Display results
        print(f"Strength Score: {score}/10")
        print(f"Strength Level: {strength}")
        print(f"Crack Time: {crack_time}")
        
        if detected_names:
            print(f"Detected Names: {', '.join(detected_names)}")
        
        print("Analysis Points:")
        for item in feedback:
            print(f"  {item}")
        
        if suggestions:
            print("Suggestions:")
            for suggestion in suggestions:
                print(f"  {suggestion}")
        
        print("-" * 40)

def demo_name_detection():
    """Demonstrate name detection feature"""
    
    print("\n🎭 Name Detection Demo")
    print("=" * 30)
    
    test_cases = [
        "john123",
        "MaryPassword",
        "david2024!",
        "SecurePass123",
        "sarah_admin",
        "NoNamesHere!"
    ]
    
    for password in test_cases:
        names = detect_names_in_password(password)
        if names:
            print(f"'{password}' contains names: {', '.join(names)}")
        else:
            print(f"'{password}' contains no detected names")

def demo_crack_time_estimation():
    """Demonstrate crack time estimation"""
    
    print("\n⏱️ Crack Time Estimation Demo")
    print("=" * 35)
    
    test_passwords = [
        "abc",
        "password",
        "Password1",
        "P@ssw0rd!",
        "MyVeryLongAndComplexPassword123!"
    ]
    
    for password in test_passwords:
        crack_time = estimate_crack_time(password)
        print(f"'{password}' ({len(password)} chars) - Estimated crack time: {crack_time}")

def demo_character_analysis():
    """Demonstrate character composition analysis"""
    
    print("\n🔍 Character Analysis Demo")
    print("=" * 32)
    
    import re
    import string
    
    test_password = "MySecure#Pass2024!"
    
    print(f"Analyzing password: {test_password}")
    print(f"Length: {len(test_password)} characters")
    
    # Character breakdown
    lowercase_count = len(re.findall(r'[a-z]', test_password))
    uppercase_count = len(re.findall(r'[A-Z]', test_password))
    digit_count = len(re.findall(r'\d', test_password))
    special_chars = string.punctuation + ' '
    special_count = sum(1 for char in test_password if char in special_chars)
    
    print(f"Lowercase letters: {lowercase_count}")
    print(f"Uppercase letters: {uppercase_count}")
    print(f"Digits: {digit_count}")
    print(f"Special characters: {special_count}")
    
    # Character set size calculation
    char_set_size = 0
    if lowercase_count > 0:
        char_set_size += 26
    if uppercase_count > 0:
        char_set_size += 26
    if digit_count > 0:
        char_set_size += 10
    if special_count > 0:
        char_set_size += len(special_chars)
    
    print(f"Total character set size: {char_set_size}")
    print(f"Possible combinations: {char_set_size ** len(test_password):.2e}")

def main():
    """Run all demonstrations"""
    
    try:
        demo_password_analysis()
        demo_name_detection()
        demo_crack_time_estimation()
        demo_character_analysis()
        
        print("\n✅ Demo completed successfully!")
        print("\nTo test the PDF generation feature, run the main application:")
        print("python main.py")
        
    except Exception as e:
        print(f"❌ Demo failed with error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
