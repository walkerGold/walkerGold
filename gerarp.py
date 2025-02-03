from flask import Flask, jsonify, request, Response
import requests
import json

app = Flask(__name__)

@app.route('/gerar_pessoa', methods=['GET'])
def gerar_pessoa():

    url = "https://www.4devs.com.br/ferramentas_online.php"

    data = {
        "acao": "gerar_pessoa",
        "sexo": "I",
        "pontuacao": "S",
        "idade": "0",
        "cep_estado": "",
        "txt_qtde": "1",
        "cep_cidade": ""
    }

    try:

        response = requests.post(url, data=data)
        response.raise_for_status() 

        response.encoding = 'utf-8'

        try:
            json_response = response.json()
        except ValueError:

            return Response(response.text, mimetype='text/html')

        return Response(json.dumps(json_response, ensure_ascii=False), mimetype='application/json')
    except requests.exceptions.RequestException as e:

        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)