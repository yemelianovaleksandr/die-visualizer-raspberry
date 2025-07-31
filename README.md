# Die Visualizer — Interactive Dice Roll Visualizer

**Die Visualizer** is a web app that visualizes dice rolls as an animated bar chart.  
It runs on a Raspberry Pi and uses Python, Flask, Matplotlib, and FFmpeg to generate video.  
Users can choose how many times to roll the die (from **100 to 5,000,000**), and the app generates a visual animation that confirms the **Law of Large Numbers**.

---

## 📸 Live Demo

 **[Launch App via Githack CDN](https://raw.githack.com/yemelianovaleksandr/die-visualizer-raspberry/main/redirect/index.html)**  
 The DDNS of the Raspberry Pi is protected via a secure proxy.

---

##  Features

-  Animated die roll distribution
-  Supports 100 to 5,000,000 rolls
-  Mobile and desktop friendly interface
-  Auto-delete videos after 60 seconds
-  Percentages accurate to 0.001%
-  Full DDNS privacy with Render proxy
-  Docker support
-  CI/CD via GitHub Actions
-  Production-ready with Nginx

---

## Project Structure
├── app/
│   ├── app.py           # Flask app
│   ├── die_anim.py      # Plot animation
│   └── templates/
├── redirect/
│   └── index.html       # Githack iframe to proxy
├── nginx/
│   └── nginx.dieapp.conf
├── Dockerfile
├── requirements.txt
├── README.md

---

##  Installation (without Docker)

```bash
sudo apt update
sudo apt install python3-pip ffmpeg
pip3 install -r requirements.txt
python3 app/app.py
