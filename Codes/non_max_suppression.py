from myModules.Intersection_over_Union import iou
def nms(bboxes, prob_threshold, iou_threshold):
    '''
    Start with discarding all bounding boxes < probability threshold
    While (Bounding Boxes):
        - Take out the bounding box with largest probability
        - Remove all other boxes with iou > iou_threshold (confidence_score_threshold)
    :param bboxes:[[],[],[],....], prob_threshold=0.5, iou_threshold=0.5
    :return: bbox_nms
    '''
    assert type(bboxes) == list
    bboxes = [box for box in bboxes if box[0] > prob_threshold]
    #print(bboxes)
    bboxes = sorted(bboxes, key=lambda x: x[0], reverse=True)
    #print(bboxes)
    bboxes_after_nms = []
    while(bboxes):
        chosen_box = bboxes.pop(0)
        bboxes = [
            box
            for box in bboxes
            if iou(chosen_box, box) > iou_threshold
        ]
    bboxes_after_nms.append(chosen_box)
    return bboxes_after_nms
