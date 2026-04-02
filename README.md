# Smart LED Controller (PIR + Light Sensor)

Intelligent LED lighting controller that automatically turns lights on based on motion detection (PIR) and ambient light level.
This project focuses on embedded system design, sensor integration, and power control using MOSFET, along with a custom 3D enclosure.

---

## 📸 Project Overview
<p align="center">
  <img src="./images/controller.jpg" width="400"/>
  <img src="images/controller_on_power_supply.jpg" width="400"/>
  <img src="./images/sensor_wall.jpg" width="400"/>
  <img src="images/sensor_image.jpg" width="400"/>
  <img src="images/rl_example.gif" width="400"/>
  
</p>

---

## ⚙️ Features

* Motion detection using PIR sensor
* Ambient light detection (prevents turning on in bright conditions)
* Red and green LED control using MOSFET
* Slowly fading to warm orage lighting
---

## 🛠 Technologies & Tools

* Electronics: PIR sensor, light sensor, MOSFET driver
* Embedded: Arduino nano 
* Schematic Design: KiCad
* 3D Design: Fusion 360
* Prototyping: breadboard / wiring
* Python: script to simulate color space and fade-in trace

---

## 📐 Hardware Design

###  Electrical Schematic

<p align="center">
  <img src="./images/schematic.png" width="500"/>
</p>

### 3D Enclosure

![Case](./images/case.png)

---

## 🚀 How It Works

- PIR sensor detects motion; photoresistor checks ambient light  
- LEDs turn ON only if motion is detected **and** it’s dark  
- Smooth fade-in/out via PWM, maintaining red/green ratio  
- LEDs turn OFF if no motion or environment becomes bright

---

## 🎯 Why I built this

The need for night lighting that helps you see what's in the room without having to turn on bright lights.

## 👤 Author
Norbert 
