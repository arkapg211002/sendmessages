import requests
import json
url="https://www.fast2sms.com/dev/bulk"
my_data={'sender_id':'FSTSMS','message':'This is a test message','language':'english','route':'p','numbers':'9143629729,8910062338'}
headers={'authorization':'RlinTOf8vIS7hg15yG3osbNKjJaH2AVc6ZMd9pmuq0WFUwPzreumohnsyGNO6wUgQ4k1j9AS5rbDClF8','content-Type':"application/x-www-form-urlencoded",'Cache-Control':"no-cache"}
response=requests.request("POST",url,data=my_data,headers=headers)
returned_msg=json.loads(response.text)
print(returned_msg['message'])