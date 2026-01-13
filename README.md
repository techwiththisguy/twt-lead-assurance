# TWT Lead Assurance
A Lead Capture & Follow-Up Assurance System by Tech With Thisguy LLC

# TWT Lead Assurance

TWT Lead Assurance is a lightweight lead capture and follow-up system designed for small service-based businesses.

It ensures every inquiry is captured, notified, and tracked so no lead falls through the cracks.

This project was built as a **production-ready MVP** and is actively usable for real businesses.

---

## Core Features

- Public quote request form
- Persistent lead storage (SQLite)
- Admin login protection
- Admin leads inbox
- Lead status tracking (NEW, CONTACTED, CLOSED, LOST)
- Mobile-friendly interface
- Clean, minimal workflow (no CRM bloating)

---

## Why TWT Lead Assurance

Small businesses often receive inquiries from multiple sources: 
- website
- Facebook
- text messages
- phone calls
- email

Leads get missed, follow-ups are delayed, and there's no single source of truth.

TWT Lead Assurance solves this by:
- Capturing every inquiry in one place
- Instantly notifying the business
- Providing a simple, focused follow-up tracker
- Keeping the workflow lightweight and easy to adopt

---

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2 templates
- Session-based authentication

---

## Status

Production-ready.

This project is actively developed and intended to be deployed as a reusable lead intake platform for small service-based businesses.

---

## Setup & Run Locally

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Run the app
python run.py