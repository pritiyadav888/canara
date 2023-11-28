from flask import Flask, request, jsonify, render_template, redirect
from flask_socketio import SocketIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyotp
import os
import joblib
from dotenv import load_dotenv
import tensorflow as tf

load_dotenv()
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow CORS

# Load your trained model
model = tf.keras.models.load_model('best_fraud_detection_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        transaction_data = request.json
        prediction = model.predict([list(transaction_data.values())])

        if prediction[0] == 1:  # Assuming '1' indicates a fraudulent prediction
            socketio.emit('fraud alert', {'message': 'A fraudulent transaction was detected.'})

        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return a JSON response with the error message and a 500 status code for internal server error


@app.route('/')
def home():
    # Emit a test fraud alert
    socketio.emit('fraud alert', {'message': 'Test alert'})
    return render_template('bank_cust.html')

@app.route('/model')
def go_to_index():
    return render_template('index.html')


@socketio.on('connection')
def handle_connection():
    print('A user connected')

@socketio.on('request code')
def handle_request_code():
    secret = pyotp.random_base32()
    token = pyotp.TOTP(secret).now()
    socketio.emit('code update', {'code': token})  # Ensure it's socketio.emit, not just emit


def format_key(key):
    return ' '.join(word.capitalize() for word in key.split('_'))


@app.route('/send-email')
def send_email():
    recipient = "yadavpriti0210@gmail.com"
    subject = "Test Email"
    body = "This is a test email."
    send_email_function(recipient, subject, body)

    socketio.emit('fraud alert', {'message': 'A test email has been sent.'})  # Emit alert message
    return "Email sent!"

@app.route('/send-fraud-email')
def send_fraud_email():
    try:
        print('send-fraud-email route was hit')
        fraud_transaction = {
            'Time': 406,
            'V1': -2.3122265423263,
            'V2': 1.95199201064158,
            'V3': -1.60985073229769,
            'V4': 3.9979055875468,
            'V5': -0.5221878646677,
            'V6': -1.4265453192059,
            'V7': -2.5373873062458,
            'V8': 1.39165724829804,
            'V9': -2.7700892771943,
            'V10': -2.7722721446592,
            'V11': 3.20203320709635,
            'V12': -2.89990738849473,
            'V13': -0.5952218813249,
            'V14': -4.28925378244217,
            'V15': 0.3897241202746,
            'V16': -1.14074717980657,
            'V17': -2.83005567450437,
            'V18': -0.0168224681806,
            'V19': 0.41695570503798,
            'V20': 0.12691055906147,
            'V21': 0.51723237086176,
            'V22': -0.0350493686052,
            'V23': -0.46521107618239,
            'V24': 0.3201981985144,
            'V25': 0.0445191674733,
            'V26': 0.1778397982841,
            'V27': 0.26114500256722,
            'V28': -0.1432758746982,
            'Amount': 0.00
        }
        
        # Convert the keys to a more readable format
        formatted_transaction_data = {format_key(k): v for k, v in fraud_transaction.items()}
        
        # Send an email with the formatted transaction data
        send_email_function("yadavpriti0210@gmail.com", "Fraud Alert Notification", formatted_transaction_data)
        print(f'Emitting fraud alert We have detected a potentially fraudulent transaction on your account...... ') 
        socketio.emit('fraud alert', {'message': 'We have detected a potentially fraudulent transaction on your account. Please check your email for details.'})
        return "Fraud email sent with dummy data!"
    except Exception as e:
        print(f'Error in /send-fraud-email route: {e}')
        return jsonify({'error': str(e)}), 500

def create_email_body(transaction_data):
    # Start the HTML email body
    html_email_body = """
    <html>
      <body>
        <div style="font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; color: #333;">
          <h2 style="color: #d32f2f;">Fraud Alert Notification</h2>
          <p>Dear Customer,</p>
          <p>We have detected a potentially fraudulent transaction on your account:</p>
          <table style="width: 100%; max-width: 600px; border-collapse: collapse;">
    """

    # Add each transaction detail to the email body
    for key, value in transaction_data.items():
        html_email_body += f"""
              <tr>
                <td style="padding: 8px; border: 1px solid #ddd; text-align: left;">{key}</td>
                <td style="padding: 8px; border: 1px solid #ddd; text-align: right;">{value}</td>
              </tr>
        """

    # End the HTML email body
    html_email_body += """
          </table>
          <p>If you did not authorize this transaction, please contact us immediately.</p>
          <p>Regards,</p>
          <p>Your Bank Security Team</p>
        </div>
      </body>
    </html>
    """
    return html_email_body

def send_email_function(recipient, subject, transaction_data):
    sender = 'pritiyadav888@gmail.com'
    password = os.getenv('EMAIL_PASS')
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    # Create the HTML email body from the transaction data
    body = create_email_body(transaction_data)
    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    socketio.run(app, debug=True, port=3000)
