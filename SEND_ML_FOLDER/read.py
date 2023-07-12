import h5py

# Open the H5 file
h5_file = h5py.File('mbpp.h5', 'r')

# Iterate over the keys (dataset names)
for dataset_name in h5_file.keys():
    print(dataset_name)

# Close the H5 file
h5_file.close()
