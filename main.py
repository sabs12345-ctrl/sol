from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    signal = data.get('message')

    if signal == "LONG 진입":
        print("LONG 주문 실행")
    elif signal == "SHORT 진입":
        print("SHORT 주문 실행")

    return "OK", 200

if __name__ == '__main__':
    app.run()
