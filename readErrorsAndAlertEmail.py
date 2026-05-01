import emailCredentials
import smtplib
from email.mime.text import MIMEText

def sendEmail():
    print(f"SENDING EMAIL TO {emailCredentials.receiver_email}")
    email_msg="TEST EMAIL"
    server=None
    email_body="COUNT EXCEEDED FROM THRESHOLD/[03]"
    email_content=MIMEText(email_body)
    email_content["from"]=emailCredentials.sender_email
    email_content["subject"]="Alert Email"
    email_content["to"]=emailCredentials.receiver_email
    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(emailCredentials.sender_email,emailCredentials.app_pass)
        server.sendmail(
            emailCredentials.sender_email,
            emailCredentials.receiver_email,
            email_content.as_string())
        print("EMAIL SENT SUCCESSFULLY!!")
    except Exception as e:
        print(f"ERROR OCCURED -- >> {e}")
    finally:
        server.quit()     
    

error_count=4
#READING LOG FILES AND SEARCHING FOR COUNT MORE THEN 2
#WRITE ERROR CODE HERE WHICH READS FILE AND REGULATE COUNT


if error_count>2 and __name__ == "__main__":
    sendEmail()