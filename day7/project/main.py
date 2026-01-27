import smtplib
import csv
import os
import random
import string
from email.message import EmailMessage
from dotenv import load_dotenv

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# --------------------------------------------------
# Resolve CSV path safely (IMPORTANT FIX)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "emails.csv")

# --------------------------------------------------
# Generate coupon code
# --------------------------------------------------
def generate_coupon(length=8):
    return "SAVE-" + "".join(
        random.choices(string.ascii_uppercase + string.digits, k=length)
    )

# --------------------------------------------------
# Send email
# --------------------------------------------------
def send_email(to_email, name, coupon):
    msg = EmailMessage()
    msg["Subject"] = "🎉 Your Exclusive Discount Coupon!"
    msg["From"] = SMTP_EMAIL
    msg["To"] = to_email

    msg.set_content(
        f"""
Hi {name},

Thank you for being part of our community!

Here is your exclusive discount coupon:

👉 {coupon}

Use this coupon at checkout and save big 🎁

Best regards,
Marketing Team
"""
    )

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)

# --------------------------------------------------
# Main execution
# --------------------------------------------------
def main():
    sent = 0
    failed = 0

    if not os.path.exists(CSV_PATH):
        print("❌ emails.csv not found!")
        return

    with open(CSV_PATH, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                coupon = generate_coupon()
                send_email(row["email"], row["name"], coupon)
                print(f"✅ Sent to {row['email']} | Coupon: {coupon}")
                sent += 1
            except Exception as e:
                print(f"❌ Failed for {row['email']} → {e}")
                failed += 1

    print("\n📊 Campaign Summary")
    print(f"✅ Emails Sent   : {sent}")
    print(f"❌ Emails Failed : {failed}")

# --------------------------------------------------
# Entry point
# --------------------------------------------------
if __name__ == "__main__":
    main()
