
# coding: utf-8

# In[1]:


import dataiku
import pandas as pd
# import xlsxwriter

client = dataiku.api_client()
project = client.get_project(dataiku.get_custom_variables()["projectKey"])
datasets = project.list_datasets()

# tag_name = 'sql_dataset'

result_dict = {'dataset':[],'tags':[]}
for index in range(len(datasets)):
    if datasets[index]['tags']:
#         if tag_name in datasets[index]['tags']:
#         result_dict = {'dataset':[],'tag':[]}
        result_dict['dataset'].append(datasets[index]['name'])
        result_dict['tags'].append(datasets[index]['tags'])
df = pd.DataFrame(data=result_dict)
# df.to_excel('output1.xlsx', engine='xlsxwriter')
df.to_excel('output1.xlsx')
#             print "dataset '{}' is tagged with '{}'".format(datasets[index]['name'],tag_name)
#         if datasets[index]['tags']=='sql_dataset':

#     if tag == 'sql_dataset':
#         print (datasets[index]['tags'])


# In[ ]:


df

