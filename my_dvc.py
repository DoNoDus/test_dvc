from dvc.api import DVCFileSystem

repository_path  = r'D:/mlflow/mlflow_learning/'
fs = DVCFileSystem(repository_path)
url = 'https://github.com/DoNoDus/test_dvc.git'
fs = DVCFileSystem(url, rev='main')

print('hello')