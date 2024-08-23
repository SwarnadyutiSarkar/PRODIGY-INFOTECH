import re

def check_password_strength(password):
    # Define criteria
    criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'number': re.search(r'[0-9]', password) is not None,
        'special_char': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }
    
    # Check which criteria are met
    criteria_met = [key for key, met in criteria.items() if met]
    
    # Determine strength
    if len(criteria_met) == 5:
        strength = 'Very Strong'
    elif len(criteria_met) == 4:
        strength = 'Strong'
    elif len(criteria_met) == 3:
        strength = 'Moderate'
    elif len(criteria_met) == 2:
        strength = 'Weak'
    else:
        strength = 'Very Weak'
    
    # Provide feedback
    feedback = {
        'Length (at least 8 characters)': criteria['length'],
        'Contains uppercase letter': criteria['uppercase'],
        'Contains lowercase letter': criteria['lowercase'],
        'Contains number': criteria['number'],
        'Contains special character': criteria['special_char']
    }
    
    print(f"Password Strength: {strength}\n")
    for criterion, met in feedback.items():
        status = "Met" if met else "Not Met"
        print(f"{criterion}: {status}")

def main():
    print("Password Complexity Checker")
    password = input("Enter a password to check: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
