from trycourier import Courier

client = Courier(auth_token="pk_prod_3NF6S5AZ4S4TSRPEM6AJVNRVCFJT")

resp = client.send(
  event="3T9NBKMKHV4WTVPHZRPKF1Y5NVQ5",
  recipient="00837b94-3e03-42bc-8f1b-eabe0370e33b",
  profile={
      "email": "malharshah2000@gmail.com",
      "phone_number": "647-893-7552"
  },
  data={
  },
)

print(resp['messageId'])

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