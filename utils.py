import os
from pxr import Usd

def setup_workarea(root):
    out_dir = os.path.join(root, 'output')
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    os.chdir(out_dir)
    return out_dir

def clear_stage(stage):
    stage.ClearDefaultPrim()

    # TODO: Didn't figure out the best way To remove the root prim
    root_paths = []
    for prim in stage.Traverse():
        path = prim.GetPath()
        if path.pathElementCount == 1:
            root_paths.append(path)
    for i in root_paths:
        stage.RemovePrim(i)

def get_stage(full_path):
    if os.path.isfile(full_path):
        return Usd.Stage.Open(full_path)
    return Usd.Stage.CreateNew(full_path)