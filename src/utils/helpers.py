import wandb
import os
from constants import *
from maths import *
from typing import Union
from file_manager import dump_data, load_data_from_path

def create_directory_tree(directory_structure: str, parent_path: str):
    """
    Recursively creates folders based on the provided directory structure dictionary.

    Parameters:
    - directory_structure (dict): The dictionary representing the directory structure.
    - parent_path (str): The parent path where the folders should be created. Default is the current directory.
    """
    for folder_name, subfolders in directory_structure.items():
        folder_path = os.path.join(parent_path, folder_name)

        os.makedirs(folder_path, mode=777, exist_ok=True)

        if subfolders:
            create_directory_tree(subfolders, folder_path)

def connect_to_wandb(project: str, 
                    run_id_path: str,
                    run_name: str) -> None:
    
    # Additional runtime checks if needed
    assert isinstance(project, str), "project_name should be a string"
    assert isinstance(run_id_path, str), "run_id_path should be a string"
    assert isinstance(run_name, str), "run_name should be a string"

    run_id = None
    resume = None 
    
    try:
        run_ids = load_data_from_path(run_id_path)
        
        if run_ids is None:
            run_ids = dict()

        if run_name in run_ids.keys():
            run_id = run_ids[run_name]
            resume = "must"
    except:
        print(f"{run_id_path} has been created")

    finally:
    
        wandb.init(project = project, name = run_name, id = run_id, resume = resume)

        # If the run is created for the first time, we will associate the run id to the run name
        # We want that this file could not be directly accessed by the user
        not_exist_run_name = (os.path.exists(run_id_path)) \
                        and (run_name not in run_ids.keys()) \
                        or (not os.path.exists(run_id_path))
        
        if not_exist_run_name:
            run_ids[run_name] = wandb.run.id
            dump_data(run_ids, run_id_path)


# connect_to_wandb(project="fg", run_name="Bal", run_id_path="run_ids.bin")