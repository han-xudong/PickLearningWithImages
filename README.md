# Learning to Pick with 2D Images
> Assignment Project #1: 30% | Due Sunday, Mar 28

------

## Basic Training
Hand-eye Calibration

## Target
This experiment is mainly divided into two parts. They are 2D calibration and object capture respectively. The goal of 2D calibration is to establish the transformation basis of the camera coordinate system and the manipulator coordinate system, that is, the hand-eye transformation matrix used to describe the relative spatial pose of the manipulator and the camera. On this basis, object grasping is to get the grasping coordinates through the camera image recognition and control the movement of the manipulator to grasp.

## Hardware List
The hardware equipment required for this experiment is as follows:
- camera: Intel Realsense
- mechanical arm: Aubo i5
- calculation platform: computer
- calibration: 3D-printed nib and base (mounted on manipulator arm)
- calibrators: 3D-printed nib (for calibration on a flat surface)
- clamping device:  pneumatic clamping jaw (air compressor and air valve)
- grasped objects:  plastic bottles, cans

## Preparation
1. Connect the power supply and plug in the AUBO.
2. Turn the black knob in the main machine of AUBO from ON to the red emergency stop button upward to the right to unlock the emergency mode.
3. Turn the emergency stop button on the teaching device up to the right, open the teaching device and click the save button in the popover.
4. Connect the control box to the main machine with network cable.
5. Right-click on the desktop to open the terminal and enter the following code to open PyCharm.
```python
cd Downloads/pycharm-community-2020.3.3/bin
sh pycharm.sh
```
6. Enter the following code in the terminal to turn on the camera.
```
realsense-viewer
```

## Conclusion
In this project, we applied multiple algorithms to achieve picking with 2D images. One is yoloV4. This algorithm has a higher accuracy in recognizing objects. Another one is yoloV5. This algorithm has a significent advantage: fast. When recognizing multiple images, it has an average processing time of 7ms per image, that’s 140 FPS, and that is an incredible achievement. Also, yoloV5 has a lighter model size, which makes it even more flexible. Considering we aim at grabing garbage, a faster solving program is exactely what we need. Thus less accuracy of yoloV5, comparing with yoloV4, is acceptable. We also tried EfficientDet to detect the target objects. It is a little bit slowly than yoloV5, and has similay accuracy. But the problem is when we require more accuracy and apply different EfficientDet algorithms, the running time of the progrim is raising so fast that it becomes a great disadvantage. The best algorithm now we have is yoloV5. If we could improve the accuracy of our program, that’s would be useful.
