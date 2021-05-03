from flask import Flask, render_template
import datetime
app = Flask(__name__)
@app.route('/')
def index():
    time = datetime.datetime.now()
    now = time.strftime("%Y-%M-%D-%H:%M")
    template_data = {
        'name': 'Sangeeth',
        'time': now
    }
    return render_template('index.html', **template_data)
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')