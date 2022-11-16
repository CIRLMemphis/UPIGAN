"""
    author: SPDKH
    date: Nov 2, 2022
"""


import sys

import tensorflow as tf
from tensorflow.keras.models import Model

# ________________ architecture Variants
from models import CGAN, CAGAN

from utils.fcns import show_all_variables
from utils.config import parse_args
from utils.data_loader import data_loader


def main():
    """
        Main Training Function
    """

    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

    # parse arguments
    args = parse_args()
    if args is None:
        sys.exit()

    # open session
    model_fns = {'CAGAN': CAGAN, 'CGAN': CGAN}

    data = data_loader()
    # declare instance for GAN
    dnn = model_fns[args.dnn_type](args)

    # build graph
    dnn.build_model()

    # show network architecture
    show_all_variables()

    # launch the graph in a session
    dnn.train()
    print(" [*] Training finished!")

    # visualize learned generator
    dnn.visualize_results(args.epoch-1)
    print(" [*] Validation finished!")


if __name__ == '__main__':
    main()