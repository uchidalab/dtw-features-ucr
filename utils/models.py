from keras.models import Model
from keras.layers import Input, Dense, multiply, concatenate, Activation, Lambda
from keras.layers import Conv1D, BatchNormalization, GlobalAveragePooling1D, Permute, Dropout
from keras.layers import MaxPooling1D, Flatten


TRAINABLE = True



def cnn_raw_model(nb_cnn, proto_num, max_seq_lenth, nb_class):
    ip1 = Input(shape=(1, max_seq_lenth))
    ip2 = Input(shape=(proto_num, max_seq_lenth))

    x = Permute((2, 1))(ip1)

    for i in range(nb_cnn):
        x = Conv1D(256, 3, padding='same', kernel_initializer='he_uniform')(x)
        x = Activation('relu')(x)
        x = MaxPooling1D(pool_size=2)(x)

    x = Flatten()(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    out = Dense(nb_class, activation='softmax')(x)

    model = Model(ip, out)

    model.summary()

    return model

def cnn_dtwfeatures_model(nb_cnn, proto_num, max_seq_lenth, nb_class):
    ip1 = Input(shape=(1, max_seq_lenth))
    ip2 = Input(shape=(proto_num, max_seq_lenth))

    x = Permute((2, 1))(ip2)

    for i in range(nb_cnn):
        x = Conv1D(256, 3, padding='same', kernel_initializer='he_uniform')(x)
        x = Activation('relu')(x)
        x = MaxPooling1D(pool_size=2)(x)

    x = Flatten()(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    out = Dense(nb_class, activation='softmax')(x)

    model = Model([ip1, ip2], out)

    model.summary()

    return model

def cnn_earlyfusion_model(nb_cnn, proto_num, max_seq_lenth, nb_class):
    ip1 = Input(shape=(1, max_seq_lenth))
    ip2 = Input(shape=(proto_num, max_seq_lenth))

    x1 = Permute((2, 1))(ip1)
    x2 = Permute((2, 1))(ip2)
    x = concatenate([x1, x2])

    for i in range(nb_cnn):
        x = Conv1D(256, 3, padding='same', kernel_initializer='he_uniform')(x)
        x = Activation('relu')(x)
        x = MaxPooling1D(pool_size=2)(x)

    x = Flatten()(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    out = Dense(nb_class, activation='softmax')(x)

    model = Model([ip1, ip2], out)

    model.summary()

    return model

def cnn_midfusion_model(nb_cnn, proto_num, max_seq_lenth, nb_class):
    ip1 = Input(shape=(1, max_seq_lenth))
    ip2 = Input(shape=(proto_num, max_seq_lenth))

    x1 = Permute((2, 1))(ip1)
    x2 = Permute((2, 1))(ip2)

    for i in range(nb_cnn):
        x1 = Conv1D(256, 3, padding='same', kernel_initializer='he_uniform')(x1)
        x1 = Activation('relu')(x1)
        x1 = MaxPooling1D(pool_size=2)(x1)

        x2 = Conv1D(256, 3, padding='same', kernel_initializer='he_uniform')(x2)
        x2 = Activation('relu')(x2)
        x2 = MaxPooling1D(pool_size=2)(x2)


    x = concatenate([x1, x2])

    x = Flatten()(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    out = Dense(nb_class, activation='softmax')(x)

    model = Model([ip1, ip2], out)

    model.summary()

    return model

def cnn_midfusion_model_v2(nb_cnn, dim_num, proto_num, max_seq_lenth, nb_class):
    ip1 = Input(shape=(dim_num, max_seq_lenth))
    ip2 = Input(shape=(proto_num, max_seq_lenth))

    x1 = Permute((2, 1))(ip1)
    x2 = Permute((2, 1))(ip2)

    for i in range(nb_cnn):
        i_prime = i if i < 2 else 2
        nb_nodes = 64 * 2 ** i_prime

        x1 = Conv1D(nb_nodes, 3, padding='same', kernel_initializer='he_uniform')(x1)
        x1 = Activation('relu')(x1)
        x1 = MaxPooling1D(pool_size=2)(x1)

        x2 = Conv1D(nb_nodes, 3, padding='same', kernel_initializer='he_uniform')(x2)
        x2 = Activation('relu')(x2)
        x2 = MaxPooling1D(pool_size=2)(x2)


    x = concatenate([x1, x2])

    x = Flatten()(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    out = Dense(nb_class, activation='softmax')(x)

    model = Model([ip1, ip2], out)

    model.summary()

    return model


def cnn_latefusion_model(nb_cnn, proto_num, max_seq_lenth, nb_class):
    ip1 = Input(shape=(1, max_seq_lenth))
    ip2 = Input(shape=(proto_num, max_seq_lenth))

    x1 = Permute((2, 1))(ip1)
    x2 = Permute((2, 1))(ip2)

    for i in range(nb_cnn):
        x1 = Conv1D(256, 3, padding='same', kernel_initializer='he_uniform')(x1)
        x1 = Activation('relu')(x1)
        x1 = MaxPooling1D(pool_size=2)(x1)

        x2 = Conv1D(256, 3, padding='same', kernel_initializer='he_uniform')(x2)
        x2 = Activation('relu')(x2)
        x2 = MaxPooling1D(pool_size=2)(x2)

    x1 = Flatten()(x1)
    x2 = Flatten()(x2)

    x1 = Dense(1024, activation='relu')(x1)
    x1 = Dropout(0.5)(x1)

    x1 = Dense(1024, activation='relu')(x1)
    x1 = Dropout(0.5)(x1)

    x2 = Dense(1024, activation='relu')(x1)
    x2 = Dropout(0.5)(x1)

    x2 = Dense(1024, activation='relu')(x2)
    x2 = Dropout(0.5)(x2)

    x = concatenate([x1, x2])

    out = Dense(nb_class, activation='softmax')(x)

    model = Model([ip1, ip2], out)

    model.summary()

    return model


def vgg_raw_model(nb_cnn, proto_num, max_seq_lenth, nb_class):
    ip1 = Input(shape=(1, max_seq_lenth))
    ip2 = Input(shape=(proto_num, max_seq_lenth))

    x = Permute((2, 1))(ip1)

    for i in range(nb_cnn):
        i_prime = i if i < 3 else 3
        nb_nodes = 64 * 2 ** i_prime

        x = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x)
        x = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x)
        if i > 2:
            x = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x)

        x = MaxPooling1D(pool_size=2)(x)

    x = Flatten()(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    out = Dense(nb_class, activation='softmax')(x)

    model = Model([ip1, ip2], out)

    model.summary()

    return model

def vgg_dtwfeatures_model(nb_cnn, proto_num, max_seq_lenth, nb_class):
    ip1 = Input(shape=(1, max_seq_lenth))
    ip2 = Input(shape=(proto_num, max_seq_lenth))
    x = Permute((2, 1))(ip2)

    for i in range(nb_cnn):
        i_prime = i if i < 3 else 3
        nb_nodes = 64 * 2 ** i_prime

        x = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x)
        x = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x)
        if i > 2:
            x = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x)

        x = MaxPooling1D(pool_size=2)(x)

    x = Flatten()(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    out = Dense(nb_class, activation='softmax')(x)

    model = Model([ip1, ip2], out)

    model.summary()

    return model

def vgg_earlyfusion_model(nb_cnn, proto_num, max_seq_lenth, nb_class):
    ip1 = Input(shape=(1, max_seq_lenth))
    ip2 = Input(shape=(proto_num, max_seq_lenth))

    x1 = Permute((2, 1))(ip1)
    x2 = Permute((2, 1))(ip2)
    x = concatenate([x1, x2])

    for i in range(nb_cnn):
        i_prime = i if i < 3 else 3
        nb_nodes = 64 * 2 ** i_prime

        x = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x)
        x = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x)
        if i > 2:
            x = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x)

        x = MaxPooling1D(pool_size=2)(x)

    x = Flatten()(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    out = Dense(nb_class, activation='softmax')(x)

    model = Model([ip1, ip2], out)

    model.summary()

    return model

def vgg_midfusion_model(nb_cnn, proto_num, max_seq_lenth, nb_class):
    ip1 = Input(shape=(1, max_seq_lenth))
    ip2 = Input(shape=(proto_num, max_seq_lenth))

    x1 = Permute((2, 1))(ip1)
    x2 = Permute((2, 1))(ip2)

    for i in range(nb_cnn):
        i_prime = i if i < 3 else 3
        nb_nodes = 64 * 2 ** i_prime

        x1 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x1)
        x1 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x1)

        x2 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x2)
        x2 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x2)
        if i > 2:
            x1 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x1)

            x2 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x2)

        x1 = MaxPooling1D(pool_size=2)(x1)
        x2 = MaxPooling1D(pool_size=2)(x2)


    x = concatenate([x1, x2])

    x = Flatten()(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)

    out = Dense(nb_class, activation='softmax')(x)

    model = Model([ip1, ip2], out)

    model.summary()

    return model


def vgg_latefusion_model(nb_cnn, proto_num, max_seq_lenth, nb_class):
    ip1 = Input(shape=(1, max_seq_lenth))
    ip2 = Input(shape=(proto_num, max_seq_lenth))

    x1 = Permute((2, 1))(ip1)
    x2 = Permute((2, 1))(ip2)

    for i in range(nb_cnn):
        i_prime = i if i < 3 else 3
        nb_nodes = 64 * 2 ** i_prime

        x1 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x1)
        x1 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x1)

        x2 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x2)
        x2 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x2)
        if i > 2:
            x1 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x1)

            x2 = Conv1D(nb_nodes, 3, padding='same', activation='relu', kernel_initializer='he_uniform')(x2)

        x1 = MaxPooling1D(pool_size=2)(x1)
        x2 = MaxPooling1D(pool_size=2)(x2)

    x1 = Flatten()(x1)
    x2 = Flatten()(x2)

    x1 = Dense(1024, activation='relu')(x1)
    x1 = Dropout(0.5)(x1)

    x1 = Dense(1024, activation='relu')(x1)
    x1 = Dropout(0.5)(x1)

    x2 = Dense(1024, activation='relu')(x1)
    x2 = Dropout(0.5)(x1)

    x2 = Dense(1024, activation='relu')(x2)
    x2 = Dropout(0.5)(x2)

    x = concatenate([x1, x2])

    out = Dense(nb_class, activation='softmax')(x)

    model = Model([ip1, ip2], out)

    model.summary()

    return model
