import time
import cv2
from mss.linux import MSS
import mss
import numpy as np
import pyscreenshot as pyshot


def get_screen_res():
    import tkinter
    root = tkinter.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return {"top": 0, "left": -30, "width": 100, "height": 100}


def run():
    title = "screen"
    fps = 0
    start_time = time.time()
    sct = MSS()
    mon = get_screen_res()
    print(mon)
    while True:
        try:
            img = np.asarray(sct.grab(mon))
        except mss.ScreenShotError:
            details = sct.get_error_details
            import pprint
            pprint.pprint(details)
            break
        else:
            cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
            fps += 1
            t = time.time() - start_time
            if t >= 1:
                print(f"FPS is {fps}")
                fps = 0
                start_time = time.time()
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

run()