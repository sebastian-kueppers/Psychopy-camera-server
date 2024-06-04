#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Juni 04, 2024, at 13:02
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from recordVideoSetup
import subprocess
import time
import requests
from psutil import process_iter
from signal import SIGTERM
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'PsychoPy_camera_server'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Sebastian Küppers\\Desktop\\Formal Theory of Co-Occuring Emotions (DFG project)\\github\\camera-server\\PsychoPy_camera_server_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1280, 720], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome" ---
    # Run 'Begin Experiment' code from recordVideoSetup
    camera_server_file = "camera_server.py"
    
    cmd_init_server = ["C:\Program Files\PsychoPy\python.exe", camera_server_file]
    
    process_server_init = subprocess.Popen(cmd_init_server, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    welcomeText = visual.TextStim(win=win, name='welcomeText',
        text='This is the PsychoPy camera server demo.\n\nThe server is already started but the camera(s) need some time (approx. 60 sec.) to initialize. If in your experiment you need to record videos before this time window has passed make sure to start the server before starting your experiment so that it is already running (see readme.md). \n\nPress [space] to start.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    welcomeKeyResp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "recording" ---
    recordingText = visual.TextStim(win=win, name='recordingText',
        text='Video is recording ...\n\nThis takes 10 seconds.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "stop_recording" ---
    stopText = visual.TextStim(win=win, name='stopText',
        text='The camera recording was stopped.\n\nPress [space] to go on.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    stopKeyResp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "end" ---
    endText = visual.TextStim(win=win, name='endText',
        text='All cameras are released.\n\nAll process on port 5000 (where the server run) were killed.\n\nEnd demo with [space].',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    endKeyResp = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "welcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('welcome.started', globalClock.getTime())
    welcomeKeyResp.keys = []
    welcomeKeyResp.rt = []
    _welcomeKeyResp_allKeys = []
    # keep track of which components have finished
    welcomeComponents = [welcomeText, welcomeKeyResp]
    for thisComponent in welcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcomeText* updates
        
        # if welcomeText is starting this frame...
        if welcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcomeText.frameNStart = frameN  # exact frame index
            welcomeText.tStart = t  # local t and not account for scr refresh
            welcomeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcomeText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcomeText.started')
            # update status
            welcomeText.status = STARTED
            welcomeText.setAutoDraw(True)
        
        # if welcomeText is active this frame...
        if welcomeText.status == STARTED:
            # update params
            pass
        
        # *welcomeKeyResp* updates
        waitOnFlip = False
        
        # if welcomeKeyResp is starting this frame...
        if welcomeKeyResp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            welcomeKeyResp.frameNStart = frameN  # exact frame index
            welcomeKeyResp.tStart = t  # local t and not account for scr refresh
            welcomeKeyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcomeKeyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcomeKeyResp.started')
            # update status
            welcomeKeyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(welcomeKeyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(welcomeKeyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if welcomeKeyResp.status == STARTED and not waitOnFlip:
            theseKeys = welcomeKeyResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _welcomeKeyResp_allKeys.extend(theseKeys)
            if len(_welcomeKeyResp_allKeys):
                welcomeKeyResp.keys = _welcomeKeyResp_allKeys[-1].name  # just the last key pressed
                welcomeKeyResp.rt = _welcomeKeyResp_allKeys[-1].rt
                welcomeKeyResp.duration = _welcomeKeyResp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('welcome.stopped', globalClock.getTime())
    # check responses
    if welcomeKeyResp.keys in ['', [], None]:  # No response was made
        welcomeKeyResp.keys = None
    thisExp.addData('welcomeKeyResp.keys',welcomeKeyResp.keys)
    if welcomeKeyResp.keys != None:  # we had a response
        thisExp.addData('welcomeKeyResp.rt', welcomeKeyResp.rt)
        thisExp.addData('welcomeKeyResp.duration', welcomeKeyResp.duration)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    record_videos_trial = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='record_videos_trial')
    thisExp.addLoop(record_videos_trial)  # add the loop to the experiment
    thisRecord_videos_trial = record_videos_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRecord_videos_trial.rgb)
    if thisRecord_videos_trial != None:
        for paramName in thisRecord_videos_trial:
            globals()[paramName] = thisRecord_videos_trial[paramName]
    
    for thisRecord_videos_trial in record_videos_trial:
        currentLoop = record_videos_trial
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRecord_videos_trial.rgb)
        if thisRecord_videos_trial != None:
            for paramName in thisRecord_videos_trial:
                globals()[paramName] = thisRecord_videos_trial[paramName]
        
        # --- Prepare to start Routine "recording" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('recording.started', globalClock.getTime())
        # Run 'Begin Routine' code from recordVideoCode
        participant = str(expInfo['participant'])
        trial = str(record_videos_trial.thisN + 1)
        date = str(expInfo['date'])
        current_time = time.time()
        
        filename = "data/" + participant + "_" + trial + "_" + date
        
        response = requests.post('http://localhost:5000/start', json={'filename': filename, 'timestamp': current_time})
        print(response.json()['message'])
        # keep track of which components have finished
        recordingComponents = [recordingText]
        for thisComponent in recordingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "recording" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recordingText* updates
            
            # if recordingText is starting this frame...
            if recordingText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recordingText.frameNStart = frameN  # exact frame index
                recordingText.tStart = t  # local t and not account for scr refresh
                recordingText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recordingText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recordingText.started')
                # update status
                recordingText.status = STARTED
                recordingText.setAutoDraw(True)
            
            # if recordingText is active this frame...
            if recordingText.status == STARTED:
                # update params
                pass
            
            # if recordingText is stopping this frame...
            if recordingText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > recordingText.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    recordingText.tStop = t  # not accounting for scr refresh
                    recordingText.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'recordingText.stopped')
                    # update status
                    recordingText.status = FINISHED
                    recordingText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in recordingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recording" ---
        for thisComponent in recordingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('recording.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "stop_recording" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('stop_recording.started', globalClock.getTime())
        stopKeyResp.keys = []
        stopKeyResp.rt = []
        _stopKeyResp_allKeys = []
        # Run 'Begin Routine' code from stopCode
        response = requests.post('http://localhost:5000/stop')
        print(response.json()['message'])
        # keep track of which components have finished
        stop_recordingComponents = [stopText, stopKeyResp]
        for thisComponent in stop_recordingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "stop_recording" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stopText* updates
            
            # if stopText is starting this frame...
            if stopText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stopText.frameNStart = frameN  # exact frame index
                stopText.tStart = t  # local t and not account for scr refresh
                stopText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stopText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stopText.started')
                # update status
                stopText.status = STARTED
                stopText.setAutoDraw(True)
            
            # if stopText is active this frame...
            if stopText.status == STARTED:
                # update params
                pass
            
            # *stopKeyResp* updates
            waitOnFlip = False
            
            # if stopKeyResp is starting this frame...
            if stopKeyResp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                stopKeyResp.frameNStart = frameN  # exact frame index
                stopKeyResp.tStart = t  # local t and not account for scr refresh
                stopKeyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stopKeyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stopKeyResp.started')
                # update status
                stopKeyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(stopKeyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(stopKeyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if stopKeyResp.status == STARTED and not waitOnFlip:
                theseKeys = stopKeyResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _stopKeyResp_allKeys.extend(theseKeys)
                if len(_stopKeyResp_allKeys):
                    stopKeyResp.keys = _stopKeyResp_allKeys[-1].name  # just the last key pressed
                    stopKeyResp.rt = _stopKeyResp_allKeys[-1].rt
                    stopKeyResp.duration = _stopKeyResp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stop_recordingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stop_recording" ---
        for thisComponent in stop_recordingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('stop_recording.stopped', globalClock.getTime())
        # check responses
        if stopKeyResp.keys in ['', [], None]:  # No response was made
            stopKeyResp.keys = None
        record_videos_trial.addData('stopKeyResp.keys',stopKeyResp.keys)
        if stopKeyResp.keys != None:  # we had a response
            record_videos_trial.addData('stopKeyResp.rt', stopKeyResp.rt)
            record_videos_trial.addData('stopKeyResp.duration', stopKeyResp.duration)
        # the Routine "stop_recording" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 2.0 repeats of 'record_videos_trial'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime())
    endKeyResp.keys = []
    endKeyResp.rt = []
    _endKeyResp_allKeys = []
    # Run 'Begin Routine' code from releaseAllCamsCode
    response = requests.post('http://localhost:5000/releaseAll')
    print(response.json()['message'])
    # Run 'Begin Routine' code from killAllProcOn5000
    from psutil import process_iter
    from signal import SIGTERM
    
    for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == 5000:
                print(proc)
                proc.terminate()
                proc.send_signal(SIGTERM)
    
    # keep track of which components have finished
    endComponents = [endText, endKeyResp]
    for thisComponent in endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *endText* updates
        
        # if endText is starting this frame...
        if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endText.frameNStart = frameN  # exact frame index
            endText.tStart = t  # local t and not account for scr refresh
            endText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endText.started')
            # update status
            endText.status = STARTED
            endText.setAutoDraw(True)
        
        # if endText is active this frame...
        if endText.status == STARTED:
            # update params
            pass
        
        # *endKeyResp* updates
        waitOnFlip = False
        
        # if endKeyResp is starting this frame...
        if endKeyResp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            endKeyResp.frameNStart = frameN  # exact frame index
            endKeyResp.tStart = t  # local t and not account for scr refresh
            endKeyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endKeyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endKeyResp.started')
            # update status
            endKeyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(endKeyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(endKeyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if endKeyResp.status == STARTED and not waitOnFlip:
            theseKeys = endKeyResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _endKeyResp_allKeys.extend(theseKeys)
            if len(_endKeyResp_allKeys):
                endKeyResp.keys = _endKeyResp_allKeys[-1].name  # just the last key pressed
                endKeyResp.rt = _endKeyResp_allKeys[-1].rt
                endKeyResp.duration = _endKeyResp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime())
    # check responses
    if endKeyResp.keys in ['', [], None]:  # No response was made
        endKeyResp.keys = None
    thisExp.addData('endKeyResp.keys',endKeyResp.keys)
    if endKeyResp.keys != None:  # we had a response
        thisExp.addData('endKeyResp.rt', endKeyResp.rt)
        thisExp.addData('endKeyResp.duration', endKeyResp.duration)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
