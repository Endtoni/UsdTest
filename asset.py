import os
from pxr import Usd, UsdGeom
import utils


def main():
    """
    Construct the stage
    """
    directory = os.path.dirname(__file__)
    output_dir = utils.setup_workarea(directory)
    ref_stage_file = os.path.join(output_dir, 'ref.usda')

    ref_stage = utils.get_stage(ref_stage_file)
    utils.clear_stage(ref_stage)
    root_prim = ref_stage.DefinePrim('/root', 'Xform')
    ref_stage.SetDefaultPrim(root_prim)

    # Move sphere to (4, 5, 6)
    sphereTransformApi = UsdGeom.XformCommonAPI(root_prim)
    sphereTransformApi.SetTranslate((4, 5, 6))

    sphereShapePrim = UsdGeom.Sphere.Define(ref_stage, '/root/shape')
    print(ref_stage.GetRootLayer().ExportToString())
    ref_stage.GetRootLayer().Save()


if __name__ == '__main__':
    main()
