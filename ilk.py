import smtplib

try:
    email = input("Sender Email: ")
    receiver_email = input("Receiver Email: ")

    subject = input("Subject: ")
    message = input("Message: ")

    text = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email, "your password")
    server.sendmail(email, receiver_email,text)

    print("Email sent to "+receiver_email)
except:
    print("Email doesnt sent")