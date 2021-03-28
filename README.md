# Learning to Pick with 2D Images
> Assignment Project #1: 30% | Due Sunday, Mar 28

------

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

## Challenges and Solutions
- 2D calibration: It is better to re-calibrate 2D calibration before each 2D grasping experiment. Once the placement position of the camera is affected by external factors, it will bring great errors to our 2D calibration results, resulting in the failure of the final clip 
- Proper 2D Camera resolution: When adjusting RealSense, open the RGB Camera and adjust its pixels to 1280*720. At first, when we carried out 2D calibration, we used the default resolution. Low resolution led to large error of calibration results and incorrect coordinates. 
- Need to resolve permission issue before running main.py in 2d_picking:
![image](https://github.com/MEE336-Red-Team/Learning_to_Pick_with_2D_Images/blob/main/image/resolve_permission_issue.png)

## Conclusion
In this project, object recognition is the key to pick with images. we propose EfficientDet to recognize the object. To compare the performance, we ran three normal algorithms, yoloV4, yoloV5 and EfficientDet. First, we tried yoloV5 provided by the tutorial. And we also tried yoloV4, which has a higher accuracy in recognizing objects. But yoloV4 is much slower than yoloV5. When recognizing multiple images, yoloV5 has an average processing time of 7ms per image, that’s 140 FPS, and that is an incredible achievement. Considering we aim at grabing garbage, a faster solving program is exactely what we need. We also tried EfficientDet to detect the target objects. It is a little bit slowly than yoloV5, and has similay accuracy. But the problem is when we require more accuracy and apply different EfficientDet algorithms, the running time of the progrim is raising so fast that it becomes a great disadvantage. However, these algorithms all have a common regret, that is, the bounding frame cannot be tilted. When the object is tilted in the camera field of view, the bounding frame is still parallel to the x- and y-axis, which leads to the robot arm still grasping along the x- or y-axis. Although it is still effective for grasping plastic bottles and cans, it may cause problems for other items. Therefore, this is an optimization direction in the future.

After we find out the way to recognize the object, we provide the position to the Aubo i5 and grasp. After many experiments, the success rate of grasping plastic bottles and cans is very high. But paper and other thin items are difficult to grasp, is due to the structure of the claw restrictions. These are what we can improve on and hopefully will be addressed in Project 3.
