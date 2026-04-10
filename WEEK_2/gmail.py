email = input("Enter your Gmail address: ")

if (email.endswith("@gmail.com") and email == email.lower() and email[0].isalpha() and "@" in email):
    print("Valid Gmail address.")
else:
    print("Invalid Gmail address.")