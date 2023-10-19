python tools/test.py projects/configs/coDETR_r/co_dino_5scale_swin_large_16e_o365tococo.py \
	/tmp2/jcwu/1_projM/2_projects/OD/1_CoDETR/3_Co-DETR_fixDNN/ckpt/final_ckpt/epoch_26.pth \
	--show-dir results_DINO_test/img/ \
	--out results_DINO_test/pickle/model.pickle \
	--format-only \
	--work-dir results_DINO_test/work/ \
	--options "jsonfile_prefix=results_DINO_test/work/test_results"
       	#tools/test.py projects/configs/coDETR_r/co_deformable_detr_swin_base_3x_coco.py /tmp2/jcwu/1_projM/2_projects/OD/1_CoDETR/ckpts/co_deformable_detr_swin_base_3x_coco.pth --launcher pytorch --eval bbox
