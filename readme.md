# Psychopy-camera-server
A PsychoPy script that starts a local server which listens for requests to start and stop video recordings.

Built with PsychoPy version ```v2023.2.3```.

## Usage
The setup can be used to precisely time video recordings with any process happening in PsychoPy, e.g., if the video recording needs to be synchronized with a stimulus. By initializing the camera(s) right at the start of the experiment

This script was used in a setup where simultaneously and synchronously two video recordings were needed to be made: of the participant's face while going through the experiment and of the participants arm capturing any degree of goosebumps with a self-made [Goosecam](https://www.psy.uni-hamburg.de/service/technischer-service/technicaloffers/projects/goosecam.html). 

STL files for 3D printing the goosecam are attached in this repo.

## Imports
At the beginning of the Psychopy file, following packages need to be imported: 
```
import time
import requests
from psutil import process_iter
from signal import SIGTERM
```

## Initializing the camera server
The camera server is initialized at the beginning of the Psychopy script. 

Note that the initialization of two cameras from the camera server can take upto 60-90 seconds depending on the webcam hardware used. If video recordings are needed to be made right at the beginning of the experiment it is recommended to start the camera server manually from the command line:
```
/path/to/python.exe camera_server.py
```

## Requests
The camera server listens on ```localhost:5000``` and accepts requests onto three different routes: ```/start (POST)```, ```/stop (POST)```, and ```/releaseAll (POST)```. Requests can be sent to the camera server at any time in the Psychopy experiment.

### POST /start
Starts recording videos from two hardware ressources (if specified). An output filename needs to be specified.
```
filename = "video_recording" # file ending is pasted onto it in camera_server.py
current_time = time.time()

response = requests.post('http://localhost:5000/start', json={'filename': filename, 'timestamp': current_time})
```
```filename``` specifies the filename body of the video recordings. ```current_time``` is used to export a latencies dataframe which holds camera latencies later.

### POST /stop
Stops all video recordings.
```
response = requests.post('http://localhost:5000/stop')
```

If not stopped via this route, the video recording is stopped automatically after ```MAXIMUM_RECORDING_TIME``` (in sec; in ```camera_server.py```).

### POST /releaseAll
Releases all cameras and webcams.
```
response = requests.post('http://localhost:5000/releaseAll')
```

## Closing the camera server
At the end of the Psychopy script, all processes that are running on post :5000 are killed.
```
for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == 5000:
                print(proc)
                proc.terminate()
                proc.send_signal(SIGTERM) 
```
