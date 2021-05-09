from trycourier import Courier

def configure_sms(event_name, short_description, phone_number, location, start_date, time, host_name):
    message = "It's time to save the planet!\n" + "You are invited to " + event_name + ".\n" + short_description + "\n\n"
    message = message + "Location: " + location + "\n"
    message = message + "Date: " + start_date + "\n"
    message = message + "Time: " + start_date + "\n\n"
    message = message + "Hope to see you there!\n\n"
    message = message + "Thanks\n" + host_name

    phoneNum = phone_number
    
    #print(message)
    return message

def send_sms(phone_number, message):
    client = Courier(auth_token="pk_prod_3NF6S5AZ4S4TSRPEM6AJVNRVCFJT")
    resp = client.send(
        event="3T9NBKMKHV4WTVPHZRPKF1Y5NVQ5",
        recipient="3T9NBKMKHV4WTVPHZRPKF1Y5NVQ5",
        profile={
            "email": "malharshah2000@gmail.com",
            "phone_number": phone_number
        },
        data={
            "unique_text": message,
        },
    )
    print(resp['messageId'])

MessageFinal = configure_sms("UofT Tree Plant", "Planting trees at UofT Garden", "647-893-7552", "27 King's College Cir, Toronto", "May 23rd", "12 PM", "Sowrow")

send_sms("647-893-7552", MessageFinal)

#send_sms(event_name="Clean UP", short_description="Come to clean up the city", phone_number=43798979696, location="89 Chestnut St", start_date="121212", host_name="Rama")

# from trycourier import Courier



# client = Courier(auth_token="pk_prod_3NF6S5AZ4S4TSRPEM6AJVNRVCFJT") #or set via COURIER_AUTH_TOKEN env var
# messageId = "Checking"

# resp = client.send(
#     event="your-event-id",
#     recipient="your-recipient-id",
#     profile={
#         "email": "malharshah2000@gmail.com",
#         "phone_number": "647-893-7552"
#     },
#     data={
#       "world": "Python!"
#     }
# )
# print(resp['messageId'])

# {
#   "event": "<COURIER_NOTIFICATION_ID>",
#   "recipient": "katherine_pryde",
#   "profile": {
#     "phone_number": "+12345678901"
#   },
#   "data": {
#     "name": "Katherine Pryde"
#   },
#   "override": {
#     "twilio": {
#       "body": {
#         "to": "+109876543210"
#       }
#     },
#     "config": {
#       "accountSid": "<your Account SID>",
#       "authToken": "<your Auth Token>"
#     }
#   }
# }