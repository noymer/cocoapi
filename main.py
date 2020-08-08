from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

cocoGt = COCO('./data/instancesonly_filtered_gtFine_val.json')
cocoDt = cocoGt.loadRes('./data/epoch_22.json')

annType = 'segm'
cocoEval = COCOeval(cocoGt,cocoDt,annType)
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()