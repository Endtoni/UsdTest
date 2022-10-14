from pxr import Usd, UsdGeom
import os

output_dir = os.path.join(os.path.join(os.path.dirname(__file__), ))
main_stage = os.path.join(os.path.dirname(__file__), 'main.usda')
ref_stage = os.path.join(os.path.dirname(__file__), 'ref.usda')


def setup_workarea(path):









if __name__ == '__main__':

out_dir = r"C:\Users\Administrator\Documents\usdOutput"
if not os.path.isdir(out_dir):
    os.makedirs(out_dir)
file_name = 'newName.usda'
os.chdir(out_dir)


full_path = os.path.join(out_dir, file_name)
if os.path.isfile(full_path):
    stage = Usd.Stage.Open(file_name)
else:
    stage = Usd.Stage.CreateNew(file_name)
stage.RemovePrim('/root')

rootTransformPrim = stage.DefinePrim('/root', 'Xform')
sphereTransformPrim = stage.DefinePrim('/root/sphere', 'Xform')

sphereTransformApi = UsdGeom.XformCommonAPI(sphereTransformPrim)
sphereTransformApi.SetTranslate((4, 5, 6))

cubeTransformPrim = stage.DefinePrim('/root/cube', 'Xform')
#xformPrim = stage.DefinePrim('/hello', 'Xform')
sphereShapePrim = UsdGeom.Sphere.Define(stage, '/root/sphere/sphereShape')
cubeShapePrim = stage.DefinePrim('/root/cube/cubeShape', 'Cube')

stage.GetRootLayer().Save()