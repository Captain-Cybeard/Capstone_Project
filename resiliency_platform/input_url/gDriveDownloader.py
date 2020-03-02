from __future__ import print_function
import pickle
import os.path
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GDriveDownloader():
    def __init__(self,creds=None,service=None):
        self.creds = creds
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.service = service
        self.fileList = None

    def authToGoogle(self):
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('client_secret_204730000731-ua1e5ag1foa5c089g1hka58vc849bvfs.apps.googleusercontent.com.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)

    def saveToken(self):
        with open('token.pickle', 'wb') as token:
            pickle.dump(self.creds, token)

    def loadToken(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

    def buildService(self):
        self.service = build('drive', 'v3', credentials=self.creds)

    def downloadFile(self,file_Id):
        request = self.service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download {}%".format(int(status.progress() * 100)))

    def getFiles(self):
        page_token = None
        while True:
            self.fileList = self.service.files().list(spaces='drive', fields='nextPageToken, items(id, title)', pageToken=page_token).execute()
            for file in self.fileList.get('items', []):
                # Process change
                #print 'Found file: %s (%s)' % (file.get('title'), file.get('id'))
                print(file.get('title'))
            page_token = self.fileList.get('nextPageToken', None)
            if page_token is None:
                break




