CUDA_VISIBLE_DEVICES='0,1'
PORT=${PORT:-29501}
python -m torch.distributed.launch --nproc_per_node=2 --master_port=$PORT \
    tools/train.py projects/configs/coDETR_r/co_deformable_detr_swin_base_3x_coco.py --launcher pytorch --work-dir ckpt/coDETR_swinB_3x_retrain_v1
    #tools/train.py projects/configs/co_deformable_detr/co_deformable_detr_swin_large_900q_3x_coco.py --launcher pytorch --work-dir ckpt/coDETR_swinB_3x_v1
