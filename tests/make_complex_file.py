""" 
Create HDF5 files with a complex datatype using
(1) the netcdf interface, and
(2) the h5py interface 
"""
from netCDF4 import Dataset
import numpy as np

# native complex
complex_array = np.array([0 + 0j, 1 + 0j, 0 + 1j, 1 + 1j, 0.25 + 0.75j])
# compound complex
complex128 = np.dtype(
    {
        "names": ["r", "i"],
        "formats": ["f8", "f8"],
        "offsets": [0, 8],
        "itemsize": 16,
        "aligned": True,
    }
)
cdata = np.array(
    [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (0.25, 0.75)], dtype=complex128
)

with Dataset("complex_variable.nc", "w", auto_complex=True) as ds:
    ds.createDimension("x", size=len(complex_array))
    var = ds.createVariable("data", "c16", ("x",))
    var[:] = complex_array
