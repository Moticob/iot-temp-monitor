from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_temperature():
    temperature = request.form.get('temperature')
    if temperature:
        with open('temperature_log.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()}: {temperature}\n")
        return "Logged successfully", 200
    return "Bad Request", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

