# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = ""
auth_token = ""
twilio_number = ""


def send_text(message, to_number, from_number=twilio_number):
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to=to_number,
        from_=from_number,
        body=message)
