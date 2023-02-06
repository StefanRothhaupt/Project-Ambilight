import board
import neopixel
import cv2
import numpy as np
import re
import time
x_pixel = 18
y_pixel = 10
pixel_pin = board.D18

num_pixels = (2*x_pixel+2*y_pixel) 
off = (0, 0, 0)
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER)
pixels.fill(off)
pixels.show()
    
    
def get_avg_color(sec):
        color = [0,0,0]
        img = sec
        
        #cv2.imshow(key, img) #zur kontrolle der sektoren
        img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
        n_colors = 1
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        flags = cv2.KMEANS_RANDOM_CENTERS
        pixels = np.float32(img.reshape(-1, 3))
        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        _, counts = np.unique(labels, return_counts=True)
        indices = np.argsort(counts)[::-1]   
        freqs = np.cumsum(np.hstack([[0], counts[indices]/float(counts.sum())]))
        rows = np.int_(img.shape[0]*freqs)
        dom_patch = np.zeros(shape=img.shape, dtype=np.uint8)    
        for i in range(len(rows) - 1):
            dom_patch[rows[i]:rows[i + 1], :, :] += np.uint8(palette[indices[i]])
        #print("test")
        #print(dom_patch[0][0])
        color[0] = int(dom_patch[0][0][0])
        color[1] = int(dom_patch[0][0][1])
        color[2] = int((dom_patch[0][0][2])*0.7)
        #for m in len(dom_patch[0][0]):
        #    color[m] = dom_patch[0][0]
        #print(type(color))
        #print(type(color[0]))
        
        
        """
        #ploted die dominanten farben in python, macht es langsam
        fig, (ax1) = plt.subplots(1, 1, figsize=(12,6))
        ax1.imshow(dom_patch)
        ax1.set_title(key)
        ax1.axis('off')
        plt.show()
        """
        color = tuple(color)
        return color

def get_sectors(x, y, img):
    
    img_y, img_x, channels = img.shape
    
    x_width = img_x//x
    y_width = img_y//y
    colors = np.empty((2*x+2*y), dtype=object)
    faktor = 3
    
    for i in range(y):
        sec = img[img_y-(y_width*(i+1)):img_y-(y_width*(i)) , img_x-x_width//faktor:img_x]
        colors[i] = get_avg_color(sec)
        
        sec = img[0+(y_width*(i)):0+(y_width*(i+1)) , 0:x_width//faktor]
        colors[i+x+y] = get_avg_color(sec)
    
    for i in range(x):
        sec = img[0:y_width//faktor , img_x-(x_width*(i+1)):img_x-(x_width*(i))]
        colors[i+y] = get_avg_color(sec)
        
        sec = img[img_y-y_width//faktor:img_y , 0+(x_width*(i)):0+(x_width*(i+1))]
        colors[i+x+2*y] = get_avg_color(sec)
    
    return colors

def start_up_color():
    
    for i in range(num_pixels):
        pixels[i] = (0,255,0)
        pixels.show()
        time.sleep(0.03)
    time.sleep(1)
    
def capture_init():

    vidcap = cv2.VideoCapture(0)
    print("Test 0")
    success, image = vidcap.read()
    if success:
        pass
    else:
        vidcap.release()
        vidcap = cv2.VideoCapture(1)
        print("Test 1")
        success, image = vidcap.read()
        if success:
            pass
        else:
            vidcap.release()
            print("Test 2")
            vidcap = cv2.VideoCapture(2)
            
    return vidcap
    
    
#starting signal
start_up_color()
#get input stream
vidcap = cv2.VideoCapture(0)
success, image = vidcap.read()
#show ambilight
try:
    while 1:
        success, image = vidcap.read()
        image = cv2.resize(image, (180, 100), interpolation = cv2.INTER_NEAREST)
        
        if success:
            col = get_sectors(18, 10, image)

            for i in range(len(col)):
                pixels[i] = col[i]
                    
        pixels.show()

except KeyboardInterrupt:
    vidcap.release()
    pixels.fill(off)
    pixels.show()
    exit

exit
