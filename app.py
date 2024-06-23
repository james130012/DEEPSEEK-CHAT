from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    api_key = data['apiKey']
    model = data['model']
    messages = data['messages']
    temperature = data.get('temperature', 1.0)

    client = openai.OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=False
    )

    return jsonify(response.choices[0].message.content)

if __name__ == '__main__':
    app.run(debug=True)
