import cv2
import matplotlib.pyplot as plt  # python plot tool
import numpy as np
import realsense_depth as rsd
import mediapipe as mp
from tqdm import tqdm  # import progress bar
import time
import PoseTrackingModel as ptk


def img_show(img):
    """BGR->RGB, because the image format of matlotlib is RGB,the color image from realsense is BGR"""
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_RGB)
    plt.show()


# get camera images
dc = rsd.DepthCamera()
# instantiate pose detector
detector = ptk.PoseDetector()
pTime = 0
cTime = 0
BG_COLOR = (192, 192, 192)  # gray
while True:

    ret, depth_frame, color_frame = dc.get_frame()  # get depth and color frames

    # input model for predicting human pose
    img_pose = detector.findPose(color_frame)

    # visualize result in real 3D world coordination with meter unit
    # detector.mpdraw.plot_landmarks(detector.results.pose_world_landmarks, detector.mppose.POSE_CONNECTIONS)

    # remove background
    try:
        annotated_image = color_frame.copy()
        mask = detector.results.segmentation_mask   # dtype type
        condition = np.stack((mask,) * 3, axis=-1) > 0.1
        bg_image = np.zeros(color_frame.shape, dtype=np.uint8)
        bg_image[:] = BG_COLOR
        annotated_image = np.where(condition, annotated_image, bg_image)
    except TypeError:
        print("Fail to capture human pose")

    cv2.imshow("segmentation", annotated_image)
    # print(mask.shape)
    # mask = mask > 0.5
    # plt.imshow(annotated_image)
    # plt.show()
    # visualize result of pose detection


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img_pose, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("origin", img_pose)

    key = cv2.waitKey(1)
    if key == 27:
        break

if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
