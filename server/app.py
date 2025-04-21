from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Configure your email settings
    sender_email = "your_email@example.com"
    receiver_email = "your_business_email@example.com"
    password = "your_email_password"

    msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    msg['Subject'] = 'New Contact Form Submission'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return jsonify({"message": "Success"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
