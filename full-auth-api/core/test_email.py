from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_test_email(EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD):
    print('****************************************************************')
    # SMTP Configuration

    smtp_server = EMAIL_HOST
    smtp_port = EMAIL_PORT
    smtp_user = EMAIL_HOST_USER
    smtp_password = EMAIL_HOST_PASSWORD

    sender_email = smtp_user
    # Replace with your recipient email address
    receiver_email = 'reza.astaraki.work@gmail.com'

    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Email"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = "This is a test email sent from Django."
    html = "<p>This is a <strong>test email</strong> sent from Django.</p>"

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part1)
    message.attach(part2)

    try:
        # Create SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        # Login to SMTP server
        server.login(smtp_user, smtp_password)
        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", e)
    finally:
        # Close SMTP session
        server.quit()


# Call the function to send the test email
