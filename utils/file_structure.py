import os

def get_file_structure_dict(root_dir):
    structure = {}

    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        
        if os.path.isdir(path):
            structure[item] = get_file_structure_dict(path)
        else:
            structure[item] = path  

    return structure
