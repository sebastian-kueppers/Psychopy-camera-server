import cv2 as cv
import time
import threading
import logging
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

# Setup logging
logging.basicConfig(filename='recording_latency.log', level=logging.INFO, format='%(asctime)s - %(message)s')

MAXIMUM_RECORDING_TIME = 200
goosecam = None
webcam = None
is_goosecam_recording = False
is_webcam_recording = False
out_goosecam = None
out_webcam = None
goosecam_recording_thread = None
webcam_recording_thread = None

latencies = []
round_counter = 1

def init_cameras():
    global goosecam, webcam
    goosecam = cv.VideoCapture(0)
    webcam = cv.VideoCapture(1)
    if goosecam.isOpened() and webcam.isOpened():
        print("Cameras initialized", flush=True)
    if not goosecam.isOpened():
        raise Exception("Could not open goosecam")
    if not webcam.isOpened():
        raise Exception("Could not open webcam")

def start_recording(base_filename, client_timestamp):
    global is_goosecam_recording, is_webcam_recording, out_goosecam, out_webcam
    global goosecam_recording_thread, webcam_recording_thread, latencies, round_counter

    if is_goosecam_recording or is_webcam_recording:
        return "Already recording"

    is_goosecam_recording = True
    is_webcam_recording = True

    server_timestamp = time.time()
    time_difference_goosecam = server_timestamp - client_timestamp
    time_difference_webcam = server_timestamp - client_timestamp

    latencies.append({
        'round': round_counter,
        'webcam': time_difference_webcam,
        'goosecam': time_difference_goosecam
    })

    filename_goosecam = base_filename + "_GOOSECAM.avi"
    filename_webcam = base_filename + "_WEBCAM.avi"

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    fps_goosecam = goosecam.get(cv.CAP_PROP_FPS)
    fps_webcam = webcam.get(cv.CAP_PROP_FPS)

    out_goosecam = cv.VideoWriter(filename_goosecam, fourcc, fps_goosecam, (640, 480))
    out_webcam = cv.VideoWriter(filename_webcam, fourcc, fps_webcam, (640, 480))

    goosecam_recording_thread = threading.Thread(target=record_goosecam_video)
    webcam_recording_thread = threading.Thread(target=record_webcam_video)

    goosecam_recording_thread.start()
    webcam_recording_thread.start()

    round_counter += 1

    return "Recording started"

def record_goosecam_video():
    global is_goosecam_recording, out_goosecam
    e1 = cv.getTickCount()
    while is_goosecam_recording:
        ret, frame = goosecam.read()
        if ret:
            out_goosecam.write(frame)
        e2 = cv.getTickCount()
        elapsed_time = (e2 - e1) / cv.getTickFrequency()
        if elapsed_time >= MAXIMUM_RECORDING_TIME:
            stop_recording()
            break
    out_goosecam.release()

def record_webcam_video():
    global is_webcam_recording, out_webcam
    e1 = cv.getTickCount()
    while is_webcam_recording:
        ret, frame = webcam.read()
        if ret:
            out_webcam.write(frame)
        e2 = cv.getTickCount()
        elapsed_time = (e2 - e1) / cv.getTickFrequency()
        if elapsed_time >= MAXIMUM_RECORDING_TIME:
            stop_recording()
            break
    out_webcam.release()

def stop_recording():
    global is_goosecam_recording, is_webcam_recording
    is_goosecam_recording = False
    is_webcam_recording = False
    return "Recording stopped"

def release_all():
    global goosecam, webcam, latencies
    if goosecam is not None:
        goosecam.release()
    if webcam is not None:
        webcam.release()

    # Export latencies to CSV
    df = pd.DataFrame(latencies)
    df.to_csv('camera_latencies.csv', index=False)

    return "All cameras released and latencies exported"

@app.route('/start', methods=['POST'])
def start():
    base_filename = request.json.get('filename')
    client_timestamp = request.json.get('timestamp')
    response = start_recording(base_filename, client_timestamp)
    return jsonify({'message': response})

@app.route('/stop', methods=['POST'])
def stop():
    response = stop_recording()
    return jsonify({'message': response})

@app.route('/releaseAll', methods=['POST'])
def release_all_route():
    response = release_all()
    return jsonify({'message': response})

if __name__ == '__main__':
    init_cameras()
    app.run(port=5000)
