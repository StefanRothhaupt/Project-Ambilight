# Project-Ambilight
![title foto of the project, with project name and fictive company name](https://github.com/StefanRothhaupt/Project-Ambilight/blob/main/Bildschirm%C2%ADfoto%202023-02-02%20um%2017.53.40.png)
## Short-Description:
In this project students from the [University of Applied Sciences](https://ee.hm.edu) in Munich built a ambient light for a monitor.
The ambient light enhances the viewing experience by illuminating the surrounding environment, creating a more immersive and enjoyable atmosphere. The code and PCB were both designed and built in-house, demonstrating the team's technical abilities and attention to detail.

## Detailed Description:
In the 6th semester of electrical engineering and information technology students are supposed to envision and build their own product.
It can be something that already exists. The purpose of the project is to simulate the whole project cycle of developing and testing the product. 
We choose to build a [ambient light](https://en.wikipedia.org/wiki/Bias_lighting) with a [single board computer](https://en.wikipedia.org/wiki/Single-board_computer), that can be mounted on the back of a screen (tv or computer monitor).
This ambient light system was designed to enhance the viewing experience by changing the light color in sync with the video stream on the TV.
We utilized the latest technology to read in the video stream, scale it down and cut it into sectors. The sectors were then analyzed to determine their most dominant color, which was then passed on to the LEDs on the back of the monitor. The result was a seamless and dynamic integration of light and video, creating an immersive viewing experience.
The project required a high level of technical expertise and collaboration between the team members.

## Resource Overview:
Here you can find all the relevant links (code, links to amazon to order the parts, and the documentation if you want to build your own ambient light)

## User-Deployment guide:
## Developer Documentation:
## Demo-video:
here you can see our elevator pitch video for the project
## Code
## Theoretical data processiong:
In short: We read the video via a HDMI Splitter in and take on of the streams to process the image data with the Raspi.
The raspi scales the video down, cuts the images into sectors, these sectors are analyzed for their most dominant color. 
The color value is then passed on to the LEDs on the back of the Screen.
refer to these slides to learn more
https://github.com/StefanRothhaupt/Project-Ambilight/blob/main/Ambilight%20Video.png
