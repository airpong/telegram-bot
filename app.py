from flask import Flask , request
import os
import requests

app = Flask(__name__)

token=os.getenv('TELEGRAM_BOT_TOKEN')

@app.route("/")
def hello():
    return "Hello w!"
    
@app.route(f"/{token}",methods=['POST'])
def telegram():
    # 1. 구조 확인하기
    from_telegram = request.get_json() 
    print(from_telegram)
    #2. 그대로 돌려보내기(메아리)
    # ['message'] #-> 키가 없으면, 에러 발생!
    # get('message') #-> 키가 없으면, none 발생!
    if from_telegram.get('message') is not None:
        
        chat_id = from_telegram['message']['chat']['id']
        text = from_telegram['message']['text']
        # api.telegram.org => api.hphk.io/telegram
        requests.get(f'https://api.hphk.io/telegram/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
        print(chat_id)
        print(text)
    return '', 200

if __name__=='__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))