# Email Automation V2

A Python email automation project that sends personalized HTML emails to multiple recipients using a CSV file, with support for file attachments.

## Features
- Reads recipient names and email addresses from a CSV file
- Personalizes emails using `{name}`
- Sends HTML email content
- Supports multiple file attachments
- Uses Gmail SMTP with an app password

## Files
- `main.py` – Reads recipients and personalizes the email
- `email_sender.py` – Handles email creation, attachments, and SMTP
- `body.html` – HTML email template
- `config.example.py` – Example configuration
- `receivers.example.csv` – Example recipient CSV
- `starter.py` – Entry point
- `attachments/` – Files to attach

## Setup
1. Install Python 3.
2. Copy `config.example.py` to `config.py`.
3. Add your Gmail address and Gmail App Password to `config.py`.
4. Copy `receivers.example.csv` to `receivers.csv` and add recipients.
5. Add files to the `attachments/` folder.
6. Run:

```bash
python3 starter.py
