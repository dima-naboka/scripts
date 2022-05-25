
# coding: utf-8

# In[1]:


import dataiku
import json
current_project = dataiku.api_client().get_project(dataiku.get_custom_variables()["projectKey"])


# In[2]:


all_project_datasets = current_project.list_datasets()

for dataset_item in all_project_datasets:
#     if isinstance(settings,dataikuapi.dss.dataset.SQLDatasetSettings):
    if dataset_item['type'] in 'PostgreSQL,MySQL':      
        dataset = current_project.get_dataset(dataset_item['name'])
        settings = dataset.get_settings()
        print("=== processing %s dataset ===" % dataset.name)
#         print(json.dumps(dataset_item['params'],sort_keys=True, indent=4))
#         print(json.dumps(settings.get_raw(),sort_keys=True, indent=4))
        settings.get_raw()['params']['schema'] = '${schema}'
        settings.save()
        print('=== END ===')

