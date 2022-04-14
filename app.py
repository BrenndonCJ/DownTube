from flask import Flask, render_template, request, url_for, redirect, send_file, session
from io import BytesIO

from functions.backend_downtube import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "POST" and request.form.get('link'):
        session['link'] = request.form.get('link')
        try:
            url = Video(session['link'])
            print(url)
            dados = url.getThumb()
            if url:
                return render_template('index.html', convert=True, thumb_url=dados[0], video_title=dados[1])
        except:
            return "FAILED"

    return render_template('index.html', convert=False)

@app.route("/download", methods = ["GET", "POST"])
def download_video():
    if request.method == "POST":
        url = Video(session['link'])
        dados = url.getThumb()
        archiv = url._download()
        print('video',archiv)
        return send_file(archiv, as_attachment=True, download_name=dados[1]+'.mp3', mimetype="audio/mp4")

    return redirect(url_for("home"))
        

if __name__ == "__main__":
    # app.run(host= '192.168.2.108', port='5000', debug=True)
    app.run(host= '192.168.2.108', port='5000', debug=True)