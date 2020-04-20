# Import pickle package
import pickle

# Open pickle file and load data: d using datafile name: data.pkl and read only mode for binary format 'rb'
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))
