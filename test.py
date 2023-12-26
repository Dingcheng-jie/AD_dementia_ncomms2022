from model_wrappers import Multask_Wrapper
from utils import read_json

model = Multask_Wrapper(
    tasks=['COG'],                            # a list of tasks to predict
    device=0,                                        # GPU device to use
    main_config={"csv_dir": "lookupcsv/CrossValid/cross0/", "model_name": "CNN_baseline_new_cross0"},            # general configuration for the experiment  
    task_config=read_json('task_config_ADNI1.json'),       # task specific configurations
    seed=1000
)                                       
model.train()                                                            
thres = model.get_optimal_thres()                    # get optimal threshold using validation dataset
model.gen_score(['test'], thres)                     # apply optimal threshold on test dataset and cache predictions