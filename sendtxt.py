from twilio.rest import Client

account_sid = 'ACd6380ec451a762cda90dae02f88949a3' # Found on Twilio Console Dashboard
auth_token = 'd573fa958ba6766c55c5bb2ad41dd0cf' # Found on Twilio Console Dashboard

myPhone = '+917899539745' # Phone number you used to verify your Twilio account
TwilioNumber = '+12058096027' # Phone number given to you by Twilio

client = Client(account_sid, auth_token)

client.messages.create(to=myPhone,from_=TwilioNumber,
body='Alert!Your child is out of the gate ' + u'\U0001f680')
