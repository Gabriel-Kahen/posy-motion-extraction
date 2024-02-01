import numpy as np
import cv2

#change file paths here
input = "input.mp4"
output = "output.mp4"

def process(input, output, delay):
    video = cv2.VideoCapture(input)
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    final_video = cv2.VideoWriter(output, fourcc, fps, (width, height)) 
    
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
        print(i + 1, "of", total_frames - delay)
        
    final_video.release()
    print("Done!")
    
process(input, output, 30)
