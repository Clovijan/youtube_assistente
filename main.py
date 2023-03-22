from youtube_transcript_api import YouTubeTranscriptApi


# A partir do ID do vídeo ele recupera as legendas de um vídeo

def getcaption(idVideo):
    transcript = YouTubeTranscriptApi.get_transcript(
        idVideo, languages=['pt'])
    print(transcript)
    return transcript
