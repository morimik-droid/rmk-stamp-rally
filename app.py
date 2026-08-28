from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 仮のスタンプ・クーポン管理用データ構造
# 実際運用時はFirestore等のDBと連携します
@app.route('/')
def index():
    return render_template('index.html')

# クーポン消込用API
@app.route('/api/use-coupon', methods=['POST'])
def use_coupon():
    data = request.json or {}
    passcode = data.get('passcode')
    
    # スタッフ専用パスコードチェック（例: 7123）
    if passcode == '7123':
        return jsonify({"success": True, "message": "消込が完了しました！"})
    else:
        return jsonify({"success": False, "message": "パスコードが正しくありません"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
