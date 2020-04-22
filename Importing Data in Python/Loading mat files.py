# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')
#This file contains gene expression data from the Albeck Lab at UC Davis.

# Print the datatype type of mat
print(type(mat))
