# hackgt9
Gesture Control Gamer Time

This is the shared repository for the Game gesture control. 

Current Idea:
  <p>Control Stardew Valley using hand gestures and movements using MediaPipe Python packages</p>
  <p>Below is an introduction to using MediaPipe with Python<br>
    https://google.github.io/mediapipe/getting_started/python </p>
  <p>Below is an intrduction to using the hand detection with MediaPipe <br>
    https://google.github.io/mediapipe/solutions/hands#python-solution-api </p>
  <p><br> 
    We'll have to focus on different parts of the workflow
    <br> Part1: We need to use media pipe to recognize gestures
    <br> Part2: We need to map those gestures to different inputs in stardew <br> https://stardewvalleywiki.com/Controls
    <br> Part3: We need to turn gestures into keyboard or controller interrupts so that Stardew can recognize those inputs. 
    <br> Options for this include modding Stardew or using an API to create keyboard interrupts </br>
    <br>
    <p> In order to run and use this code, you can run testGameIput.py after installing the necessary dependencies, and then when you switch windows to the game you want to play, you can control the game using your hands. This requires that the game is the active window currently, and that you have a working webcam. You may have to specify which webcam to use.
