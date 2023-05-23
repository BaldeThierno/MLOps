import mlrun
project = mlrun.get_or_create_project("fromjenkins", context="./", user_project=True)