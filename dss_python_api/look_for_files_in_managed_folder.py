
# coding: utf-8

# In[1]:


import dataiku
import os
import re
import datetime as dt


# In[3]:


folder_path = dataiku.Folder("managed_ds").get_path()
managed_folder_name = "managed_ds"
today = dt.datetime.now().date()


# In[23]:


for file in dataiku.Folder(managed_folder_name).list_paths_in_partition():
#     print(folder_path+file)
    if re.match(r"/my_file*", file):
#         print (file)
        filetime = dt.datetime.fromtimestamp(os.path.getctime(folder_path+file))
        if filetime.date() == today:
#             print('today')
            current_project = dataiku.api_client().get_project(dataiku.get_custom_variables()["projectKey"])
            variables = current_project.get_variables()
            variables['standard']['file_uploaded_today'] = 'yes'
            current_project.set_variables(variables)


# In[26]:


# from dataiku.scenario import Trigger
# t = Trigger()

import dataiku
import os
import re
import datetime as dt
folder_path = dataiku.Folder("managed_ds").get_path()
today = dt.datetime.now().date()
current_project = dataiku.api_client().get_project(dataiku.get_custom_variables()["projectKey"])
variables = current_project.get_variables()

for file in dataiku.Folder("managed_ds").list_paths_in_partition():
    if re.match(r"/my_file*", file):
        filetime = dt.datetime.fromtimestamp(os.path.getctime(folder_path+file))
        if filetime.date() == today:
#             t.fire()
#             print(variables['standard'])
            try:
                variables['standard']['file_uploaded_today']
            except KeyError:
                print('no key')
                break
#             try:
#                 variables['standard']['file_uploaded_today'] == 'yes'
#             except KeyError:
#                 print('not yes')
            if not variables['standard']['file_uploaded_today'] == 'yes':
                print('not yes')
#                 if not variables['standard']['file_uploaded_today'] == 'yes':
#             if not(variables['standard']['file_uploaded_today'] == 'yes'):
#                     print('not yes')
#                 t.fire()

