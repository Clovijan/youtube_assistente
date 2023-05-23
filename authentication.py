from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Defina as informações de autenticação
client_id = '858706138504-sgrrc3pgck2tliikhpu4si4f02pi42qn.apps.googleusercontent.com'
client_secret = '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'
scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']

# Configuração do fluxo de autenticação
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secrets.json',
    scopes=scopes
)
credentials = flow.run_local_server(host='localhost',
                                    port=8080,
                                    open_browser=True)

# Criação do serviço da API do YouTube
youtube_service = build('youtube', 'v3', credentials=credentials)

response = youtube_service.search().list(
    part='snippet',
    channelId='UCL88vArV8o7RaCUV2pMbFmw',
    type='video'
).execute()

videos = response['items']
for video in videos:
    print(video['snippet']['title'])
