import string
import re
import math
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

def detect_names_in_password(password):
    """Detect potential names in password"""
    # Common first names (subset for detection)
    common_names = [
        'john', 'jane', 'mike', 'mary', 'david', 'sarah', 'chris', 'lisa',
        'james', 'jennifer', 'robert', 'patricia', 'michael', 'linda',
        'william', 'elizabeth', 'richard', 'barbara', 'joseph', 'susan',
        'thomas', 'jessica', 'charles', 'nancy', 'daniel', 'karen',
        'matthew', 'betty', 'anthony', 'helen', 'mark', 'sandra',
        'donald', 'donna', 'steven', 'carol', 'paul', 'ruth', 'andrew',
        'sharon', 'joshua', 'michelle', 'kenneth', 'laura', 'kevin',
        'sarah', 'brian', 'kimberly', 'george', 'deborah', 'edward',
        'dorothy', 'ronald', 'lisa', 'timothy', 'nancy', 'jason',
        'karen', 'jeffrey', 'betty', 'ryan', 'helen', 'jacob', 'sandra',
        'gary', 'donna', 'nicholas', 'carol', 'eric', 'ruth', 'jonathan',
        'sharon', 'stephen', 'michelle', 'larry', 'laura', 'justin',
        'sarah', 'scott', 'kimberly', 'brandon', 'deborah', 'benjamin',
        'dorothy', 'samuel', 'lisa', 'gregory', 'nancy', 'alexander',
        'karen', 'patrick', 'betty', 'frank', 'helen', 'raymond',
        'sandra', 'jack', 'donna', 'dennis', 'carol', 'jerry', 'ruth'
    ]
    
    password_lower = password.lower()
    detected_names = []
    
    # Check for exact name matches (case insensitive)
    for name in common_names:
        if name in password_lower:
            detected_names.append(name.capitalize())
    
    # Check for names with numbers/symbols attached (like "John123")
    for name in common_names:
        pattern = re.compile(r'\b' + re.escape(name) + r'[0-9!@#$%^&*]*\b', re.IGNORECASE)
        if pattern.search(password):
            if name.capitalize() not in detected_names:
                detected_names.append(name.capitalize())
    
    return detected_names

def analyze_password_strength(password):
    """Comprehensive password strength analyzer"""
    
    # Initialize scoring
    score = 0
    feedback = []
    
    # Length analysis
    length = len(password)
    if length < 8:
        feedback.append(f"❌ Too short ({length} chars) - minimum 8 required")
        return 0, feedback, "Very Weak"
    elif length >= 8 and length < 12:
        score += 1
        feedback.append(f"⚠️ Short length ({length} chars) - consider 12+ characters")
    elif length >= 12 and length < 16:
        score += 2
        feedback.append(f"✅ Good length ({length} chars)")
    else:
        score += 3
        feedback.append(f"✅ Excellent length ({length} chars)")
    
    # Character variety analysis
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digits = bool(re.search(r'\d', password))
    # Use all ASCII punctuation characters and whitespace
    special_chars = string.punctuation + ' '
    has_special = any(char in special_chars for char in password)
    
    char_types = sum([has_lower, has_upper, has_digits, has_special])
    
    if has_lower:
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")
    
    if has_upper:
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")
    
    if has_digits:
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Missing numbers")
    
    if has_special:
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Missing special characters")
    
    # Pattern analysis
    if not re.search(r'(.)\1{2,}', password):
        score += 1
        feedback.append("✅ No repetitive characters")
    else:
        feedback.append("⚠️ Contains repetitive characters")
    
    # Common pattern checks
    common_patterns = [
        r'123',
        r'abc',
        r'qwerty',
        r'password',
        r'admin'
    ]
    
    pattern_found = False
    for pattern in common_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            pattern_found = True
            break
    
    if not pattern_found:
        score += 1
        feedback.append("✅ No common patterns detected")
    else:
        feedback.append("⚠️ Contains common patterns")
    
    # Name detection
    detected_names = detect_names_in_password(password)
    if not detected_names:
        score += 1
        feedback.append("✅ No common names detected")
    else:
        feedback.append(f"❌ Contains potential names: {', '.join(detected_names)}")
    
    # Determine strength level (updated for new scoring out of 10)
    if score <= 3:
        strength = "Very Weak"
    elif score <= 5:
        strength = "Weak"
    elif score <= 7:
        strength = "Moderate"
    elif score <= 9:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return score, feedback, strength

def estimate_crack_time(password):
    """Estimate time to crack password using brute force"""
    
    # Determine character set size
    char_set_size = 0
    
    if re.search(r'[a-z]', password):
        char_set_size += 26
    if re.search(r'[A-Z]', password):
        char_set_size += 26
    if re.search(r'\d', password):
        char_set_size += 10
    # Check for special characters (punctuation + space)
    special_chars = string.punctuation + ' '
    if any(char in special_chars for char in password):
        char_set_size += len(special_chars)  # 33 characters total
    
    if char_set_size == 0:
        return "Unable to estimate"
    
    # Calculate possible combinations
    password_length = len(password)
    total_combinations = char_set_size ** password_length
    
    # Assume 1 billion attempts per second (modern hardware)
    attempts_per_second = 1_000_000_000
    
    # Average time is half of total combinations
    avg_seconds = total_combinations / (2 * attempts_per_second)
    
    # Convert to readable format
    if avg_seconds < 60:
        return f"{avg_seconds:.2f} seconds"
    elif avg_seconds < 3600:
        return f"{avg_seconds/60:.2f} minutes"
    elif avg_seconds < 86400:
        return f"{avg_seconds/3600:.2f} hours"
    elif avg_seconds < 31536000:
        return f"{avg_seconds/86400:.2f} days"
    else:
        return f"{avg_seconds/31536000:.2f} years"

def get_password_suggestions(feedback):
    """Provide specific suggestions based on analysis"""
    suggestions = []
    
    feedback_text = ' '.join(feedback)
    
    if "Missing lowercase" in feedback_text:
        suggestions.append("• Add lowercase letters (a-z)")
    if "Missing uppercase" in feedback_text:
        suggestions.append("• Add uppercase letters (A-Z)")
    if "Missing numbers" in feedback_text:
        suggestions.append("• Add numbers (0-9)")
    if "Missing special" in feedback_text:
        suggestions.append("• Add special characters (!@#$%^&*)")
    if "Too short" in feedback_text or "Short length" in feedback_text:
        suggestions.append("• Use at least 12-16 characters")
    if "repetitive characters" in feedback_text:
        suggestions.append("• Avoid repeating the same character")
    if "common patterns" in feedback_text:
        suggestions.append("• Avoid common patterns like '123', 'abc', 'qwerty'")
    if "Contains potential names" in feedback_text:
        suggestions.append("• Avoid using names or personal information")
    
    return suggestions

def generate_pdf_report(password, score, feedback, strength, crack_time, suggestions):
    """Generate a PDF report of the password analysis"""
    
    # Create filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"password_analysis_report_{timestamp}.pdf"
    
    # Create the PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=1,  # Center alignment
        textColor=colors.darkblue
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor=colors.darkblue
    )
    
    # Title
    title = Paragraph("Password Security Analysis Report", title_style)
    story.append(title)
    story.append(Spacer(1, 20))
    
    # Report metadata
    report_info = [
        ["Report Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        ["Password Length:", f"{len(password)} characters"],
        ["Strength Score:", f"{score}/10"],
        ["Strength Level:", strength],
        ["Estimated Crack Time:", crack_time]
    ]
    
    info_table = Table(report_info, colWidths=[2*inch, 3*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (1, 0), (1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(info_table)
    story.append(Spacer(1, 20))
    
    # Character composition analysis
    story.append(Paragraph("Character Composition Analysis", heading_style))
    
    special_chars = string.punctuation + ' '
    composition_data = [
        ["Character Type", "Count"],
        ["Lowercase Letters", str(len(re.findall(r'[a-z]', password)))],
        ["Uppercase Letters", str(len(re.findall(r'[A-Z]', password)))],
        ["Numbers", str(len(re.findall(r'\d', password)))],
        ["Special Characters", str(sum(1 for char in password if char in special_chars))]
    ]
    
    comp_table = Table(composition_data, colWidths=[2.5*inch, 1*inch])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(comp_table)
    story.append(Spacer(1, 20))
    
    # Detailed analysis
    story.append(Paragraph("Detailed Security Analysis", heading_style))
    
    for item in feedback:
        # Clean up the feedback text for PDF
        clean_item = item.replace("✅", "✓").replace("❌", "✗").replace("⚠️", "!")
        story.append(Paragraph(clean_item, styles['Normal']))
    
    story.append(Spacer(1, 20))
    
    # Suggestions for improvement
    if suggestions:
        story.append(Paragraph("Recommendations for Improvement", heading_style))
        
        for suggestion in suggestions:
            story.append(Paragraph(suggestion, styles['Normal']))
        
        story.append(Spacer(1, 20))
    
    # Security recommendations
    story.append(Paragraph("General Security Best Practices", heading_style))
    
    best_practices = [
        "• Use a unique password for each account",
        "• Enable two-factor authentication when available",
        "• Regularly update your passwords",
        "• Consider using a reputable password manager",
        "• Never share your passwords with others",
        "• Avoid using personal information in passwords",
        "• Use passphrases with random words for better security"
    ]
    
    for practice in best_practices:
        story.append(Paragraph(practice, styles['Normal']))
    
    # Build the PDF
    doc.build(story)
    
    return filename

def main():
    print("🔐 Password Strength Tester")
    print("=" * 40)
    
    while True:
        password = input("\nEnter password to test (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not password:
            print("Please enter a password.")
            continue
        
        # Analyze password
        score, feedback, strength = analyze_password_strength(password)
        crack_time = estimate_crack_time(password)
        suggestions = get_password_suggestions(feedback)
        
        # Display results
        print(f"\n📊 Password Analysis Results")
        print("-" * 30)
        print(f"Password Length: {len(password)} characters")
        print(f"Strength Score: {score}/10")
        print(f"Strength Level: {strength}")
        print(f"Estimated Crack Time: {crack_time}")
        
        print(f"\n📝 Detailed Analysis:")
        for item in feedback:
            print(f"  {item}")
        
        if suggestions:
            print(f"\n💡 Suggestions for improvement:")
            for suggestion in suggestions:
                print(f"  {suggestion}")
        
        # Show character composition
        print(f"\n🔍 Character Composition:")
        print(f"  Lowercase: {len(re.findall(r'[a-z]', password))}")
        print(f"  Uppercase: {len(re.findall(r'[A-Z]', password))}")
        digits_pattern = r'\d'
        print(f"  Numbers: {len(re.findall(digits_pattern, password))}")
        # Count all special characters (punctuation + space)
        special_chars = string.punctuation + ' '
        special_count = sum(1 for char in password if char in special_chars)
        print(f"  Special: {special_count}")
        
        # Ask if user wants to generate a PDF report
        generate_report = input("\n📄 Would you like to generate a PDF report? (y/n): ").lower().strip()
        if generate_report == 'y' or generate_report == 'yes':
            try:
                filename = generate_pdf_report(password, score, feedback, strength, crack_time, suggestions)
                print(f"✅ PDF report generated successfully: {filename}")
            except Exception as e:
                print(f"❌ Error generating PDF report: {e}")
                print("Make sure you have the reportlab library installed.")
        
        print("\n" + "=" * 40)

if __name__ == "__main__":
    main()
