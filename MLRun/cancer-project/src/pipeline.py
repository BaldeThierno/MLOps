import pandas as pd
from sklearn.datasets import load_breast_cancer

import mlrun
project = mlrun.get_or_create_project("cancer-project", context="./", user_project=False)
dataprep_fn = project.set_function("data-prep.py", name="data-prep", kind="job", image="mlrun/mlrun", handler="breast_cancer_generator")
run_id = project.run(
    workflow_path="./src/workflow.py",
    arguments={"model_name": "cancer-classifier"},
    watch= True
)