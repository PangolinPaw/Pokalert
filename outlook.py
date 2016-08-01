import win32com.client

def sendMessage(recipient, subject, message, attachment):
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.body = message
    mail.Attachments.Add(Source=attachment)
    mail.send

if __name__ == "__main__":
    sendMessage()