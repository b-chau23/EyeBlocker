# EyeBlocker
Starring at your screen for too long? Consider blinding yourself! Once every 20 minutes or so, your screen will turn completely white, rendering you unable to do any type of work until it goes away about 5 seconds later.
During this period, consider taking your eyes off the screen. 

## How it Works
Utilizing the OpenCV library, this [program) detects your face with your device's camera. While your face continues to be on screen, the timer continually ticks until it reaches 20 minutes, in which case a tkinter window will pop up fullscreen and block any kind of work. After 5 seconds, the tkinter window will close and the whole process will start again shortly. The timer can also be reset when a face has not been detected on screen for at least 5 seconds. 

## Usage
In Command Prompt or Powershell:
```
C:\Users\...> python main.py
```
To close, open the camera window and press `q`.

## Notes
Should you ever need to close the tkinter window before time is up (whether due to a bug or something else) hold either left or right `alt` and press `tab` and manually click close on the window.  
  
Similarly, should the camera window also not close after pressing `q`, search for 'python' in Task Manager and end the task.
