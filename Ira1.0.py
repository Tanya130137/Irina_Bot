import time
import vk
from random import random
session1 = vk.Session(access_token='типо токен окда?')
ira = vk.API(session1, v='5.68')
stop=1
while True:
  a=ira.messages.get(count=1)
  f=a['items'][0]['read_state']
  otprav=a['items'][0]['user_id']
  variants=['Ира, off']
  variantson=['Ира, on']
  c=a['items'][0]['chat_id']
  b=a['items'][0]['body']
  d=int(random()*100)
  for i in variants:
    if i in b and f==0 :
      stop=1
      ira.messages.send(chat_id=c,message='Выключено')
  for i in variantson:
    if i in b and f==0:
      stop=0
      ira.messages.send(chat_id=c,message='Включено')
  if b=='help' and f==0:
    ira.messages.send(chat_id=c,message='Включить переворот - Ира, on. Выключить переворот - Ира, off. Помощь - help. Выслать исходники - исходники.')
  if b=='исходники' and f==0:
    ira.messages.send(chat_id=c,message='Держи *ссылка*')
  if f==0 and stop!=1:
    print(b)
  if len(b)>0 and f==0 and stop!=1 and b!='Ира, on':
    b=b[::-1]
    ira.messages.send(chat_id=c,message=b)
    time.sleep(1)
  time.sleep(1)
        
