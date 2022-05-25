
# coding: utf-8

# In[1]:


import dataiku
import os
import re
import datetime as dt


# In[3]:


folder_path = dataiku.Folder("m8qucVGO")
today = dt.datetime.now().date()
current_project = dataiku.api_client().get_project(dataiku.get_custom_variables()["projectKey"])
variables = current_project.get_variables()

print('===')


# In[ ]:


for file_iter in files:
    if re.match(r"/my_file*", file_iter):
        print(folder_path.get_path_details(file_iter))


# In[3]:


for file_iter in folder_path.list_paths_in_partition():
    if re.match(r"/my_file*", file_iter):
#         print(folder_path.get_path_details(file_iter)['lastModified'])
#         print(dt.datetime.fromtimestamp(1615874998000/1000.0))
# divide by 1000.0 to convert millisec to sec
        filetime = dt.datetime.fromtimestamp(folder_path.get_path_details(file_iter)['lastModified']/1000.0)
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

