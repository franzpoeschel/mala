import os

import mala
from mala import printout

from mala.datahandling.data_repo import data_repo_path
data_path = os.path.join(data_repo_path, "Be2")


test_parameters = mala.Parameters()

test_parameters.targets.target_type = "LDOS"
test_parameters.targets.ldos_gridsize = 11
test_parameters.targets.ldos_gridspacing_ev = 2.5
test_parameters.targets.ldos_gridoffset_ev = -5

data_converter = mala.DataConverter(test_parameters)
ldosfile = os.path.join(data_path, "cubes/tmp.pp*Be_ldos.cube")
data_converter.add_snapshot(target_input_type=".cube",
                            target_input_path=ldosfile,
                            target_units="1/(Ry*Bohr^3)")
data_converter.convert_snapshots(target_save_path="./",
                                 naming_scheme="Be_snapshot_only_out*.bp")