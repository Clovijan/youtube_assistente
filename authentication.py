# Importe as bibliotecas necessárias
from YouTubeAPI import YouTubeAPI

# Caminho para o arquivo de credenciais da API e chave da API
credentials_path = 'client_secrets.json'

# Crie uma instância da classe YouTubeAPI
youtube_api = YouTubeAPI(credentials_path)

# Autentique no canal
youtube = youtube_api.youtube
my_channel = youtube.channels().list(
    part='contentDetails',
    mine=True
).execute()

channel_id = my_channel['items'][0]['id']

# Liste os 10 primeiros vídeos do canal autenticado
videos = youtube.search().list(
    part='snippet',
    channelId=channel_id,
    maxResults=10,
    order='date'
).execute()

for video in videos['items']:
    video_id = video['id']['videoId']
    title = video['snippet']['title']
    print(f"Video ID: {video_id}")
    print(f"Title: {title}")
    print("----------------------")
