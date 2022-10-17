import os
import utils
from pxr import Usd, UsdGeom


def add_reference(stage, path, reference_file):
    over_prim = stage.OverridePrim(path)
    references = over_prim.GetReferences()
    references.ClearReferences()
    references.AddReference(reference_file)
    return over_prim


def main():
    directory = os.path.dirname(__file__)
    output_dir = utils.setup_workarea(directory)
    ref_stage_file = os.path.join(output_dir, 'ref.usda')

    main_stage_file = os.path.join(output_dir, 'main.usda')
    main_stage = utils.get_stage(main_stage_file)
    utils.clear_stage(main_stage)

    ref1 = add_reference(main_stage, '/refSphere1', ref_stage_file)
    ref2 = add_reference(main_stage, '/refSphere2', ref_stage_file)

    # Reset ref1's xform to origin
    ref_xform = UsdGeom.Xformable(ref1)
    ref_xform.SetXformOpOrder([])

    # Set display color
    over_sphere = UsdGeom.Sphere.Get(main_stage, '/refSphere2/shape')
    over_sphere.GetDisplayColorAttr().Set([(1, 0, 0)])

    print(main_stage.GetRootLayer().ExportToString())
    main_stage.GetRootLayer().Save()


if __name__ == "__main__":
    main()

