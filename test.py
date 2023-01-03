from twilio.rest import Client 
from twilio.base.exceptions import TwilioRestException
 
sid = input("Enter SID:")
token = input("Enter auth token:")
# msg_sid = input("Enter messaging SID:") 

account_sid = sid 
auth_token = token
try:
  client = Client(account_sid, auth_token) 
 
  message = client.messages.create(  
                              from_= "+number",
                            #   messaging_service_sid=msg_sid, 
                              body='Hello everyone how are you', 
                              status_callback='http://postb.in/1234abcd',     
                              to='+number' 
                          ) 
 
  res_sid = message.sid
  res_date = message.date_sent
  res_err = message.error_message
  res_msg = message.status
  res_num = message.to

  print("sent to :",res_num," \n Status: ",res_msg,"\n Time:",res_date,"\n Error:",res_err)

except TwilioRestException as e:
        print("E:",e)
        print("E.code:",e.code)

