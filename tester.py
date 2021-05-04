from flask import Flask, render_template,request, redirect
from pytube import YouTube
import datetime
app = Flask(__name__)
@app.route('/', methods=["GET","POST"])
def index():
    time = datetime.datetime.now()
    now = time.strftime("%b-%a-%l:%M")
    if request.method == "POST":
        link = request.form['link']
        print("Link is "+link)
        #YouTube(link).streams[0].download('Desktop/')
        yt = YouTube(link)
        print("Video: "+yt.title)
        yt.streams.first().download('/home/sangeeth/Desktop')
        download_status = {
        'video_title': yt.title,
        'status': "completed"
        }
        return render_template('download.html', **download_status)

    template_data = {
        'name': 'Sangeeth',
        'time': now
    }
    return render_template('index.html', **template_data)

@app.route('/download')
def downloader():
    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')