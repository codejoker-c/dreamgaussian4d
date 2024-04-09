import argparse

import numpy as np
from plyfile import PlyData

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="path to the yaml config file")
    args = parser.parse_args()

    plydata = PlyData.read(args.path)

    print(np.asarray(plydata.elements[0]["x"].shape[0]))
