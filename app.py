# app.py
from flask import Flask, request, jsonify, render_template
from frete import calcular_frete

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    if not data:
        return jsonify({"erro": "Nenhum dado enviado"}), 400

    try:
        valor = float(data.get('valor', 0))
        regiao = data.get('regiao', '')
        frete_base = float(data.get('frete_base', 20.0))
        cupom = data.get('cupom', '')

        # Chama a função de domínio
        resultado = calcular_frete(valor, regiao, frete_base, cupom)

        # Normaliza o retorno para JSON, já que a função pode retornar float ou dict
        if isinstance(resultado, dict):
            valor_final = resultado["valor_carrinho"]
            frete = resultado["frete_calculado"]
        else:
            valor_final = valor
            frete = resultado

        total = valor_final + frete

        # Resposta otimizada para RF-02 (baixo tempo de resposta)
        return jsonify({
            "valor_carrinho": round(valor_final, 2),
            "frete": round(frete, 2),
            "total": round(total, 2)
        }), 200

    except ValueError as e:
        # RB-02: Retorna HTTP 400 em caso de erro na regra de domínio
        return jsonify({"erro": str(e)}), 400
    except Exception:
        return jsonify({"erro": "Erro interno no servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)