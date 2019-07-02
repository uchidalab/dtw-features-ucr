import utils.dtw as dtw
import time
import numpy as np
import os
import csv
import sys


if __name__ == "__main__":
    version = sys.argv[1]
    length = int(sys.argv[2])

    print("Starting: {}".format(version))

    # load settings
    full_train_file = os.path.join("data", version + "_TRAIN")

    # load data
    full_train = np.genfromtxt(full_train_file, delimiter=',')[:,1:].reshape((-1, length, 1))


    # print(proto_number)

    train_number = np.shape(full_train)[0]

    fileloc = os.path.join("data", "all-"+version + "-dtw-matrix.txt")

    with open(fileloc, 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, delimiter=" ")
        for t1 in range(train_number):
            writeline = np.zeros((train_number))
            for t2 in range(train_number):
                writeline[t2] = dtw.dtw(full_train[t1], full_train[t2], extended=False)
            writer.writerow(writeline)
            print(t1)

print("Done")
