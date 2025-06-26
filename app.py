from datetime import datetime
import pytz

# Set timezone to India
india_timezone = pytz.timezone('Asia/Kolkata')

# Get current time in IST
current_time = datetime.now(india_timezone)

# Format and print
print("📅 Date:", current_time.strftime("%d-%m-%Y"))
print("⏰ Time:", current_time.strftime("%I:%M:%S %p"))
print("📆 Day :", current_time.strftime("%A"))
