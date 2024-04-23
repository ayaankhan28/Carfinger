import cv2


from pynput.keyboard import  Controller
import handtrackingmodule2 as htm

##############################################

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#############################################

detector = htm.handDetector(maxHands=1, detectionCon=0.5, trackCon=0.5)



keyboard = Controller()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers = detector.fingersUp()
        print(fingers)



        if fingers[1] == 1:
            keyboard.release('s')
            keyboard.press("w")#


        if fingers[1] == 0:
            keyboard.press("s")  #
            keyboard.release('w')

        if fingers[0] == 1:


            keyboard.press("a")
        if fingers[0] == 0:

            keyboard.release('a')
        if fingers[2] == 1:


            keyboard.press('d')
        if fingers[2] == 0:

            keyboard.release('d')

    cv2.imshow("image", img)
    cv2.waitKey(1)
#wawawawasawawawawawawawawawawawawawawawawawawawawawawawawasawawawawawdsssswdsawadwadwadsawadwawadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadsssssssssssasasasasawawadwdwdwdwdwdwdwdwdwdwdwdwdwadwadwadwadwadwadwadwadwadwadwadwadsassssssssssswwwwwwwwwwwwwwwsasasasasasasasasasasassssswadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadsadwasasasawadsssssssssssssssssssssssasasasasasasasasasasasasasawwadwadwadwadwadwdwadwdwdwdwdwdwdwdwdwdwdwdwdwdwdwadwdwadwadwadwadwadwadwadwadwadwadwadwadwadwasasasasasasawasawsssssssasasasasasasasawawasasawawasasasasasasasasasasasasasssassasasasasasasawasawawadwawawadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadsadwadwadwadwadwadwadwadwadwadwdwadwadwadwadwdwadwadwadwadwadwsasasasasawadwawawasasawawawawawasawawadwadwawadwadwadwadwadwadwadwadsadwadwadwadwadwadwadwadwadwadssssswwdwdwdwdwdwsswdwdwdwdwdwdwdsssswdswwdwdwdwdswdwsadsdswdwdwdwdssswwwdswdwdwdwdwdwdwdsswdwdwdwdwdwdwdwdsssswdssswwwwwwwwwwwwwwwwwwwwwwdsssswssasasasasasassswwdwdwdwdwadwadwadwadwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdsdsssdwdssssssssssdsssasssssssssssssssasasasasawdwdwdwdwdwdsadwadwadwadwadssssswdwadwadwadwdwdwwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwwwwwwwwwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdsasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasawadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwdwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadsaswadwadwdwadwadsasasawadwadwadsadsadsasadsadwadwadsasasdsadsadsasasasasasadwadwadwadwadwadwadwdwadsadsadsadsadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadsasasasasasasasssssssssswdwdwdsdsdsdsdsdsdsdsdsdsdsdwdwdwdwdwdwdwdwdwdwdsdsdwdwdwdswssssssssssssswwsswwwwwwwswwwwsssssssssssssssssssssssssssssssssssssswssssssssssswdsasasasasasasasasasasawadwadwadwawadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadssssssssssssswadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwdwdwadwadwdwadwadwadwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwadwadwadwadwdwdwdwdwdwdwadwadwadwadwadwdwdwdwadwadwadwadwadwadwadwdwadwdwdwdwadwadwadwadwadwadwdwdwadwdwdwadwadwadwadwadwdwdwadwadwadwadwadwadwadwadwadwdwdwdwadwadwadwadwadwadwadwadwdwdwadwadwadwadwadwadwadwdwdwdwdwadwadwadwadwadwadwdwdwdwdwadwadwadwadwadwadwdwdwdwadwadwadwadwadwadwadwadwdwdwadwasasawasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasawawawawawawawawawawawawawawawawawawawawawawadwadwadwadwadsasassasssasasassasawd#wadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwdwdwdwdwdwdwdwdwdwdwdwdwwwwdwadsawadwadwadwawawadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwadwdwdwdwadwadwadwadssdssssssss