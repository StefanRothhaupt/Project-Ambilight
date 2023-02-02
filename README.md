# Project-Ambilight

##Short-Description:

In this project students from the University of Applied Sciences in Munich built a ambient light for a monitor.
##Detailed Description:
In the 6th semester of electrical engineering and information technology students are supposed to envision and build their own product.
It can be something that already exists. The purpose of the project is to simulate the whole project cycle of devleoping and testing the product. 
We choose to build a ambient light with a single board computer, that can be mounted on the back of a screen (tv or computer monitor)

##Resource Overview:
Here you can find all the relevant links (code, links to amazon to order the parts, and the documentation if you want to build your own ambient light)

##User-Deployment guide:
##Developer Documentation:
##Demo-video:
here you can see our elevator pitch video for the project
##Code
##Theoretical data processiong:
In short: We read the video via a HDMI Splitter in and take on of the streams to process the image data with the Raspi.
The raspi scales the video down, cuts the images into sectors, these sectors are analyzed for their most dominant color. 
The color value is then passed on to the LEDs on the back of the Screen.
refer to these slides to learn more
