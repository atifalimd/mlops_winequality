import os

#folder required
dirs=[
    #os.path.join("base directory","child directory")
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebook",
    "saved_models",
    "src"
]
'''exist_ok=True-->if the dir is not created will create and if it is created will simply ignore
    exist_ok=True-->if the dir is not created will create and and if it is created will throw error'''
for dir in dirs:
    os.makedirs(dir,exist_ok=True)
    with open(os.path.join(dir,".gitkeep"), "w") as f:
        pass
    


files=[
"dvc.yaml",
"params.yaml",
os.path.join("src","__init__.py")
]

for file in files:
    with open(file,"w") as f:
        pass