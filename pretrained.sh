PORT=${PORT:-29510}
python -m torch.distributed.launch --nproc_per_node=2 --master_port=$PORT \
       	tools/test.py projects/configs/coDETR_r/co_deformable_detr_swin_base_3x_coco.py \
	/tmp2/jcwu/1_projM/2_projects/OD/1_CoDETR/3_Co-DETR_fixDNN/ckpt/best_ckpt/best_ckpt.pth \
	--launcher pytorch --eval bbox
       	#tools/test.py projects/configs/coDETR_r/co_deformable_detr_swin_base_3x_coco.py /tmp2/jcwu/1_projM/2_projects/OD/1_CoDETR/ckpts/co_deformable_detr_swin_base_3x_coco.pth --launcher pytorch --eval bbox
