<<<<<<< HEAD
import numpy as np
import cv2 as cv


def contrastandbrightness(img, contrast, brightness):
    img_trans = contrast * img + brightness
    img_trans = np.clip(img_trans, 0, 255)
    img_trans = img_trans.astype(np.uint8)
    return img_trans
        

def camrecording():
    cam = cv.VideoCapture(0)
    framewidth = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
    frameheight = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    target = cv.VideoWriter('output_video.avi', fourcc, 24.0, (framewidth, frameheight))
    mod = 'preview'

    contrast = 1
    brightness = 0

    if cam.isOpened():
        fps = cam.get(cv.CAP_PROP_FPS)
        wait_msec = int(1/fps*1000)
        

        while True:
            valid, img = cam.read()

            if not valid:
                print("카메라를 불러올 수 없습니다.")
                break
            
            img = contrastandbrightness(img, contrast, brightness)
            if mod == 'record':
                target.write(img)
                cv.circle(img, (20, 20), 10, (255, 255, 255), -5)
                cv.circle(img, (20, 20), 10, (0, 0, 255), -5)
                cv.putText(img, 'REC', (10, 50), cv.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 2)
                cv.putText(img, 'REC', (10, 50), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)

            cv.imshow('Yeonplayer', img)


            key = cv.waitKey(wait_msec)
            if key == 27:
                break
            elif key == ord(' '):
                mod = 'record' if mod == 'preview' else 'preview'
            elif key == ord('w') or key == ord('W'):
                brightness += 1
            elif key == ord('s') or key == ord('S'):
                brightness -= 1
            elif key == ord('a') or key == ord('A'):
                contrast -= 0.1
            elif key == ord('d') or key == ord('D'):
                contrast += 0.1
            elif key == ord('x') or key == ord('X'):
                contrast = 1
                brightness = 0
            brightness = np.clip(brightness, -255, 255)
            contrast = np.clip(contrast, 0.1, 3)
        
        cam.release()
        target.release()
        cv.destroyAllWindows()




if __name__ == '__main__':
    camrecording() 
=======
import numpy as np
import cv2 as cv


def contrastandbrightness(img, contrast, brightness):
    img_trans = contrast * img + brightness
    img_trans = np.clip(img_trans, 0, 255)
    img_trans = img_trans.astype(np.uint8)
    return img_trans
        

def camrecording():
    cam = cv.VideoCapture(0)
    framewidth = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
    frameheight = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    target = cv.VideoWriter('output_video.avi', fourcc, 24.0, (framewidth, frameheight))
    mod = 'preview'

    contrast = 1
    brightness = 0

    if cam.isOpened():
        fps = cam.get(cv.CAP_PROP_FPS)
        wait_msec = int(1/fps*1000)
        

        while True:
            valid, img = cam.read()

            if not valid:
                print("카메라를 불러올 수 없습니다.")
                break
            
            img = contrastandbrightness(img, contrast, brightness)
            if mod == 'record':
                target.write(img)
                cv.circle(img, (20, 20), 10, (255, 255, 255), -5)
                cv.circle(img, (20, 20), 10, (0, 0, 255), -5)
                cv.putText(img, 'REC', (10, 50), cv.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 2)
                cv.putText(img, 'REC', (10, 50), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)

            cv.imshow('Yeonplayer', img)


            key = cv.waitKey(wait_msec)
            if key == 27:
                break
            elif key == ord(' '):
                mod = 'record' if mod == 'preview' else 'preview'
            elif key == ord('w') or key == ord('W'):
                brightness += 1
            elif key == ord('s') or key == ord('S'):
                brightness -= 1
            elif key == ord('a') or key == ord('A'):
                contrast -= 0.1
            elif key == ord('d') or key == ord('D'):
                contrast += 0.1
            elif key == ord('x') or key == ord('X'):
                contrast = 1
                brightness = 0
            brightness = np.clip(brightness, -255, 255)
            contrast = np.clip(contrast, 0.1, 3)
        
        cam.release()
        target.release()
        cv.destroyAllWindows()




if __name__ == '__main__':
    camrecording() 
>>>>>>> 265f265fc63ebbc3c6f4da9e98be76875a172bf5
