email=input("enter the email id")


if(email == email.lower() and email[0]==email.isalpha() and '@' in email and email.endswith("@gmail.com")):
   print("email is valid")
else:
  print("email is invalid")
