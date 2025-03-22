import os
import requests
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
API_URL = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def send_whatsapp_message(invitee_phone_number, invitee_name, event_details, host):
    data = {
        "messaging_product": "whatsapp",
        "to": invitee_phone_number,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": { "code": "en_US" },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        { "type": "text", "text": event_details },
                        { "type": "text", "text": host }
                    ]
                },
                {
                    "type": "button",
                    "sub_type": "url",
                    "index": "0",
                    "parameters": [
                        { "type": "text", "text": f"&entry.1671793693={invitee_name}&entry.286063792={invitee_phone_number}" }
                    ]
                }
            ]
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=data)
    return response.json()

print(send_whatsapp_message("972504227119", "invitee", "event details", "Oz"))
