from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📩 알림 받음:", data)
    # 여기에 MEXC 주문 코드 추가 예정
    return '', 200

@app.route('/', methods=['GET'])
def home():
    return '✅ 서버 작동 중'

if __name__ == '__main__':
    app.run(debug=True)
