
import yt_dlp
url="https://www.youtube.com/watch?v=sTzf5UEi4P4"

ydl_opts = {
    'format': 'mp4',
    'outtmpl': '%(title)s.%(ext)s',
    'continuedl': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])