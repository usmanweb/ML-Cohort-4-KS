def iou(box1, box2):
    '''
    Input: box1 = [x1 y1 x2 y2] = [511 41 577 76]
        box2 = [x1 y1 x2 y2] = [544 59 610 94]
    output: intersection over union
    '''
    #box1_area = (x2-x1)*(y2-y1)
    box1_area = abs(box1[2]-box1[0])*abs(box1[3]-box1[1])
    box2_area = abs(box2[2]-box2[0])*abs(box2[3]-box2[1])

    # Intersection calculation
    Ix1 = max(box1[0], box2[0])
    Iy1 = max(box1[1], box2[1])
    Ix2 = min(box1[2], box2[2])
    Iy2 = min(box1[3], box2[3])

    Intersection_area = abs(Ix2-Ix1)*abs(Iy2-Iy1)
    union_area = box1_area + box2_area - Intersection_area
    output = Intersection_area/union_area
    return output
