import numpy as np

from experiments import init_experiment, QuickParams, DefaultParams, FineParams
from observations import DataMatrix


###
### First follow the configuration directions in README.md. Then run the following:
###
###     python example.py
###     python experiments.py everything example
###

def read_array(fname):
    return np.array([list(map(float, line.split())) for line in open(fname)])


def read_list(fname):
    return list(map(str.strip, open(fname).readlines()))


def init():
    X = read_array('example_data/motion_capture/Crouch1_M.txt')
    print(X.shape)
    row_labels = None  # read_list('example_data/animals-names.txt')
    col_labels = None  # read_list('example_data/animals-features.txt')

    # normalize to zero mean, unit variance

    X = X[0: 200, 0:45]

    X -= X.mean()
    X /= X.std()
    # since the data were binary, add a small amount of noise to prevent degeneracy
    X = np.random.normal(X, np.sqrt(0.1))

    data_matrix = DataMatrix.from_real_values(X)  # , row_labels=row_labels, col_labels=col_labels)
    init_experiment('motion', data_matrix, FineParams(search_depth=3))


if __name__ == '__main__':
    init()



