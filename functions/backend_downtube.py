from pytube import YouTube
from io import BytesIO


class Video():
    def __init__(self, url) -> None:
        try:
            self.dados = YouTube(url)

        except:
            return False

    def _download(self):

        buffer = BytesIO()

        tag = self.dados.streams.filter(only_audio=True).filter(abr="128kbps").itag_index.keys()
        tag = [k for k in tag]
        print('inicio')
        self.video = self.dados.streams.get_by_itag(tag[0])
        self.video.stream_to_buffer(buffer)
        buffer.seek(0)
        print('concluido')
        return buffer

    def getThumb(self):
        try:
            title = self.dados.title.replace('/','')
            return self.dados.thumbnail_url, title
        except:
            return None


# Video('https://www.youtube.com/watch?v=1z3tQh3LsgQ&list=RD1z3tQh3LsgQ&start_radio=1')._download()
