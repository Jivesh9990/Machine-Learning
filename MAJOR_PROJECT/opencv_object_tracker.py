# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2
import pyautogui


video=None
tracker_choice='csrt'
OPENCV_OBJECT_TRACKERS = {
        "csrt": cv2.TrackerCSRT_create,
        "kcf": cv2.TrackerKCF_create,
        # "boosting": cv2.TrackerBoosting_create,
        "mil": cv2.TrackerMIL_create,
        # "tld": cv2.TrackerTLD_create,
        # "medianflow": cv2.TrackerMedianFlow_create,
        # "mosse": cv2.TrackerMOSSE_create
}
tracker = OPENCV_OBJECT_TRACKERS[tracker_choice]()

initBB = None


if not video:
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    time.sleep(1.0)
# otherwise, grab a reference to the video file
else:
    vs = cv2.VideoCapture(video)
# initialize the FPS throughput estimator
fps = None


# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image', 800,600)
# cv2.namedWindow("image", 0)
# cv2.resizeWindow("image", 1280, 720)

while True:
    # grab the current frame, then handle if we are using a
    # VideoStream or VideoCapture object
    frame = vs.read()
    frame = frame[1] if video else frame
    # check to see if we have reached the end of the stream
    

    if frame is None:
        break
    # resize the frame (so we can process it faster) and grab the
    # frame dimensions
    frame = imutils.resize(frame, width=500)
    (H, W) = frame.shape[:2]



    # font = cv2.FONT_HERSHEY_SIMPLEX
    # frame = cv2.line(frame,(200,0),(200,500),(255,255,0),3)
    # frame = cv2.line(frame,(400,0),(400,500),(255,255,0),3)
    # frame = cv2.line(frame,(200,160),(400,160),(255,255,0),3)
    # frame = cv2.line(frame,(200,325),(400,325),(255,255,0),3)
    # cv2.putText(frame,'Left',(75,270), font, 1,(255,255,255),2,cv2.LINE_AA)
    # cv2.putText(frame,'forward',(240,80), font, 1,(255,255,255),2,cv2.LINE_AA)
    # cv2.putText(frame,'Neutral',(240,260), font, 1,(255,255,255),2,cv2.LINE_AA)
    # cv2.putText(frame,'Backward',(230,420), font, 1,(255,255,255),2,cv2.LINE_AA)
    # cv2.putText(frame,'Right',(480,270), font, 1,(255,255,255),2,cv2.LINE_AA)
    
    if initBB is not None:
        # grab the new bounding box coordinates of the object
        (success, box) = tracker.update(frame)
        # check to see if the tracking was a success

        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h),(0, 255, 0), 2)
            x2=x+y
            y2=y+h
            
            if x2<=220:
                pyautogui.press('a')
                cv2.putText(frame,'LEFT',(10,10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),1)
            elif x>=260:
                pyautogui.press('d')
                cv2.putText(frame,'RIGHT',(10,10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),1)
            else:
                print('NUETRAL')

            # pyautogui.press('w')

        #while True:
            
            # if cv2.waitKey(1) == ord('q'):
            # 	break

        # cap.release()
        # cv2.destroyAllWindows()
        # update the FPS counter
        fps.update()
        fps.stop()
        # initialize the set of information we'll be displaying on
        # the frame
        info = [
            ("Tracker", tracker_choice),
            ("Success", "Yes" if success else "No"),
            ("FPS", "{:.2f}".format(fps.fps())),
            ("coords",f"{x,y,w,h}")
        ]
        # loop over the info tuples and draw them on our frame
        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(frame, text, (10, H - ((i * 20) + 20)),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)



    cv2.imshow("image", frame)
    key = cv2.waitKey(1) & 0xFF
    # if the 's' key is selected, we are going to "select" a bounding
    # box to track
    if key == ord("s"):
        # select the bounding box of the object we want to track (make
        # sure you press ENTER or SPACE after selecting the ROI)
        initBB = cv2.selectROI("image", frame, fromCenter=False,showCrosshair=True)
        # start OpenCV object tracker using the supplied bounding box
        # coordinates, then start the FPS throughput estimator as well
        tracker.init(frame, initBB)
        fps = FPS().start()




    elif key == ord("q"):
        break
# if we are using a webcam, release the pointer
if not video:
    vs.stop()
# otherwise, release the file pointer
else:
    vs.release()
# close all windows
cv2.destroyAllWindows()