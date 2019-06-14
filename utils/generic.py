import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

import warnings
warnings.simplefilter('ignore', category=DeprecationWarning)

from keras.models import Model
from keras.layers import Permute
from keras.optimizers import Adam, SGD, Nadam
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, TensorBoard, CSVLogger, EarlyStopping
from keras import backend as K

from utils.constants import max_seq_len, nb_classes, nb_dims


def load_dataset(index, method, proto_num, normalize_timeseries=False, verbose=True) -> (np.array, np.array):
    dim = nb_dims(index) 

    train_data1 = "data/all-raw-train-data-%s-%s-%s.txt" % (index, method, str(proto_num))
    test_data1 = "data/all-raw-test-data-%s-%s-%s.txt" % (index, method, str(proto_num))

    train_data2 = "data/all-dtw_features-train-data-%s-%s-%s.txt" % (index, method, str(proto_num))
    test_data2 = "data/all-dtw_features-test-data-%s-%s-%s.txt" % (index, method, str(proto_num))

    train_labels = "data/all-train-label-%s-%s-%s.txt" % (index, method, str(proto_num))
    test_labels = "data/all-test-label-%s-%s-%s.txt" % (index, method, str(proto_num))


    is_timeseries = True # assume all input data is univariate time series

    if os.path.exists(train_data1):
        df = pd.read_csv(train_data1, delimiter=' ', header=None, encoding='latin-1')
    else:
        raise FileNotFoundError('File %s not found!' % (train_data1))
    X_train1 = df.values
    X_train1 = np.reshape(X_train1, (np.shape(X_train1)[0], dim, int(np.shape(X_train1)[1]/(dim))))

    if normalize_timeseries:
        X_train1_min = np.min(X_train1)
        X_train1_max = np.max(X_train1)
        X_train1 = 2. * (X_train1 - X_train1_min) / (X_train1_max - X_train1_min) - 1.

    if os.path.exists(train_data2):
        df = pd.read_csv(train_data2, delimiter=' ', header=None, encoding='latin-1')
    else:
        raise FileNotFoundError('File %s not found!' % (train_data2))

    X_train2 = df.values
    X_train2 = np.reshape(X_train2, (np.shape(X_train2)[0], proto_num, int(np.shape(X_train2)[1]/(proto_num))))

    if normalize_timeseries:
        X_train2_min = np.min(X_train2)
        X_train2_max = np.max(X_train2)
        X_train2 = 2. * (X_train2 - X_train2_min) / (X_train2_max - X_train2_min) - 1.

    if os.path.exists(train_labels):
        df = pd.read_csv(train_labels, delimiter=' ', header=None, encoding='latin-1')
    else:
        raise FileNotFoundError('File %s not found!' % (train_labels))

    y_train = df[[1]].values

    no_classes = nb_classes(index) #len(np.unique(y_train))


    if os.path.exists(test_data1):
        df = pd.read_csv(test_data1, delimiter=' ', header=None, encoding='latin-1')
    else:
        raise FileNotFoundError('File %s not found!' % (test_data1))
    X_test1 = df.values
    X_test1 = np.reshape(X_test1, (np.shape(X_test1)[0], dim, int(np.shape(X_test1)[1]/(dim))))

    if normalize_timeseries:
        X_test1 = 2. * (X_test1 - X_train1_min) / (X_train1_max - X_train1_min) - 1.

    if os.path.exists(test_data2):
        df = pd.read_csv(test_data2, delimiter=' ', header=None, encoding='latin-1')
    else:
        raise FileNotFoundError('File %s not found!' % (test_data2))

    X_test2 = df.values
    X_test2 = np.reshape(X_test2, (np.shape(X_test2)[0], proto_num, int(np.shape(X_test2)[1]/(proto_num))))

    if normalize_timeseries:
        X_test2 = 2. * (X_test2 - X_train2_min) / (X_train2_max - X_train2_min) - 1.

    if os.path.exists(test_labels):
        df = pd.read_csv(test_labels, delimiter=' ', header=None, encoding='latin-1')
    else:
        raise FileNotFoundError('File %s not found!' % (test_labels))

    y_test = df[[1]].values

    if verbose:
        print("Finished loading test dataset..")
        print()
        print("Number of train samples : ", X_train1.shape[0], "Number of test samples : ", X_test1.shape[0])
        print("Number of classes : ", no_classes)
        print("Sequence length : ", X_train1.shape[-1])


    return X_train1, X_train2, y_train, X_test1, X_test2, y_test, is_timeseries


def train_model(model:Model, dataset_id, method, proto_num, dataset_prefix, nb_iterations=100000, batch_size=128, val_subset=None, cutoff=None, normalize_timeseries=False, opt='Adam', learning_rate=1e-3, early_stop=False, balance_classes=True):
    X_train1, X_train2, y_train, X_test1, X_test2, y_test, is_timeseries = load_dataset(dataset_id, method, proto_num, normalize_timeseries=normalize_timeseries)

    #calculate num of batches
    nb_epochs = math.ceil(nb_iterations * (batch_size / X_train1.shape[0]))

    if balance_classes == True:
        classes = np.arange(0, nb_classes(dataset_id))
        le = LabelEncoder()
        y_ind = le.fit_transform(y_train.ravel())
        recip_freq = len(y_train) / (len(le.classes_) * np.bincount(y_ind).astype(np.float64))
        class_weight = recip_freq[le.transform(classes)]

        print("Class weights : ", class_weight)

    y_train = to_categorical(y_train, nb_classes(dataset_id))
    y_test = to_categorical(y_test, nb_classes(dataset_id))

    reduce_lr = ReduceLROnPlateau(monitor='loss', patience=math.ceil(nb_epochs / 20), mode='auto',
                                  factor=1/2., cooldown=0, min_lr=learning_rate/10., verbose=2)

    model_checkpoint = ModelCheckpoint("./weights/%s_%s_%s_weights.h5" % (dataset_prefix, method, str(proto_num)), verbose=2, monitor='loss', save_best_only=True, save_weights_only=True)

    tensorboard = TensorBoard(log_dir='./logs/%s_%s_%s' % (dataset_prefix, method, str(proto_num)), batch_size=batch_size)
    csv_logger = CSVLogger('./logs/%s_%s_%s.csv' % (dataset_prefix, method, str(proto_num)))
    if early_stop:
        early_stopping = EarlyStopping(monitor='loss', patience=500, mode='auto', verbose=2, restore_best_weights=True)
        callback_list = [model_checkpoint, early_stopping, tensorboard, csv_logger]
    else:
        callback_list = [model_checkpoint, tensorboard, csv_logger]

    if opt == 'SGD':
        optm = SGD(lr=learning_rate, momentum=0.9, decay=5e-4)
    elif opt == 'Nadam':
        optm = Nadam(lr=learning_rate)
    elif opt == 'Adam_decay':
        optm = Adam(lr=learning_rate, decay=9./nb_iterations)
    else:
        optm = Adam(lr=learning_rate)

    model.compile(optimizer=optm, loss='categorical_crossentropy', metrics=['accuracy'])

    if balance_classes:
        model.fit([X_train1, X_train2], y_train, batch_size=batch_size, epochs=nb_epochs, callbacks=callback_list,
              class_weight=class_weight, verbose=2, validation_data=([X_test1, X_test2], y_test))
    else:
        model.fit([X_train1, X_train2], y_train, batch_size=batch_size, epochs=nb_epochs, callbacks=callback_list, verbose=2, validation_data=([X_test1, X_test2], y_test))


def evaluate_model(model:Model, dataset_id, method, proto_num, dataset_prefix, batch_size=128, test_data_subset=None, cutoff=None, normalize_timeseries=False):
    X_train1, X_train2, y_train, X_test1, X_test2, y_test, is_timeseries = load_dataset(dataset_id, method, proto_num, normalize_timeseries=normalize_timeseries)
    
    y_test = to_categorical(y_test, nb_classes(dataset_id))

    optm = Adam(lr=1e-3)
    model.compile(optimizer=optm, loss='categorical_crossentropy', metrics=['accuracy'])

    model.load_weights("./weights/%s_%s_%s_weights.h5" % (dataset_prefix, method, str(proto_num)))


    print("\nEvaluating : ")
    loss, accuracy = model.evaluate([X_test1, X_test2], y_test, batch_size=batch_size)
    print()
    print("Final Accuracy : ", accuracy)

    return accuracy


