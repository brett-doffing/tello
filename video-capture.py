import cv2, threading, multiprocessing, time, datetime
import queue
from tkinter import *

class VidCap:
    def __init__(self, cam_name, cam_port):
        self.cap = cv2.VideoCapture(f"udp://0.0.0.0:{cam_port}")
        self.q = queue.Queue()
        t = threading.Thread(target=self._reader)
        t.daemon = True
        t.start()

    # read frames as soon as they are available, keeping only most recent
    def _reader(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait() # discard previous (unprocessed) frame
                except queue.Empty:
                    pass
            
            self.q.put(frame)

        self.cap.release()
    
    def read(self):
        return self.q.get()

img_db_path = "/path/to/images"

cap1 = VidCap("Tello_1", 11113)
cap2 = VidCap("Tello_2", 11115)
cap3 = VidCap("Tello_3", 11117)

cam_int = 1

def snap():
    frame1 = cap1.read()
    frame2 = cap2.read()
    frame3 = cap3.read()

    cv2.imwrite(f"{img_db_path}{datetime.datetime.now()}_1.jpg", frame1)
    cv2.imwrite(f"{img_db_path}{datetime.datetime.now()}_2.jpg", frame2)
    cv2.imwrite(f"{img_db_path}{datetime.datetime.now()}_3.jpg", frame3)

def toggle_cam():
    global cam_int
    if cam_int == 1:
        cam_int = 2
    elif cam_int == 2:
        cam_int = 3
    else:
        cam_int = 1

root = Tk()
root.geometry("600x200")

txt_fld = Text(root, width=50, height=1, pady=10)
txt_fld.pack()

btn_snap = Button(root, text="SNAPSHOT", width=50, pady=20, command=snap)
btn_snap.pack()

btn_cam = Button(root, text="TOGGLE CAM", width=50, pady=20, command=toggle_cam)
btn_cam.pack()

while True:
    root.update()
    frame1 = cap1.read()
    frame2 = cap2.read()
    frame3 = cap3.read()

    if cam_int == 1:
        cv2.imshow("Tello_1", frame1)
    elif cam_int == 2:
        cv2.imshow("Tello_2", frame2)
    else:
        cv2.imshow("Tello_3", frame3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
