![title foto of the project, with project name and fictive company name](https://github.com/StefanRothhaupt/Project-Ambilight/blob/main/Bildschirm%C2%ADfoto%202023-02-03%20um%2018.16.53.png)

## Description:
In the 6th semester of electrical engineering and information technology, students are supposed to envision and build their own product.
In this project students from the [University of Applied Sciences](https://ee.hm.edu) in Munich built a ambient light for a monitor.
The [ambient light](https://en.wikipedia.org/wiki/Bias_lighting) enhances the viewing experience by illuminating the surrounding environment, creating a more immersive and enjoyable atmosphere. The code and PCB were both designed and built in-house, demonstrating the team's technical abilities and attention to detail. The purpose of the project is to simulate the whole project cycle of developing and testing the product. 
We utilized the latest technology to read in the video stream, scale it down and cut it into sectors. The sectors were then analyzed to determine their most dominant color, which was then passed on to the LEDs on the back of the monitor. The result was a seamless and dynamic integration of light and video, creating an immersive viewing experience. The project required a high level of technical expertise and collaboration between the team members. This collaboration was enabled through scrum and state-of the art collaboration software like github and microsoft office.

## Resource Overview:
Here you can find all the relevant products we used (Find code, pcb-gerber-files, and the documentation below):
| Produkt        | Quantity         | estimated cost  |
| ------------- |:-------------:| -----:|
| [LED Strip, WS2812B, 5M 150LEDs](https://www.amazon.de/BTF-LIGHTING-WS2812B-adressierbare-Streifen-Wasserdicht/dp/B01CDTECSG/ref=sr_1_2_sspa?crid=1POT8EH2W8453&keywords=ws2801&qid=1666263020&qu=eyJxc2MiOiIzLjE5IiwicXNhIjoiMi41MCIsInFzcCI6IjIuMTAifQ%3D%3D&sprefix=WS2%2Caps%2C87&sr=8-2-spons&th=1)  | 1| `30€` |
| [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)       | 1      |   `120€` |
| [HDMI Splitter](https://www.amazon.de/Links-4330119358-HDMI-Adapter/dp/B0732MD43P/ref=sr_1_8?crid=34ROZS50JI9VR&keywords=hdmi+splitter&qid=1666263505&qu=eyJxc2MiOiI1LjI2IiwicXNhIjoiNC44MSIsInFzcCI6IjQuNjMifQ%3D%3D&s=ce-de&sprefix=HDMI%2Celectronics%2C82&sr=1-8)       | 1      |   `17€` |
| [Capture Card](https://www.amazon.de/Newhope-Capture-Directly-Computer-Compatible-Schwarz/dp/B09NQM16VY/ref=sr_1_5?crid=3P1CORD8IG5NV&keywords=hdmi%2Bcapture%2Bcard&qid=1666861631&qu=eyJxc2MiOiI1LjQ2IiwicXNhIjoiNC43NyIsInFzcCI6IjQuNDgifQ%3D%3D&sprefix=HDMI%2BCap%2Caps%2C150&sr=8-5&th=1)       | 1      |   `18€` |
| [Powersupply](https://www.amazon.de/ALITOVE-Konverter-Transformator-Pixelstreifen-Sicherheitssystem-Black/dp/B0B49TZQZX/ref=sr_1_8?__mk_de_DE=ÅMÅŽÕÑ&crid=1M5ERXVVCWK9A&keywords=5v+5a+netzteil&qid=1666264450&qu=eyJxc2MiOiI0LjE5IiwicXNhIjoiNC4wMSIsInFzcCI6IjQuMDAifQ%3D%3D&sprefix=5v+5a+netzteil%2Caps%2C140&sr=8-8)       | 1      |   `12€` |
| [SD card](https://www.amazon.de/SanDisk-microSD-Karte-VR-Spielgrafiken-4K-UHD-Video-SDSQXAF-032G-GN6GN/dp/B089M5KV4Y/ref=sr_1_8?crid=1BY1FABF1RLRQ&keywords=micro+sd+karte+16gb+sandisk+extreme&qid=1666264516&qu=eyJxc2MiOiIyLjg3IiwicXNhIjoiMS43OSIsInFzcCI6IjEuMzgifQ%3D%3D&sprefix=micro+sd+karte+16gb%2Caps%2C86&sr=8-8)       | 1      |   `10€` |
| [Switch](https://www.amazon.de/Gebildet-Edelstahl-Drucktastenschalter-Wasserdichter-Kippschalter/dp/B07RXX75KZ/ref=sr_1_13?__mk_de_DE=ÅMÅŽÕÑ&crid=1I6LW9XT2VN0S&keywords=schalter%2B5v%2B5a&qid=1666264741&qu=eyJxc2MiOiIyLjc3IiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=schalter%2B5v%2B5a%2Caps%2C67&sr=8-13&th=1 )      | 1      |   `10€` |

## User-guide:
Follow the [instructions](https://github.com/StefanRothhaupt/Project-Ambilight/blob/main/4-Documentation/User_Manual.pdf), to setup the ambient light if you have the Raspberry Pi with a preinstalled OS and ambilight.py program.
If you still need to setup the Raspberry Pi please follow the instructions below.

## Developer Documentation:
Follow the steps in the [Software manual](https://github.com/StefanRothhaupt/Project-Ambilight/blob/main/4-Documentation/Projekt_Ambilight_Software_Manual.pdf) to setup your [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) for the ambient light. Download the [ambilight python code](https://github.com/StefanRothhaupt/Project-Ambilight/blob/main/1-Code/ambilight.py). Keep in mind, that you need at least 4GB of RAM to drive the capture card. Otherwise the imageprocessing will be too slow and you will be notice a delay when the colors of the LEDs need to change quickly.
After the software setup, follow the [Hardware manual](https://github.com/StefanRothhaupt/Project-Ambilight/blob/main/4-Documentation/Projekt_Ambilight_Hardware_Manual.pdf) to make the system more compact and ready to ba packed into the housing.
You can use [our design](https://github.com/StefanRothhaupt/Project-Ambilight/tree/main/3-Case) or you can create your own.

## Demo-video:
In this demo video we briefly go over the program and how it works and we give you a glimpse of what the ambilight is capable of.
[![Pitch-video_of_the_project](https://github.com/StefanRothhaupt/Project-Ambilight/blob/main/Ambilight_cover_foto.png)](https://www.youtube.com)
