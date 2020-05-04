##
# For this class structure inlcude the import needed
# The full api function used even if renamed
# Possible error returns and checks for the errors
## 
'''
class [NAME](object):
    def __init__(self):
        ##For Attributes use convention [NAME]_?[MODOL]_[PARAM]
        ## [NAME]__user_download_path
        ## [NAME]_get_files_list_result
        ## [NAME]_entries_to_download_list

    def [NAME]_authentication(self):
        #This is for the authentication of the class, include anything neccessary to do so here

    def [NAME]_get_files_list(self):
        #This is a generic template for gathering files
        #Often this may have a list of file entires as a return

    def [NAME]_format_entries_list(self):
        #This function will take the return of [NAME]_get_files_list
        #And provide the neccessary information to pass to a dropdown select menu

    def [NAME]_select_entries_to_download(self):
        #May be an uneeded function, but will generate a list to pass to the download function
    
    def [NAME]_get_user_download_path(self):
        #This function will allow users to select where they want the items to download
        #The default being set in the __init__ as downloads

    def [NAME]_download_selected_entries(self, list_of_selected_downloads=null, path):
        #This function will download the list returned by [NAME]_select_entries_to_download
        #Using the [NAME]__usr_download_path will then download the files.
'''