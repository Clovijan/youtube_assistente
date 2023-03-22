from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator

# A partir do ID do vídeo ele recupera as legendas desse vídeo


def getCaption(idVideo):
    transcript = YouTubeTranscriptApi.get_transcript(
        idVideo, languages=['pt'])
    return transcript


def tradutor(transcript):
    translator = Translator()
    translated = translator.translate(transcript, src="pt", dest='en').text
    return translated


print(tradutor('ola mundo'))
