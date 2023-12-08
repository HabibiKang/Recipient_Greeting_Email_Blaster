import re
import csv
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import certifi

# Regular expression to match email addresses
email_regex = r"[\w]+[\d]*\@[\w]+[\d]*\.\w+"

# Create an empty list to store the extracted email addresses
extracted_data = []

# Open CSV file
with open("clients.csv", mode="r") as file:
    csv_file = csv.reader(file)
    for rows in csv_file:
        if len(rows) > 1:
            first_name = rows[0]
            line_str = ' '.join(rows)
            matches = re.findall(email_regex, line_str)
            if matches:
                email = matches[0]
                extracted_data.append((first_name, email))

subject = "Add your subject here"

message = "Add your message here"


# Replace the following placeholders with your Gmail email account information
smtp_server = "smtp.gmail.com"
sender_email = "add your email address here"  # Your Gmail email address
password = "zbfx yjmf ytcj ulyt"  # Your Gmail password

# Create an SMTP connection
context = ssl.create_default_context(cafile=certifi.where())

with smtplib.SMTP_SSL(smtp_server, 465, context=context) as smtp:
    smtp.login(sender_email, password)

    for first_name, email in extracted_data:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = email
        msg["Subject"] = subject

        # Customize the email body with the first name
        custom_message = message.replace("[FirstNamePlaceholder]", first_name)
        msg.attach(MIMEText(custom_message, "plain"))

        text = msg.as_string()
        smtp.sendmail(sender_email, email, text)

# Print the extracted email addresses
for name, email in extracted_data:
    print(f"Email sent to {name} ({email})")

print("All emails sent successfully!")

