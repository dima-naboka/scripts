
# coding: utf-8

# In[1]:


import dataiku
# from dataiku import pandasutils as pdu
import pandas as pd

client = dataiku.api_client()
projects = client.list_projects()
result_df = pd.DataFrame(columns=['project', 'connection', 'type', 'name'])

for p in projects :
    proj = client.get_project(p["projectKey"])
#     recipes = proj.list_recipes()
    datasets = []
    all_datasets = proj.list_datasets()
    for dataset in all_datasets:
        ds_type = dataset['type']
        ds_name = dataset['name']
        try:
            connection = dataset["params"]["connection"]
        except KeyError:
            connection = "unlisted connection"
        result_df = result_df.append({'project': p["projectKey"], 'connection': connection,'type': ds_type,'name':ds_name}, ignore_index=True)
#         print(p["projectKey"])
#         df = df.drop_duplicates()


# In[2]:


result_df


# In[3]:


for pr in projects:
    print(pr['projectKey'])

