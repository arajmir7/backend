from flask_mail import Mail, Message

mail = Mail()

def send_enrollment_email(app, student_email, student_name):
    with app.app_context():
        try:
            msg = Message(
                'Enrollment Confirmed! 🎓',
                sender=app.config['MAIL_USERNAME'],
                recipients=[student_email]
            )
            msg.body = f"High key, welcome to the program, {student_name}! You're officially in the database."
            mail.send(msg)
            print(f"✅ [Automation] Email sent to {student_email}")
        except Exception as e:
            print(f"❌ [Automation Error] Failed to send: {e}")