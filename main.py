
import os

from pxr import Usd, UsdGeom
import shutil


def setup_workarea(root):
    out_dir = os.path.join(root, 'output')
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    return out_dir


def get_stage(full_path):
    if os.path.isfile(full_path):
        return Usd.Stage.Open(full_path)
    return Usd.Stage.CreateNew(full_path)


if __name__ == '__main__':
    directory = os.path.dirname(__file__)
    output_dir = setup_workarea(directory)

    main_stage_file = os.path.join(output_dir, 'main.usda')
    ref_stage_file = os.path.join(output_dir, 'ref.usda')

    main_stage = get_stage(main_stage_file)
    ref_stage = get_stage(ref_stage_file)

    main_stage.RemovePrim('/root')

    rootTransformPrim = main_stage.DefinePrim('/root', 'Xform')
    sphereTransformPrim = main_stage.DefinePrim('/root/sphere', 'Xform')

    sphereTransformApi = UsdGeom.XformCommonAPI(sphereTransformPrim)
    sphereTransformApi.SetTranslate((4, 5, 6))
    cubeTransformPrim = main_stage.DefinePrim('/root/cube', 'Xform')
    sphereShapePrim = UsdGeom.Sphere.Define(main_stage, '/root/sphere/sphereShape')
    cubeShapePrim = main_stage.DefinePrim('/root/cube/cubeShape', 'Cube')
    main_stage.GetRootLayer().Save()