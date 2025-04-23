from email_validator import validate_email, EmailNotValidError

def check(email):
    try:
        v = validate_email(email) 
        email = v["email"]  
        print("True")
    except EmailNotValidError as e:
        print(str(e))
    
    return email

normalized_email = check("Andy@GMAIL.com")
print(f"Normalized email: {normalized_email}")