"""Module providing configuration for training on human parsing with mobilenetv2
backbone"""

from glob import glob

import tensorflow as tf


CONFIG = {
    'project_name': 'deeplabv3-plus',
    'experiment_name': 'human-parsing-mobilenet-v2-backbone-polylr',

    'train_dataset_config': {
        'images': sorted(
            glob(
                './dataset/instance-level_human_parsing/'
                'instance-level_human_parsing/Training/Images/*'
            )
        ),
        'labels': sorted(
            glob(
                './dataset/instance-level_human_parsing/'
                'instance-level_human_parsing/Training/Category_ids/*'
            )
        ),
        'height': 512, 'width': 512, 'batch_size': 8
    },

    'val_dataset_config': {
        'images': sorted(
            glob(
                './dataset/instance-level_human_parsing/'
                'instance-level_human_parsing/Validation/Images/*'
            )
        ),
        'labels': sorted(
            glob(
                './dataset/instance-level_human_parsing/'
                'instance-level_human_parsing/Validation/Category_ids/*'
            )
        ),
        'height': 512, 'width': 512, 'batch_size': 8
    },

    'strategy': tf.distribute.OneDeviceStrategy(device="/gpu:0"),

    'num_classes': 20,
    'backbone': 'mobilenetv2',
    'learning_rate': tf.keras.optimizers.schedules.PolynomialDecay(
        0.007, 0.9997, end_learning_rate=0.0001,
        power=1.0, cycle=False, name=None
    ),

    'checkpoint_dir': "./checkpoints/",
    'checkpoint_file_prefix':
    'deeplabv3-plus-human-parsing-mobile-net-v2-backbone_',

    'epochs': 100
}