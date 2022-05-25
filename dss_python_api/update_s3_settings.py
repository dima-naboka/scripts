
# coding: utf-8

# In[24]:


import dataiku
import json
client = dataiku.api_client()
current_project = client.get_project(dataiku.get_custom_variables()["projectKey"])


# In[3]:


datasets = current_project.list_datasets()


# In[48]:


for d in datasets:
    dataset = current_project.get_dataset(d["name"])
    settings = dataset.get_settings()
    raw_settings = settings.get_raw()
    if raw_settings['type'] != 'S3':
        continue
    else:
        print('updating "%s" settings' %raw_settings['name'])
#         print(json.dumps(client.get_connection(name=raw_settings["params"]["connection"]).get_definition()['params'],indent=2))
#         break
        raw_settings["params"]["metastoreDatabaseName"] = client.get_connection(name=raw_settings["params"]["connection"]).get_definition()['params']['defaultMetastoreDatabase']
        raw_settings["params"]["metastoreTableName"] =  raw_settings['name'] + client.get_connection(name=raw_settings["params"]["connection"]).get_definition()['params']['namingRule']['metastoreTableNameDatasetNamePrefix']
        settings.save()
# #         print('BEFORE DELETE %s' %json.dumps(raw_settings['params'],indent=2))
#         try:
#             del raw_settings["params"]["metastoreDatabaseName"]
#         except Exception:
#             pass
#         try:
#             settings.save()
#         except Exception:
#             pass
# #         print('AFTER DELETE %s' %json.dumps(raw_settings['params'],indent=2))
        break

