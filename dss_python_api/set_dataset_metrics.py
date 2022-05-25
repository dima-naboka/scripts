
# coding: utf-8

# In[1]:


import dataiku
import json
client = dataiku.api_client()
current_project = client.get_project(dataiku.get_custom_variables()["projectKey"])


# In[ ]:


list_of_datasets = ['fd','SFPD_Reports_partitioned_PdDistrict_copy','dimension_by_district_rolling','partt']
columns_of_interest=['type','Date','DayOfWeek','district_copy','Date_last']

# col_stat_json['configuration']['aggregates'] = col_stat_aggr


# In[ ]:


for dataset in list_of_datasets:
    ds = current_project.get_dataset(dataset)
    ds_settings = ds.get_settings()
    ds_metrics = ds_settings.get_raw()['metrics']
    compute_metrics=[]

    col_stat_json={u'computeOnBuildMode': u'NO',
    u'configuration': {u'aggregates': []},
    u'enabled': True,
    'meta': {u'level': 2, u'name': u'Columns statistics'},
    u'type': u'col_stats'}
    
    for cl in columns_of_interest:
#         print('first for:%s'%cl)
        for index in range(len(ds.get_schema()[u'columns'])):
#             print('second for:%s cl:%s'% (ds.get_schema()[u'columns'][index][u'name'],cl))
            if cl == ds.get_schema()[u'columns'][index][u'name']:
#                 print(ds.get_schema()[u'columns'][index][u'name'])
                print('column:%s, dataset:%s'% (cl,dataset))
                compute_metrics.append('col_stats:COUNT:'+cl)
                compute_metrics.append('col_stats:COUNT_DISTINCT:'+cl)
                col_stat_json['configuration']['aggregates'].append({u'aggregated': u'COUNT', u'column': cl})
                col_stat_json['configuration']['aggregates'].append({u'aggregated': u'COUNT_DISTINCT', u'column': cl})


#     compute_metrics=[]
#     compute_metrics.extend('col_stats:COUNT:'+cl for cl in columns_of_interest)
#     compute_metrics.extend('col_stats:COUNT_DISTINCT:'+cl for cl in columns_of_interest)

#     col_stat_json['configuration']['aggregates'].extend({u'aggregated': u'COUNT', u'column': cl} for cl in columns_of_interest)
#     col_stat_json['configuration']['aggregates'].extend({u'aggregated': u'COUNT_DISTINCT', u'column': cl} for cl in columns_of_interest)

    
    # Status/Edit/General settings tab 
    #in case any additional metrics are enabled or "Columns statistics" metrics were enabled but disabled afterwards
    try:
        ds_metrics['probes'][3] = col_stat_json
    except:
        ds_metrics['probes'].append(col_stat_json)
        
    #Status/Metrics/Metrics to display pop-up
    ds_metrics['displayedState']['metrics'].extend(compute_metrics)
    
    #Saving settings
    ds_settings.save()
    
    #Compute metrics could take some time
    ds.compute_metrics(metric_ids=compute_metrics)


# In[ ]:


# ds_tt = current_project.get_dataset('SFPD_Reports_prepared_prepared')
# # ds_tt_cols = ds_tt.get_schema()['columns']
# # ds_tt.get_schema()['columns'][0]
# ds_tt_settings = ds_tt.get_settings()
# ds_tt_metrics = ds_tt_settings.get_raw()['metrics']
# ds_tt_metrics['probes'][3]['configuration']['aggregates']

# # for cl in columns_of_interest:
# #     for index in range(len(ds_tt_cols)):
# #         if cl in ds_tt_cols[index]['name']:
# #             col_stat_json['configuration']['aggregates'].append({u'aggregated': u'COUNT', u'column': cl})
# #             col_stat_json['configuration']['aggregates'].append({u'aggregated': u'COUNT_DISTINCT', u'column': cl})

