
# coding: utf-8

# In[1]:


import dataiku
client = dataiku.api_client()
current_project = dataiku.api_client().get_project(dataiku.get_custom_variables()["projectKey"])


# In[3]:


recipes = current_project.list_recipes()
datasets = []

all_datasets = current_project.list_datasets()
for dataset in all_datasets:
    datasets.append(dataset["name"])
    
for recipe in recipes:
    inputs = recipe["inputs"]
    outputs = recipe["outputs"]
    input_keys = inputs.keys()
    output_keys = outputs.keys()
        
    for key in input_keys:
        if "items" in inputs[key]:
            for item in inputs[key]["items"]:
                dataset_name = item["ref"]
                if dataset_name in datasets:
                    datasets.remove(dataset_name)

    for key in output_keys:
        if "items" in outputs[key]:
            for item in outputs[key]["items"]:
                dataset_name = item["ref"]
                if dataset_name in datasets:
                    datasets.remove(dataset_name)

print(datasets)


# In[ ]:


# for dataset in datasets:
#     project_t.get_dataset(dataset).delete()
#     print(dataset)

