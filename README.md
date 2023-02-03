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
| Produkt        | Quantity         | estimated cost  | Order-Nr. |
| ------------- |:-------------:| -----:|:-------------:|
| [LED Strip, WS2812B, 5M 150LEDs](https://www.amazon.de/BTF-LIGHTING-WS2812B-adressierbare-Streifen-Wasserdicht/dp/B01CDTECSG/ref=sr_1_2_sspa?crid=1POT8EH2W8453&keywords=ws2801&qid=1666263020&qu=eyJxc2MiOiIzLjE5IiwicXNhIjoiMi41MCIsInFzcCI6IjIuMTAifQ%3D%3D&sprefix=WS2%2Caps%2C87&sr=8-2-spons&th=1)  | 1| 30€ |B01CDTECSG |
| [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)       | 1      |   120€ |-|
| [HDMI Splitter](https://www.amazon.de/Links-4330119358-HDMI-Adapter/dp/B0732MD43P/ref=sr_1_8?crid=34ROZS50JI9VR&keywords=hdmi+splitter&qid=1666263505&qu=eyJxc2MiOiI1LjI2IiwicXNhIjoiNC44MSIsInFzcCI6IjQuNjMifQ%3D%3D&s=ce-de&sprefix=HDMI%2Celectronics%2C82&sr=1-8)       | 1      |   120€ |B0732MD43P|
| [Capture Card](https://www.amazon.de/Newhope-Capture-Directly-Computer-Compatible-Schwarz/dp/B09NQM16VY/ref=sr_1_5?crid=3P1CORD8IG5NV&keywords=hdmi%2Bcapture%2Bcard&qid=1666861631&qu=eyJxc2MiOiI1LjQ2IiwicXNhIjoiNC43NyIsInFzcCI6IjQuNDgifQ%3D%3D&sprefix=HDMI%2BCap%2Caps%2C150&sr=8-5&th=1)       | 1      |   120€ |B09NQM16VY|
| [Netzteil](https://www.amazon.de/ALITOVE-Konverter-Transformator-Pixelstreifen-Sicherheitssystem-Black/dp/B0B49TZQZX/ref=sr_1_8?__mk_de_DE=ÅMÅŽÕÑ&crid=1M5ERXVVCWK9A&keywords=5v+5a+netzteil&qid=1666264450&qu=eyJxc2MiOiI0LjE5IiwicXNhIjoiNC4wMSIsInFzcCI6IjQuMDAifQ%3D%3D&sprefix=5v+5a+netzteil%2Caps%2C140&sr=8-8)       | 1      |   120€ |B0B49TZQZX|
| [SD card](https://www.amazon.de/SanDisk-microSD-Karte-VR-Spielgrafiken-4K-UHD-Video-SDSQXAF-032G-GN6GN/dp/B089M5KV4Y/ref=sr_1_8?crid=1BY1FABF1RLRQ&keywords=micro+sd+karte+16gb+sandisk+extreme&qid=1666264516&qu=eyJxc2MiOiIyLjg3IiwicXNhIjoiMS43OSIsInFzcCI6IjEuMzgifQ%3D%3D&sprefix=micro+sd+karte+16gb%2Caps%2C86&sr=8-8)       | 1      |   120€ |-|
| [Switch](https://www.amazon.de/Gebildet-Edelstahl-Drucktastenschalter-Wasserdichter-Kippschalter/dp/B07RXX75KZ/ref=sr_1_13?__mk_de_DE=ÅMÅŽÕÑ&crid=1I6LW9XT2VN0S&keywords=schalter%2B5v%2B5a&qid=1666264741&qu=eyJxc2MiOiIyLjc3IiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=schalter%2B5v%2B5a%2Caps%2C67&sr=8-13&th=1 )      | 1      |   120€ |-|

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
