from flask import Flask, render_template, request
from pytube import YouTube, Playlist
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    link = request.form["downloadLink"]
    yt = YouTube(link)
    print(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('./MyFolder')
    message = "Download is Complete"
    return render_template("index.html", message = message)


@app.route("/listDownload", methods=["POST"])
def listDownload():
    link = request.form["downloadLinkList"]
    p = Playlist(link)
    for url in p.video_urls:
        try:
            yt = YouTube(url)
        except Exception as e:
            # message = (f'Video {url} is unavaialable, skipping. {e}')
            print(e)
        else:
            print(link)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('./MyFolder')
            # message = yt.title
    
    return render_template("index.html", message = "List Complete")