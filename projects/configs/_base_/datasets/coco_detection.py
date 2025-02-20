# dataset settings
dataset_type = 'CocoDataset'
<<<<<<< HEAD
data_root = 'data/coco/'
=======
#data_root = 'data/coco/'
data_root = 'data/ntu/'
>>>>>>> first-repo/main
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
<<<<<<< HEAD
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
=======
    dict(type='Resize', img_scale=(1024, 800), keep_ratio=True),
    #dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
>>>>>>> first-repo/main
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
<<<<<<< HEAD
        img_scale=(1333, 800),
=======
        img_scale=(1024, 800),
        #img_scale=(1333, 800),
>>>>>>> first-repo/main
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
<<<<<<< HEAD
        ann_file=data_root + 'annotations/instances_train2017.json',
        img_prefix=data_root + 'train2017/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/instances_val2017.json',
        img_prefix=data_root + 'val2017/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/instances_val2017.json',
        img_prefix=data_root + 'val2017/',
=======
        ann_file=data_root + 'annotations/train.json',
        img_prefix=data_root + 'train/',
        #ann_file=data_root + 'annotations/instances_train2017.json',
        #img_prefix=data_root + 'train2017/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/val.json',
        img_prefix=data_root + 'valid/',
        #ann_file=data_root + 'annotations/instances_val2017.json',
        #img_prefix=data_root + 'val2017/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/test.json',
        img_prefix=data_root + 'test/',
        #ann_file=data_root + 'annotations/val.json',
        #img_prefix=data_root + 'valid/',
        #ann_file=data_root + 'annotations/instances_val2017.json',
        #img_prefix=data_root + 'val2017/',
>>>>>>> first-repo/main
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric='bbox')
