# dataset settings
_base_ = 'coco_instance.py'
dataset_type = 'LVISV1Dataset'
<<<<<<< HEAD
data_root = 'data/lvis_v1/'
=======
#data_root = 'data/lvis_v1/'
data_root = 'data/ntu/'
>>>>>>> first-repo/main
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        _delete_=True,
        type='ClassBalancedDataset',
        oversample_thr=1e-3,
        dataset=dict(
            type=dataset_type,
<<<<<<< HEAD
            ann_file=data_root + 'annotations/lvis_v1_train.json',
            img_prefix=data_root)),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/lvis_v1_val.json',
        img_prefix=data_root),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/lvis_v1_val.json',
=======
            ann_file=data_root + 'annotations/train.json',
            #ann_file=data_root + 'annotations/lvis_v1_train.json',
            img_prefix=data_root)),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/valid.json',
        #ann_file=data_root + 'annotations/lvis_v1_val.json',
        img_prefix=data_root),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/valid.json',
        #ann_file=data_root + 'annotations/lvis_v1_val.json',
>>>>>>> first-repo/main
        img_prefix=data_root))
evaluation = dict(metric=['bbox', 'segm'])
