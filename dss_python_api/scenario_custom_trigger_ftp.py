from dataiku.scenario import Trigger
t = Trigger()

import dataiku
import os
import re
import datetime as dt

folder_path = dataiku.Folder("m8qucVGO")
today = dt.datetime.now().date()
current_project = dataiku.api_client().get_project(dataiku.get_custom_variables()["projectKey"])
variables = current_project.get_variables()

for file_iter in folder_path.list_paths_in_partition():
    if re.match(r"/my_file*", file_iter):
#this code is for remote managed folders
#local filesystem works with         
#         filetime = dt.datetime.fromtimestamp(os.path.getctime(folder_path.get_path()+file))
        filetime = dt.datetime.fromtimestamp(folder_path.get_path_details(file_iter)['lastModified']/1000.0)
        if filetime.date() == today:
            try:
                variables['standard']['file_uploaded_today']
            except KeyError:
                t.fire()
                break
            if not variables['standard']['file_uploaded_today'] == 'yes':
                t.fire()
