from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return "POSTING RANDOM DAILY SHIT"

@app.route('/google529aa2489f3093d9.html')
def google_verification():
    return send_from_directory('.', 'google529aa2489f3093d9.html')

if __name__ == '__main__':
    app.run(debug=True)



