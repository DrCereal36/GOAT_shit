from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>POSTING DAILY RANDOM SHIT</h1>
    <p>[23/8/2025] Grow a Garden sucks</p>
    """

@app.route('/google529aa2489f3093d9.html')
def google_verification():
    return send_from_directory('.', 'google529aa2489f3093d9.html')

if __name__ == '__main__':
    app.run(debug=True)







