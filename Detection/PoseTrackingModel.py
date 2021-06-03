import cv2
import time
import mediapipe as mp


class PoseDetector():
    def __init__(self, model=False, model_comple=1, smooth_lm=True, detectionCon=0.5, trackCon=0.5):
        self.model = model
        self.model_comple = model_comple
        self.smooth_lm = smooth_lm
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mppose = mp.solutions.pose
        self.Pose = self.mppose.Pose(self.model, self.model_comple, self.smooth_lm, self.detectionCon, self.trackCon)
        self.mpdraw = mp.solutions.drawing_utils

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.Pose.process(imgRGB)

        if self.results.pose_landmarks:
            self.mpdraw.draw_landmarks(img, self.results.pose_landmarks, self.mppose.POSE_CONNECTIONS)

        return img

    def findPosition(self, img, draw=False):

        Plmlist = []
        if self.results.pose_landmarks:
            myposeLms = self.results.pose_landmarks
            for id, lm in enumerate(myposeLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, ':', cx, cy)
                Plmlist.append([id, cx, cy])
                if draw:
                    if id == 10:
                        cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)

        return Plmlist


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = PoseDetector()
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue
        img2 = detector.findPose(img)
        Plmlist = detector.findPosition(img2, True)

        if len(Plmlist) != 0:
            print(Plmlist[10])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img2, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    cap.release()


if __name__ == "__main__":
    main()
