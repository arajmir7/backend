import csv
import os
from datetime import datetime

FILE_NAME = "gst_history.csv"


def show_history():
    if not os.path.exists(FILE_NAME):
        print("No previous GST records found.\n")
        return

    print("\n--- GST CALCULATION HISTORY ---")
    with open(FILE_NAME, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            print(
                f"Price: {row[0]}, GST%: {row[1]}, GST Amt: {row[2]}, Final Price: {row[3]}, Time: {row[4]}"
            )
    print()


def save_to_csv(price, gst_rate, gst_amount, final_price):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(
                ["price", "gst_rate", "gst_amount", "final_price", "timestamp"]
            )

        writer.writerow(
            [
                price,
                gst_rate,
                round(gst_amount, 2),
                round(final_price, 2),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ]
        )


def calculate_gst():
    try:
        price = float(input("Enter product price: "))
        gst_rate = float(input("Enter GST rate (%): "))

        if price < 0 or gst_rate < 0:
            print("❌ Price and GST rate must be non-negative.")
            return

        gst_amount = (price * gst_rate) / 100
        final_price = price + gst_amount

        print("\n--- GST CALCULATION RESULT ---")
        print(f"GST Amount: ₹{gst_amount:.2f}")
        print(f"Final Price: ₹{final_price:.2f}\n")

        save_to_csv(price, gst_rate, gst_amount, final_price)

    except ValueError:
        print("❌ Invalid input. Please enter numeric values only.")


def main():
    print("=== GST CALCULATOR ===\n")
    show_history()
    calculate_gst()
    print("✅ Calculation saved successfully.")


if __name__ == "__main__":
    main()
