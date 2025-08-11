from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📩 알림 받음:", data)
    return '', 200

@app.route('/', methods=['GET'])
def home():
    return '✅ 서버 작동 중'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render가 제공하는 포트 사용
    app.run(host='0.0.0.0', port=port)
