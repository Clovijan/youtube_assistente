from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator


def getCaption(idVideo):  # A partir do ID do vídeo ele recupera as legendas desse vídeo
    transcript = YouTubeTranscriptApi.get_transcript(
        idVideo, languages=['pt'])
    return transcript


def tradutor(transcript):
    translator = Translator()
    translated = ""
    translated = list(map(lambda x: translator.translate(x,
                      src="en", dest='pt').text, transcript))
    return translated


legendas = getCaption("RWIbWaCS0YM")
legendasExtraídas = list(map(lambda x: x['text'], legendas))

print(legendasExtraídas)
