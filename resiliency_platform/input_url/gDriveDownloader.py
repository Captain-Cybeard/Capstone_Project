from __future__ import print_function
import pickle
import os.path
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#googleapiclient.discovery.build
#googleapiclient.discovery.build.files().list()
#googleapiclient.http.MediaIoBaseDownload
#google_auth_oauthlib.flow.InstalledAppFlow
#google.auth.transport.requests.Request


class GDriveDownloader():
    def __init__(self,creds=None,service=None):
        self.GDriveDownloader_creds = creds
        self.GDriveDownloader_SCOPES = ['https://www.googleapis.com/auth/drive']
        self.GDriveDownloader_service = service
        self.GDriveDownloader_file_List = None
        self.GDriveDownloader_json = None

    def GDriveDownloader_authentication(self):
        # If there are no (valid) credentials available, let the user log in.
        if not self.GDriveDownloader_creds or not self.GDriveDownloader_creds.valid:
            if self.GDriveDownloader_creds and self.GDriveDownloader_creds.expired and self.GDriveDownloader_creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('client_secret_204730000731-c0gs1os80ucalj6mto9c1etmaee70is7.apps.googleusercontent.com.json', self.GDriveDownloader_SCOPES)
                self.GDriveDownloader_creds = flow.run_local_server(port=0)

    def GDriveDownloader_save_Token(self):
        with open('token.pickle', 'wb') as token:
            pickle.dump(self.GDriveDownloader_creds, token)

    def GDriveDownloader_load_Token(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

    def GDriveDownloader_build_Service(self):
        self.GDriveDownloader_service = build('drive', 'v3', credentials=self.GDriveDownloader_creds)

    def GDriveDownloader__download_File(self,file_Id):
        request = self.GDriveDownloader_service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download {}%".format(int(status.progress() * 100)))

    def GDriveDownloader__get_Files(self):
        page_token = None
        while True:
            self.GDriveDownloader_file_List = self.GDriveDownloader_service.files().list(spaces='drive', fields='nextPageToken, items(id, title)', pageToken=page_token).execute()
            for file in self.GDriveDownloader_file_List.get('items', []):
                # Process change
                #print 'Found file: %s (%s)' % (file.get('title'), file.get('id'))
                print(file.get('title'))
            page_token = self.GDriveDownloader_file_List.get('nextPageToken', None)
            if page_token is None:
                break




