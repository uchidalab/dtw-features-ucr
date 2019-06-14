from utils.constants import max_seq_len, nb_classes, nb_dims
from utils.generic import train_model, evaluate_model
#from utils.models import cnn_raw_model, cnn_dtwfeatures_model, cnn_earlyfusion_model, cnn_midfusion_model, cnn_latefusion_model
from utils.models import cnn_midfusion_model_v2, lstm_model

import sys
import math
import numpy as np
import os

if __name__ == "__main__":
    dataset = sys.argv[1]
    method = sys.argv[2]
    proto_num = int(sys.argv[3])
    os.environ["CUDA_VISIBLE_DEVICES"]=sys.argv[4]

    max_seq_lenth = max_seq_len(dataset)
    nb_class = nb_classes(dataset)
    dim_num = nb_dims(dataset)
    nb_cnn = int(round(math.log(max_seq_lenth, 2))-3)


    #model = cnn_raw_model(nb_cnn, proto_num, max_seq_lenth, nb_class)
    #model = cnn_dtwfeatures_model(nb_cnn, proto_num, max_seq_lenth, nb_class)
    #model = cnn_earlyfusion_model(nb_cnn, proto_num, max_seq_lenth, nb_class)
    model = cnn_midfusion_model_v2(nb_cnn, dim_num, proto_num, max_seq_lenth, nb_class)
    #model = cnn_latefusion_model(nb_cnn, proto_num, max_seq_lenth, nb_class)

    print("Number of Pooling Layers: %s" % str(nb_cnn))

    train_model(model, dataset, method, proto_num, dataset_prefix=dataset, nb_iterations=50000, batch_size=32, normalize_timeseries=True, learning_rate=0.0001, early_stop=False, balance_classes=False)

    acc = evaluate_model(model, dataset, method, proto_num, dataset_prefix=dataset, batch_size=50, normalize_timeseries=True)
    np.savetxt("output/%s-%s-%s-%s" % (dataset, method, str(proto_num), str(acc)), [acc])
