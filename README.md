# Rain-Alert

## Overview
This Python script provides a rain alert notification system that checks weather forecasts for the next 12 hours and sends an email when precipitation is expected.

## Features
- Monitors weather forecasts for upcoming rain conditions.
- Sends email alerts when rain is predicted within the next 12 hours.
- Easy setup and configuration.

## Applications
This project can be useful in various scenarios, including:
- **Outdoor Activities**: Receive alerts to plan outdoor activities based on weather conditions.
- **Farmers and Gardeners**: Get notified to take necessary precautions for crops or gardens.
- **Travel Planning**: Plan travel routes or activities based on weather predictions.

## Installation
1. Clone the repository : git clone https://github.com/your-username/rain-alert.git
2. Install dependencies : pip install -r requirements.txt

## Usage
1. Set up your email credentials and location details in `main.py`.
2. Run the script : python main.py

## Configuration
To configure the Rain Alert Project, edit the `main.py` file with the following details:

- **Location**: Update `lat and lon` with your latitude and longitude for which you want to receive rain alerts.

### Example
```python
# Example configuration in main.py
latitude = 'your location latitue'
longitude = 'your location longitude'
sender_email = 'your-email@gmail.com'
receiver_email = 'recipient-email@gmail.com'
email_password = 'your-email-password'






