#!/bin/python
import dropbox

#####################################################################
# dropbox.oauth.DropboxOAuth2FlowNoRedirect(key, secret)
# dropbox.oauth.DropboxOAuth2FlowNoRedirect(key, secret).start()
# dropbox.oauth.DropboxOAuth2FlowNoRedirect(key, secret).finish(code)
# dropbox.dropbox.Dropbox(access_token)
# dropbox.dropbox.Dropbox(access_token).list_folder_result(path)
#   returns: dropbox.files.Metadata()
#       includes:   files.Metadata.name
#                   files.Metadata.path_lower 
#                   files.Metadata.path_display 
#                   files.Metadata.parent_shared_folder_id
#   raises: dropbox.exceptions.ApiError()
#       includes:   request_id
#                   error 
#                   user_message_text
# dropbox.dropbox.Dropbox(access_token).files_list_folder_continue(cursor)
#   retuns: dropbox.files.Metadata()
#   raises: dropbox.exceptions.ApiError()
#dropbox.dropbox.Dropbox(access_token).files_download_to_file(download_path, path)
#   returns: dropbox.files.FileMetadata()
#       includes:   files.FileMetadata.id
#                   files.FileMetadata.client_modified
#                   files.FileMetadata.server_modified 
#                   files.FileMetadata.rev 
#                   files.FileMetadata.size 
#                   files.FileMetadata.media_info 
#                   files.FileMetadata.symlink_info 
#                   files.FileMetadata.sharing_info 
#                   files.FileMetadata.is_downloadable 
#                   files.FileMetadata.export_info 
#                   files.FileMetadata.property_groups
#                   files.FileMetadata.has_explicit_shared_members  
#                   files.FileMetadata.content_hash
####################################################################


'''
POSSIBLY USEFUL FOR WEBSITE
from selenium import webdriver

options = webdriver.ChromeOptions() 
options.add_argument("download.default_directory=C:/Downloads")

driver = webdriver.Chrome(chrome_options=options)
'''

class DropBox(object):
    def __init__(self):
        self.dropbox_api_key = 'xq8jbecr17pq4sm'
        self.dropbox_api_secret = 'tyz24n7zoq2e090'
        self.dropbox_authentication_auth_flow = ""
        self.dropbox_authentication_authorize_url = ""
        self.dropbox_authentication_auth_code = ""
        self.dropbox_authentication_oauth_result = ""
        self.dbx = ""
        self.dropbox_get_files_return = ""
        self.dropbox_get_files_list_result = []
        self.dropbox_entries_to_download_list = []
        self.dropbox_download_path = "/mnt/c/Users/tsesu/Downloads/"

    def dropbox_authentication(self):
        self.dropbox_authentication_auth_flow = dropbox.oauth.DropboxOAuth2FlowNoRedirect(self.dropbox_api_key, self.dropbox_api_secret)
        self.dropbox_authentication_authorize_url = self.dropbox_authentication_auth_flow.start()
        print("1. Go to: " + self.dropbox_authentication_authorize_url)
        print("2. Click \"Allow\" (you might have to log in first)")
        print("3. Copy the authorization code.")
        self.dropbox_authentication_auth_code = raw_input("Enter the authorization code here: ").strip()

        try:
            self.dropbox_authentication_oauth_result = self.dropbox_authentication_auth_flow.finish(self.dropbox_authentication_auth_code)
        except Exception, e:
            print("Error: %s" % (e,))

        self.dbx = dropbox.dropbox.Dropbox(self.dropbox_authentication_oauth_result.access_token) #renaming for readability

    def dropbox_get_files_list(self):
        self.dropbox_get_files_list_return = self.dbx.files_list_folder("", recursive=True)
        for dropbox_files in self.dropbox_get_files_listing.entries:
            self.dropbox_get_files_list_result.append(dropbox_files)
    
        return self.dropbox_get_files_list_result

    def dropbox_format_entries_list(self):
        folders = []
        files = []
        for file_names in self.dropbox_get_files_list_result:
            for second_file_names in self.dropbox_get_files_list_result:
                if file_names.name.lower() + "/" in second_file_names.path_lower:
                    if file_names not in folders:
                        folders.append(file_names)

    def dropbox_select_entries_to_download(self):
        number_string = raw_input("\nPlease select files to download by number: ")
        print("Selected Files:")
        for numbers in number_string:
            if(numbers != " "):
                self.dropbox_entries_to_download_list.append(self.dropbox_get_files_list_result[int(numbers)])
        for e in self.dropbox_entries_to_download_list:
            print(e.name)
'''
    def dropbox_download_selected_entries(self, list_of_selected_downloads=null, path):
        #this function will download the list of specified files to the path given by the user
'''

##Main
test = DropBox()
test.dropbox_authentication()

#This functionality will need to be a function of the dropbox class that will allow the 
#user to select specific files, later to be integrated into a check box format
file_list = test.dropbox_get_files_list()

test.format_entries_list()    
test.select_entries_to_download()

# #This functionality will be used for the actual download capability, taking the list of files the user 
# #would like to download and downloading them to the desktop -> this can later be set by the user
# download_path = "/mnt/c/Users/tsesu/Downloads/"

# for numbers in number_string:
#     if(numbers != " "):
#         path = file_list[int(numbers)].path_lower
#         print(path)
# #dbx.files_download_to_file(download_path, path)