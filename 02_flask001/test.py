from flask import *  # 必要なライブラリのインポート

app = Flask(__name__)  # アプリの設定


@app.route("/")  # どのページで実行する関数か設定
def main():
    return "Hello, World! I am iron man"  # Hello, World! を出力

if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
