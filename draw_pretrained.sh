python tools/test.py projects/configs/coDETR_r/co_deformable_detr_swin_base_3x_coco.py \
	/tmp2/jcwu/1_projM/2_projects/OD/1_CoDETR/3_Co-DETR_fixDNN/ckpt/best_ckpt/best_ckpt.pth \
	--show-dir results/best_ckpt/ \
	--out results/output/model.pickle \
	--format-only \
	--work-dir results/work/ \
	--options "jsonfile_prefix=results/work/mask_rcnn_test-dev_results, logger=results/log/log"
       	#tools/test.py projects/configs/coDETR_r/co_deformable_detr_swin_base_3x_coco.py /tmp2/jcwu/1_projM/2_projects/OD/1_CoDETR/ckpts/co_deformable_detr_swin_base_3x_coco.pth --launcher pytorch --eval bbox
