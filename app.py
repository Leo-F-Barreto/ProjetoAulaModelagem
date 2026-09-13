from flask import Flask, request, jsonify, render_template
from frete import calcular_frete

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    try:
        valor = float(data.get('valor', 0))
        regiao = data.get('regiao', '')
        frete_base = float(data.get('frete_base', 0))
        cupom = data.get('cupom', '')

        # RB-02: Exibir erro se o valor for inválido
        resultado = calcular_frete(valor, regiao, frete_base, cupom)
        return jsonify(resultado), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except Exception:
        return jsonify({"erro": "Erro interno no servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)