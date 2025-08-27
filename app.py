from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>POSTING DAILY RANDOM SHIT</h1>
    <p>[23/8/2025] Grow a Garden sucks</p>
    <p>[24/8/2025] Tibet...</p>
    <p>[25/8/2025] LIAR - Anakin skywalker</p>
    <p>[26/8/2025] "Go on and get your refund, motherfucker, I ain't dead" </p>
    <p>[27/8/2025] "Cause he got hit like I got hit, but he ain't fuckin' breathin" </p>
    """

@app.route('/google529aa2489f3093d9.html')
def google_verification():
    return send_from_directory('.', 'google529aa2489f3093d9.html')

if __name__ == '__main__':
    app.run(debug=True)










