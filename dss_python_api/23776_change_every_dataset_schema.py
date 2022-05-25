
# coding: utf-8

# In[1]:


import dataiku
import json
#print(json.dumps(job,indent=4))

client = dataiku.api_client()
current_project = client.get_project(dataiku.get_custom_variables()["projectKey"])
variables = current_project.get_variables()
general_settings = client.get_general_settings()


# In[2]:


all_datasets = current_project.list_datasets()


# In[6]:


for dataset_list_item in all_datasets:
    dataset = current_project.get_dataset(dataset_list_item["name"])
    dataset_settings = dataset.get_settings()
    if dataset_settings.get_raw()['type'] == 'Snowflake':
        print('===')
        print('original %s schema'%dataset_list_item["name"])
        print(json.dumps(dataset_settings.schema_columns,indent=2))
        for index in range(len(dataset_list_item['schema']['columns'])):
            if dataset_settings.schema_columns[index]['type'] == 'bigint':
                dataset_settings.schema_columns[index]['type'] = 'int'
                dataset_settings.save()
        print('updated %s schema'%dataset_list_item["name"])
        print(json.dumps(dataset_settings.schema_columns,indent=2))

#     print(json.dumps(dataset_settings.get_raw()['type'],indent=2))

