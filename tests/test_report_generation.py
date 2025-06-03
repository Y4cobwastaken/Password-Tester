#!/usr/bin/env python3
"""
Unit tests for PDF report generation functionality
"""

import unittest
import sys
import os
import tempfile
from unittest.mock import patch, MagicMock

# Add parent directory to path to import main module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import generate_pdf_report, analyze_password_strength, get_password_suggestions

class TestReportGeneration(unittest.TestCase):
    """Test cases for PDF report generation"""
    
    def setUp(self):
        """Set up test data"""
        self.test_password = "TestPassword123!"
        self.score, self.feedback, self.strength = analyze_password_strength(self.test_password)
        self.crack_time = "2.5 years"
        self.suggestions = get_password_suggestions(self.feedback)
    
    @patch('main.SimpleDocTemplate')
    @patch('main.datetime')
    def test_pdf_report_creation(self, mock_datetime, mock_doc):
        """Test PDF report file creation"""
        # Mock datetime for consistent filename
        mock_datetime.now.return_value.strftime.return_value = "20241201_120000"
        
        # Mock PDF document
        mock_doc_instance = MagicMock()
        mock_doc.return_value = mock_doc_instance
        
        filename = generate_pdf_report(
            self.test_password,
            self.score,
            self.feedback,
            self.strength,
            self.crack_time,
            self.suggestions
        )
        
        # Verify filename format
        expected_filename = "password_analysis_report_20241201_120000.pdf"
        self.assertEqual(filename, expected_filename)
        
        # Verify document creation was called
        mock_doc.assert_called_once()
        mock_doc_instance.build.assert_called_once()
    
    def test_report_with_empty_data(self):
        """Test report generation with minimal data"""
        try:
            filename = generate_pdf_report(
                "test",
                0,
                ["❌ Too short"],
                "Very Weak",
                "1 second",
                ["• Use longer password"]
            )
            self.assertIsInstance(filename, str)
            self.assertTrue(filename.endswith('.pdf'))
        except Exception as e:
            self.fail(f"Report generation failed with minimal data: {e}")
    
    def test_report_with_complex_data(self):
        """Test report generation with complex data"""
        complex_feedback = [
            "✅ Excellent length (20 chars)",
            "✅ Contains lowercase letters",
            "✅ Contains uppercase letters",
            "✅ Contains numbers",
            "✅ Contains special characters",
            "✅ No repetitive characters",
            "✅ No common patterns detected",
            "❌ Contains potential names: John"
        ]
        
        complex_suggestions = [
            "• Avoid using names or personal information",
            "• Consider using random words instead"
        ]
        
        try:
            filename = generate_pdf_report(
                "JohnSecurePassword123!",
                8,
                complex_feedback,
                "Strong",
                "1.2e+15 years",
                complex_suggestions
            )
            self.assertIsInstance(filename, str)
            self.assertTrue(filename.endswith('.pdf'))
        except Exception as e:
            self.fail(f"Report generation failed with complex data: {e}")
    
    def test_report_filename_uniqueness(self):
        """Test that report filenames are unique"""
        # This test would need actual file creation to verify uniqueness
        # For now, we test the timestamp-based naming logic
        import re
        from datetime import datetime
        
        filename = generate_pdf_report(
            self.test_password,
            self.score,
            self.feedback,
            self.strength,
            self.crack_time,
            self.suggestions
        )
        
        # Check filename pattern
        pattern = r'password_analysis_report_\d{8}_\d{6}\.pdf'
        self.assertIsNotNone(re.match(pattern, filename),
                            "Filename should follow timestamp pattern")
    
    def test_special_characters_in_feedback(self):
        """Test report generation with special characters"""
        special_feedback = [
            "✅ Contains émojis and spëcial chars",
            "❌ Missing some requirements",
            "⚠️ Warning about patterns"
        ]
        
        try:
            filename = generate_pdf_report(
                "TestPassword!@#",
                5,
                special_feedback,
                "Moderate",
                "5 hours",
                ["• Improve complexity"]
            )
            self.assertIsInstance(filename, str)
        except Exception as e:
            self.fail(f"Report generation failed with special characters: {e}")

class TestReportContent(unittest.TestCase):
    """Test cases for PDF report content validation"""
    
    @patch('main.SimpleDocTemplate')
    def test_report_structure(self, mock_doc):
        """Test that report contains expected sections"""
        mock_doc_instance = MagicMock()
        mock_doc.return_value = mock_doc_instance
        
        password = "TestPassword123!"
        score, feedback, strength = analyze_password_strength(password)
        suggestions = get_password_suggestions(feedback)
        
        generate_pdf_report(
            password, score, feedback, strength, "1 year", suggestions
        )
        
        # Verify build was called with story content
        mock_doc_instance.build.assert_called_once()
        
        # Get the story argument passed to build
        story_arg = mock_doc_instance.build.call_args[0][0]
        self.assertIsInstance(story_arg, list, "Story should be a list")
        self.assertGreater(len(story_arg), 0, "Story should contain elements")
    
    def test_character_composition_calculation(self):
        """Test character composition calculations for report"""
        import re
        import string
        
        test_password = "MyTest123!@#"
        
        # Calculate composition
        lowercase_count = len(re.findall(r'[a-z]', test_password))
        uppercase_count = len(re.findall(r'[A-Z]', test_password))
        digit_count = len(re.findall(r'\d', test_password))
        special_chars = string.punctuation + ' '
        special_count = sum(1 for char in test_password if char in special_chars)
        
        # Verify calculations
        self.assertEqual(lowercase_count, 4)  # y, e, s, t
        self.assertEqual(uppercase_count, 2)  # M, T
        self.assertEqual(digit_count, 3)      # 1, 2, 3
        self.assertEqual(special_count, 3)    # !, @, #
        
        # Total should equal password length
        total = lowercase_count + uppercase_count + digit_count + special_count
        self.assertEqual(total, len(test_password))

class MockReportTests(unittest.TestCase):
    """Test cases using mocked PDF components"""
    
    @patch('main.Table')
    @patch('main.SimpleDocTemplate')
    def test_table_creation(self, mock_doc, mock_table):
        """Test that tables are created correctly"""
        mock_doc_instance = MagicMock()
        mock_doc.return_value = mock_doc_instance
        
        mock_table_instance = MagicMock()
        mock_table.return_value = mock_table_instance
        
        generate_pdf_report(
            "test", 5, ["test feedback"], "Moderate", "1 hour", ["suggestion"]
        )
        
        # Verify tables were created
        self.assertGreater(mock_table.call_count, 0, "Tables should be created")
        
        # Verify table styling was applied
        mock_table_instance.setStyle.assert_called()
    
    @patch('main.Paragraph')
    @patch('main.SimpleDocTemplate')
    def test_paragraph_creation(self, mock_doc, mock_paragraph):
        """Test that paragraphs are created correctly"""
        mock_doc_instance = MagicMock()
        mock_doc.return_value = mock_doc_instance
        
        generate_pdf_report(
            "test", 5, ["test feedback"], "Moderate", "1 hour", ["suggestion"]
        )
        
        # Verify paragraphs were created
        self.assertGreater(mock_paragraph.call_count, 0, "Paragraphs should be created")

def run_report_tests():
    """Run all report generation tests"""
    print("📄 Running PDF Report Generation Tests")
    print("=" * 45)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestReportGeneration))
    suite.addTests(loader.loadTestsFromTestCase(TestReportContent))
    suite.addTests(loader.loadTestsFromTestCase(MockReportTests))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 45)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("✅ All report tests passed!")
        return 0
    else:
        print("❌ Some report tests failed!")
        return 1

if __name__ == "__main__":
    exit(run_report_tests())
