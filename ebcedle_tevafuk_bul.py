from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

ebced_table = {
    'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
    'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80,
    'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600,
    'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
}

periodic_table = {
    26: 'Fe (Demir)',
    56: 'Ba (Baryum)',
    57: 'La (Lantan)',
    79: 'Au (Altın)',
    29: 'Cu (Bakır)',
    30: 'Zn (Çinko)'
}

def ebced_hesapla(kelime):
    return sum(ebced_table.get(harf, 0) for harf in kelime if harf in ebced_table)

def tevafuk_kontrol(deger):
    matches = []
    for numara, element in periodic_table.items():
        if abs(deger - numara) <= 1:
            matches.append({"element": element, "atom_no": numara})
    return matches

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    kelime = request.form['kelime']
    deger = ebced_hesapla(kelime)
    tevafuklar = tevafuk_kontrol(deger)
    return jsonify({"kelime": kelime, "ebced": deger, "tevafuklar": tevafuklar})

if __name__ == '__main__':
    app.run(debug=True)
    app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
    import os
    
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
