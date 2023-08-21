import os
import shutil
# origin = '../duplicate-checker'
target = './duplicate-files'
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

 
install_and_import('difPy')
# folders = next(os.walk('./duplicate-image'))
folders = []
for path, subfolders, filenames in os.walk('./duplicate-image'):
    for filename in filenames:
        folders.append("/".join(f"{path}/{filename}".split("/")[:-1]))

folders = list(set(folders))
print(f"searching in {folders}")
search = difPy.dif(folders)
# print(search.result)

for key, data in search.result.items():
    location = data["location"]
    matches = data["matches"]
    for k, d in matches.items():
        print(f"{location} image has dublicate: {d['location']}")
        loc = d['location']
        splitloc = "/".join(loc.split("/")[:-1])
        os.makedirs(f"{target}/{splitloc}", exist_ok = True)
        shutil.copy(loc,f"{target}/{splitloc}")
        print("removed file in : =>  ",loc)