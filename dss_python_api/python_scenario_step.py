import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import uuid
from dataiku.scenario import Scenario
PARTNER = 'IHG'
MODEL_TYPE = 'BG'
proj_handle = dataiku.api_client().get_project("IHG_AUTO_V1_1")
proj_var = proj_handle.get_variables()
# Create the main handle to interact with the scenario
scen = Scenario()
step = scen.get_previous_steps_outputs()
# Score #
result_date = ([d for d in step if d['stepName']=='query_date'])[0]['result']
new_score_date = result_date['rows'][0][0]

# train #
result_train_ref_date = ([d for d in step if d['stepName']=='train_ref_date'])[0]['result']
new_train_date = result_train_ref_date['rows'][0][0]

# valid #
result_valid_ref_date = ([d for d in step if d['stepName']=='valid_ref_date'])[0]['result']
new_valid_date = result_valid_ref_date['rows'][0][0]

#previous value
cur_score_date = proj_var["standard"]["scoring_file_date"]
cur_train_date = proj_var["standard"]["train_file_date"]

if new_score_date != cur_score_date:
    proj_var["standard"]["validation_file_date"] = new_valid_date
    proj_var["standard"]["scoring_file_date"] = new_score_date
    proj_var["standard"]["current_file_date"] = new_score_date
    proj_var["standard"]["train_file_date"] = new_train_date
    proj_var["standard"]["last_scoring_file_date"] = cur_score_date
    # date used to calculate the date difference in train data, validation and score
    proj_var["standard"]["train_substract_date"] = proj_var["standard"]["train_file_date"] + '01'
    proj_var["standard"]["validation_substract_date"] = proj_var["standard"]["validation_file_date"] + '01'
    proj_var["standard"]["scoring_substract_date"] = proj_var["standard"]["scoring_file_date"] + '01'
    proj_handle.set_variables(proj_var)
else:
    pass
