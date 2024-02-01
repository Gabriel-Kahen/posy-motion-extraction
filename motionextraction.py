import numpy as np
import cv2

#change file paths here
input = "input.mp4"
output = "output.mp4"

#change the delay (in frames) here
delay = 5

def process(input, output, delay):
    video = cv2.VideoCapture(input)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    final_video = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'mp4v'), video.get(cv2.CAP_PROP_FPS), (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))) 
    for i in range(total_frames - delay):
        video.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame1 = video.read()
        video.set(cv2.CAP_PROP_POS_FRAMES, i + delay)
        ret, frame2 = video.read()
        if not ret:
            break
        frame2 = 255 - frame2
        final_frame = ((frame1 * 0.5) + (frame2 * (1 - 0.5))).astype(np.uint8)
        final_video.write(final_frame)
        print(i + 1, "of", int(total_frames - delay))   
    final_video.release()
    print("Done!")
    
process(input, output, delay)
