import os
from ase.io import read
import mala
from mala.datahandling.data_repo import data_repo_path
data_path = os.path.join(data_repo_path, "Be2")

# Trigger LAMMPS by performing inference on an atomic snapshot.
parameters, network, data_handler, predictor = mala.Predictor.\
    load_run("be_model", path="basic")
atoms = read(os.path.join(data_path, "Be_snapshot3.out"))
ldos = predictor.predict_for_atoms(atoms)
ldos_calculator: mala.LDOS = predictor.target_calculator
ldos_calculator.read_from_array(ldos)

# Test OpenPMD.
params = mala.Parameters()
ldos_calculator = mala.LDOS. \
    from_numpy_file(params,
                    os.path.join(data_path,
                                 "Be_snapshot1.out.npy"))
ldos_calculator. \
    read_additional_calculation_data(os.path.join(data_path,
                                                  "Be_snapshot1.out"),
                                     "espresso-out")

# Write and then read in via OpenPMD and make sure all the info is
# retained.
# for key, val in os.environ.items():
#     print("\t{}:{}".format(key, val))
ldos_calculator.write_to_openpmd_file("test_openpmd.bp4",
                                      ldos_calculator.
                                      local_density_of_states)