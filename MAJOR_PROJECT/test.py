import cv2

OPENCV_OBJECT_TRACKERS = {
		"csrt": cv2.TrackerCSRT_create,
		"kcf": cv2.TrackerKCF_create,
		
		"mil": cv2.TrackerMIL_create,
}
tracker = OPENCV_OBJECT_TRACKERS['csrt']()