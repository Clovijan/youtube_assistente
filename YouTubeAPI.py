from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os
import json


class YouTubeAPI:
    scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']

    def __init__(self, credentials_path):
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.credentials_path = credentials_path
        self.youtube = self.authenticate()

    def authenticate(self):
        credentials = self.get_credentials()
        youtube = build(self.api_service_name, self.api_version,
                        credentials=credentials)
        return youtube


    def get_api_key(self):
        with open(self.credentials_path, "r") as file:
            credentials = self.get_credentials()
            api_key = credentials['web']['api_key']
        return api_key

    def get_credentials(self):
        credentials = None

        # Check if credentials file exists
        if os.path.exists(self.credentials_path):
            credentials = self.load_credentials()

        # If there are no (valid) credentials available, let the user log in.
        if not credentials or 'valid' not in credentials or not credentials['valid']:
            if credentials and 'expired' in credentials and credentials['expired'] and 'refresh_token' in credentials:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, scopes=self.scopes)
                credentials = flow.run_local_server(
                    host='localhost', port=8080, open_browser=True)

            # Save the credentials for the next run
            self.save_credentials(credentials)

        return credentials

    def load_credentials(self):
        credentials = None
        with open(self.credentials_path, "rb") as file:
            credentials = json.load(file)
        return credentials

    def save_credentials(self, credentials):
        token_path = "token.pickle"
        with open(token_path, "wb") as file:
            pickle.dump(credentials, file)
