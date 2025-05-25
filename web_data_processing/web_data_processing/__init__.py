from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('dev-secret-key')

# mock api endpoint that will be replaced by the go microservice
@app.route('/api/traffic-data')
def get_traffic_data():

    # some placeholder data
    sample_data = {
        'data_1': 12345
    }
    return jsonify(sample_data)

# route for homepage
@app.route('/')
def index():
    return render_template('dashboard.html', title='Traffic Data Dashboard')

@app.route('/statistics')
def statistics():
    return render_template('dashboard.html', title='Statistics')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')