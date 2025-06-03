
#!/usr/bin/env python3
"""
Unit tests for password analysis functionality
"""

import unittest
import sys
import os

# Add parent directory to path to import main module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import analyze_password_strength, detect_names_in_password, estimate_crack_time, get_password_suggestions

class TestPasswordAnalysis(unittest.TestCase):
    """Test cases for password strength analysis"""
    
    def test_very_weak_passwords(self):
        """Test very weak password detection"""
        weak_passwords = ["123", "abc", "pass", "1234567"]
        
        for password in weak_passwords:
            score, feedback, strength = analyze_password_strength(password)
            self.assertLessEqual(score, 3, f"Password '{password}' should be very weak")
            self.assertEqual(strength, "Very Weak")
    
    def test_weak_passwords(self):
        """Test weak password detection"""
        weak_passwords = ["password123", "admin2024", "qwerty123"]
        
        for password in weak_passwords:
            score, feedback, strength = analyze_password_strength(password)
            self.assertLessEqual(score, 5, f"Password '{password}' should be weak or very weak")
            self.assertIn(strength, ["Very Weak", "Weak"])
    
    def test_strong_passwords(self):
        """Test strong password detection"""
        strong_passwords = [
            "MySecure#Pass2024!",
            "Tr0ub4dor&3",
            "SuperStr0ng&Secure#Password2024!"
        ]
        
        for password in strong_passwords:
            score, feedback, strength = analyze_password_strength(password)
            self.assertGreaterEqual(score, 8, f"Password '{password}' should be strong")
            self.assertIn(strength, ["Strong", "Very Strong"])
    
    def test_length_scoring(self):
        """Test password length scoring"""
        # Test short password
        score, _, _ = analyze_password_strength("Aa1!")
        self.assertEqual(score, 0, "Password under 8 chars should score 0")
        
        # Test medium length
        score, _, _ = analyze_password_strength("Aa1!Bb2@")
        self.assertGreater(score, 0, "8+ char password should score > 0")
        
        # Test long password
        score, _, _ = analyze_password_strength("MyVeryLongPassword123!")
        self.assertGreater(score, 5, "Long complex password should score well")
    
    def test_character_variety(self):
        """Test character variety scoring"""
        # Only lowercase
        score1, _, _ = analyze_password_strength("abcdefghij")
        
        # Add uppercase
        score2, _, _ = analyze_password_strength("Abcdefghij")
        self.assertGreater(score2, score1, "Adding uppercase should improve score")
        
        # Add numbers
        score3, _, _ = analyze_password_strength("Abcdefghi1")
        self.assertGreater(score3, score2, "Adding numbers should improve score")
        
        # Add special characters
        score4, _, _ = analyze_password_strength("Abcdefgh1!")
        self.assertGreater(score4, score3, "Adding special chars should improve score")
    
    def test_pattern_detection(self):
        """Test common pattern detection"""
        pattern_passwords = [
            "password123abc",
            "admin456qwerty",
            "test123sequence"
        ]
        
        for password in pattern_passwords:
            score, feedback, _ = analyze_password_strength(password)
            feedback_text = ' '.join(feedback)
            self.assertIn("common patterns", feedback_text.lower(),
                         f"Should detect patterns in '{password}'")
    
    def test_repetitive_characters(self):
        """Test repetitive character detection"""
        repetitive_password = "AAAbbbccc123"
        score, feedback, _ = analyze_password_strength(repetitive_password)
        feedback_text = ' '.join(feedback)
        self.assertIn("repetitive", feedback_text.lower(),
                     "Should detect repetitive characters")
        
        # Test non-repetitive
        normal_password = "AbC123def!"
        score, feedback, _ = analyze_password_strength(normal_password)
        feedback_text = ' '.join(feedback)
        self.assertIn("No repetitive", feedback_text,
                     "Should not flag non-repetitive password")

class TestNameDetection(unittest.TestCase):
    """Test cases for name detection functionality"""
    
    def test_common_name_detection(self):
        """Test detection of common names"""
        name_passwords = [
            ("john123", ["John"]),
            ("MaryPassword", ["Mary"]),
            ("david2024!", ["David"]),
            ("sarah_admin", ["Sarah"])
        ]
        
        for password, expected_names in name_passwords:
            detected = detect_names_in_password(password)
            for name in expected_names:
                self.assertIn(name, detected,
                             f"Should detect '{name}' in '{password}'")
    
    def test_no_names_detected(self):
        """Test passwords without names"""
        no_name_passwords = [
            "SecurePass123!",
            "MyPassword2024",
            "ComplexStr1ng!",
            "RandomText456@"
        ]
        
        for password in no_name_passwords:
            detected = detect_names_in_password(password)
            self.assertEqual(len(detected), 0,
                           f"Should not detect names in '{password}'")
    
    def test_case_insensitive_detection(self):
        """Test case insensitive name detection"""
        variations = ["JOHN123", "john123", "John123", "jOhN123"]
        
        for password in variations:
            detected = detect_names_in_password(password)
            self.assertIn("John", detected,
                         f"Should detect 'John' in '{password}' regardless of case")
    
    def test_names_with_attachments(self):
        """Test names with numbers and symbols"""
        attached_passwords = [
            "john123!",
            "mary@456",
            "david#2024"
        ]
        
        for password in attached_passwords:
            detected = detect_names_in_password(password)
            self.assertGreater(len(detected), 0,
                              f"Should detect names in '{password}' with attachments")

class TestCrackTimeEstimation(unittest.TestCase):
    """Test cases for crack time estimation"""
    
    def test_short_passwords(self):
        """Test crack time for short passwords"""
        short_password = "abc"
        crack_time = estimate_crack_time(short_password)
        self.assertIsInstance(crack_time, str, "Should return string estimate")
        # Short passwords should crack quickly
        self.assertTrue(any(unit in crack_time.lower() for unit in ["second", "minute"]),
                       "Short password should crack in seconds/minutes")
    
    def test_long_complex_passwords(self):
        """Test crack time for long complex passwords"""
        complex_password = "MyVeryLongAndComplexPassword123!@#"
        crack_time = estimate_crack_time(complex_password)
        self.assertIsInstance(crack_time, str, "Should return string estimate")
        # Complex passwords should take years
        self.assertIn("year", crack_time.lower(),
                     "Complex password should take years to crack")
    
    def test_different_character_sets(self):
        """Test crack time with different character sets"""
        passwords = [
            "lowercase",  # Only lowercase
            "Uppercase",  # Mixed case
            "Numbers123", # With numbers
            "Special!@#"  # With special chars
        ]
        
        times = []
        for password in passwords:
            time_str = estimate_crack_time(password)
            times.append(time_str)
        
        # Each should return a valid time estimate
        for time_estimate in times:
            self.assertIsInstance(time_estimate, str)
            self.assertNotEqual(time_estimate, "Unable to estimate")

class TestPasswordSuggestions(unittest.TestCase):
    """Test cases for password improvement suggestions"""
    
    def test_suggestions_for_weak_password(self):
        """Test suggestions for weak passwords"""
        weak_password = "pass"
        _, feedback, _ = analyze_password_strength(weak_password)
        suggestions = get_password_suggestions(feedback)
        
        self.assertGreater(len(suggestions), 0, "Should provide suggestions for weak password")
        
        # Check for common suggestions
        suggestion_text = ' '.join(suggestions)
        expected_suggestions = [
            "uppercase",
            "numbers",
            "special",
            "characters"
        ]
        
        for expected in expected_suggestions:
            self.assertIn(expected.lower(), suggestion_text.lower(),
                         f"Should suggest adding {expected}")
    
    def test_no_suggestions_for_strong_password(self):
        """Test no suggestions for strong passwords"""
        strong_password = "MyExcellentPassword123!@#"
        _, feedback, _ = analyze_password_strength(strong_password)
        suggestions = get_password_suggestions(feedback)
        
        # Strong passwords should have fewer or no suggestions
        self.assertLessEqual(len(suggestions), 2,
                            "Strong password should have minimal suggestions")
    
    def test_specific_suggestions(self):
        """Test specific suggestion types"""
        test_cases = [
            ("password", "uppercase"),  # Missing uppercase
            ("PASSWORD", "lowercase"),  # Missing lowercase
            ("Password", "numbers"),    # Missing numbers
            ("Password1", "special")    # Missing special chars
        ]
        
        for password, expected_suggestion in test_cases:
            _, feedback, _ = analyze_password_strength(password)
            suggestions = get_password_suggestions(feedback)
            suggestion_text = ' '.join(suggestions).lower()
            
            self.assertIn(expected_suggestion, suggestion_text,
                         f"Should suggest {expected_suggestion} for '{password}'")

def run_tests():
    """Run all tests"""
    print("🧪 Running Password Strength Tester Unit Tests")
    print("=" * 50)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestPasswordAnalysis))
    suite.addTests(loader.loadTestsFromTestCase(TestNameDetection))
    suite.addTests(loader.loadTestsFromTestCase(TestCrackTimeEstimation))
    suite.addTests(loader.loadTestsFromTestCase(TestPasswordSuggestions))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("✅ All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1

if __name__ == "__main__":
    exit(run_tests())
