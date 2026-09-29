# Email Automation — V1

A Python-based email automation project that sends emails to multiple recipients using a CSV file.

## Features

* Sends emails through Gmail SMTP
* Supports multiple recipients using CSV
* Supports file attachments
* Uses a separate configuration file for sender credentials and subject

## Project Structure

```text
V1/
├── attachments/
├── email_sender.py
├── main.py
├── starter.py
└── receivers.example.csv
```

## Setup

1. Create a `config.py` file containing your Gmail address, Gmail App Password, and email subject.
2. Create `receivers.csv` using `receivers.example.csv` as the template.
3. Place files to be attached inside the `attachments/` folder.
4. Run:

```bash
python3 starter.py
```

## Note

Do not upload `config.py` or `receivers.csv` if they contain credentials or real email addresses.
