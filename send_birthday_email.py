import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_birthday_email():
    # Email configuration
    sender_email = "deepaksingh4.iitr@gmail.com"
    receiver_email = "deepaksingh4.iitr@gmail.com"  # Sending to yourself for testing
    
    # ⚠️ IMPORTANT: Replace this with your Gmail App Password
    # You can generate one at: https://myaccount.google.com/apppasswords
    password = "YOUR_APP_PASSWORD_HERE"

    message = MIMEMultipart("alternative")
    message["Subject"] = "✨ A Very Special Surprise for minnuuudddiiiii... ✨"
    message["From"] = f"petu <{sender_email}>"
    message["To"] = receiver_email

    # Plain text fallback
    text = """\
    Happy 26th Birthday, minnuuudddiiiii! 🎉
    
    I made something very special just for you. 
    
    Please open this link on your laptop for the best experience:
    https://singhdeepakkk04.github.io/26thbday/
    
    With all my love,
    petu ❤️
    """

    # Highly aesthetic HTML version
    html = """\
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400&display=swap');
        
        body {
          margin: 0;
          padding: 0;
          background-color: #fdfaf7;
          font-family: 'DM Sans', sans-serif;
        }
        .wrapper {
          width: 100%;
          table-layout: fixed;
          background-color: #fdfaf7;
          padding-bottom: 60px;
        }
        .main {
          background-color: #ffffff;
          margin: 0 auto;
          width: 100%;
          max-width: 600px;
          border-spacing: 0;
          color: #3d2430;
          border-radius: 24px;
          box-shadow: 0 20px 40px rgba(184, 51, 89, 0.08);
          overflow: hidden;
          border: 1px solid rgba(249, 180, 204, 0.3);
        }
        .header {
          background: linear-gradient(135deg, #f9b4cc, #e06c95);
          padding: 40px 20px;
          text-align: center;
        }
        .header h1 {
          margin: 0;
          color: #ffffff;
          font-family: 'Cormorant Garamond', serif;
          font-size: 36px;
          font-weight: 600;
          text-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .content {
          padding: 50px 40px;
          text-align: center;
        }
        .greeting {
          font-family: 'Cormorant Garamond', serif;
          font-size: 28px;
          color: #b83359;
          margin-bottom: 20px;
          font-style: italic;
        }
        .message {
          font-size: 16px;
          line-height: 1.8;
          color: #55444b;
          margin-bottom: 40px;
          font-weight: 300;
        }
        .btn-container {
          text-align: center;
          margin-bottom: 40px;
        }
        .btn {
          background: linear-gradient(135deg, #d4a843, #b38b22);
          color: #ffffff !important;
          text-decoration: none;
          padding: 16px 40px;
          border-radius: 50px;
          font-weight: 600;
          font-size: 16px;
          letter-spacing: 1px;
          text-transform: uppercase;
          display: inline-block;
          box-shadow: 0 10px 20px rgba(212, 168, 67, 0.3);
        }
        .footer {
          text-align: center;
          padding: 30px;
          background-color: #fff9fb;
          border-top: 1px solid rgba(249, 180, 204, 0.2);
        }
        .note {
          font-size: 14px;
          color: #b83359;
          font-style: italic;
          margin-bottom: 10px;
        }
        .sig {
          font-family: 'Cormorant Garamond', serif;
          font-size: 24px;
          color: #d4a843;
          font-weight: 600;
        }
      </style>
    </head>
    <body>
      <center class="wrapper">
        <table class="main" width="100%">
          <tr>
            <td class="header">
              <h1>Happy 26th Birthday! ✨</h1>
            </td>
          </tr>
          <tr>
            <td class="content">
              <div class="greeting">Dearest minnuuudddiiiii,</div>
              <div class="message">
                Today is a day to celebrate the most extraordinary person. I've spent some time putting together a little digital surprise just for you, walking through our memories and all the reasons why you're amazing.
              </div>
              
              <div class="btn-container">
                <a href="https://singhdeepakkk04.github.io/26thbday/" class="btn">Open Your Surprise</a>
              </div>
              
              <div class="note">
                🌟 <strong>Important Note:</strong> Please make sure to open this link on your <strong>laptop</strong> for the best and most beautiful experience! 🌟
              </div>
            </td>
          </tr>
          <tr>
            <td class="footer">
              <div class="message" style="margin-bottom: 10px;">With all my love,</div>
              <div class="sig">your petu ❤️</div>
            </td>
          </tr>
        </table>
      </center>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    print("Attempting to send email...")
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        print("✅ Email sent successfully to:", receiver_email)
    except Exception as e:
        print("❌ Error sending email:")
        print(e)
        print("\nNote: Make sure you have replaced 'YOUR_APP_PASSWORD_HERE' with a valid Gmail App Password.")
        print("If you have 2-Step Verification enabled, you cannot use your regular Gmail password.")

if __name__ == "__main__":
    send_birthday_email()
