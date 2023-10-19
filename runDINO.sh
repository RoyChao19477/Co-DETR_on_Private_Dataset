CUDA_VISIBLE_DEVICES='0'
PORT=${PORT:-29501}
python -m torch.distributed.launch --nproc_per_node=1 --master_port=$PORT \
    tools/train.py projects/configs/coDETR_r/co_dino_5scale_swin_large_16e_o365tococo.py --launcher pytorch --work-dir ckpt/co_dino_5scale_lsj_swin_large_3x_coco__batch4_v5
    #tools/train.py projects/configs/coDETR_r/co_deformable_detr_swin_base_100x_coco.py --launcher pytorch --work-dir ckpt/coDETR_swinB_1000x_type8_batch4_v3
    #tools/train.py projects/configs/coDETR_r/co_deformable_detr_swin_base_100x_coco.py --launcher pytorch --work-dir ckpt/coDETR_swinB_1000x_type8_batch2_v2
    #tools/train.py projects/configs/co_deformable_detr/co_deformable_detr_swin_large_900q_3x_coco.py --launcher pytorch --work-dir ckpt/coDETR_swinB_3x_v1
