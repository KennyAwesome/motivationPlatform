#!/bin/python

from twilio.rest import TwilioRestClient

account_sid = "AC6865ef1ff37933c0a1af74b799c827cf"
auth_token  = "702eed3bdf5c5e45e9e84576996be227"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="It's magic!",
    to="+4917661254477",
    from_="+4915735987462 ")

print(message.sid)
