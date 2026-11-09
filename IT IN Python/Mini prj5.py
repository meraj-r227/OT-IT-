# Better  Understanding  of nested  dict  
# We  have  something  called  API.telegram.org  
#That  tells  us which  key  the  user pressed  last  
# note :  only  someone  who has  my  token  can  find  this  out  
# not  just anyone  can  access  this  part  
 
import  requests
import json
Token =  "writ your  Token  Bot"
http = requests.get("api.telegram/bot{Token}/Getupdates").text
 
print(http) 
# we  can  change  str  to  dict  with  json
data =json.loads(http)

print(data)
print(data.keys())
print(data.values())
print(data['result'][0]['message']['text'])


mylist = [{"key1":"value1"},{"key2":"value2"}]
print(mylist[0]['key1'])