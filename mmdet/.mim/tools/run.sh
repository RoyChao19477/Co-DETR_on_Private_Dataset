python -m torch.distributed.launch --nproc_per_node=2 --master_port=-29500 \
    tools/train.py projects/configs/co_deformable_detr/co_deformable_detr_swin_base_3x_coco.py --launcher pytorch --work-dir ckpt/coDETR_swinB_3x_v1
