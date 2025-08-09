# Birthday Email Sender

This Python script automatically sends personalized birthday emails.  
It reads birthday information from `birthdays.csv`, checks if today matches any birthday,  
selects a random letter template from the `letter_templates` folder, replaces `[NAME]` with the recipient's name,  
and sends the email via Gmail SMTP. The email password is securely loaded from an environment variable.

---

## Features & How It Works

- Reads birthdays from a CSV file (`birthdays.csv`).
- Checks if today's date matches any birthday.
- Picks a random letter template and personalizes it by replacing `[NAME]`.
- Sends the email using Gmail SMTP.
- Keeps your email password secure by reading it from the `EMAIL_PASSWORD` environment variable.

---

## Requirements

- Python 3.x
- `pandas` library (`pip install pandas`)

---

## Setup Instructions

1. **Create `birthdays.csv`** with these columns: `name,email,year,month,day`.  
   Example:

   ```csv
   name,email,year,month,day
   Yusuf,yusuf@example.com,1990,8,9
   Ahmet,ahmet@example.com,1985,10,25
