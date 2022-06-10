import os
import sys
import cv2

def getfilepaths(path, ext = 'avi'):
    files = os.listdir(path)
    files_file = [f for f in files if os.path.isfile(os.path.join(path, f)) and f.endswith('.' + ext)]
    return files_file

path_input = './input'
path_output = './output'

for file in getfilepaths(path_input):
    video = cv2.VideoCapture(os.path.join(path_input, file))
    k = 0
    frames = []
    while(video.isOpened()):
        ret, frame = video.read()
        if ret == False:
            sys.stderr.write("\rinput '" + file + "' (%d frames)\n" % (k-1))
            break
        frames.append(frame)

        sys.stderr.write('\r%d' % k)
        sys.stderr.flush()

        k = k + 1

    frame_rate = 24.0
    size = (512, 512)
    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    writer = cv2.VideoWriter(os.path.join(path_output, os.path.splitext(file)[0] + '.mp4'), fmt, frame_rate, size)
    k = 0
    for frame in frames:
        writer.write(frame)
        sys.stderr.write('\r%d' % k)
        sys.stderr.flush()
        k = k + 1
    sys.stderr.write("\routput '" + os.path.splitext(file)[0] + ".mp4' (%d frames)\n\n" % (k-1))
    writer.release()
