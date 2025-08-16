# 🖱️ Virtual Mouse using OpenCV, MediaPipe & PyAutoGUI  

Control your computer **mouse cursor** with just your **hand gestures**!  
This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to detect hand landmarks in real-time and simulate mouse actions like moving, clicking, scrolling, and zooming — all without touching a physical mouse.  

---

## 🚀 Features  
- 👆 **Cursor Control** – Move the cursor using your index finger.  
- 👆🤏 **Left & Double Click** – Thumb + Index pinch  
  - Quick pinch → Left Click  
  - Hold pinch for >1s → Double Click  
- 🔁 **Smooth Scrolling** – Index + Middle finger gap controls scrolling:  
  - Index above middle → Scroll up  
  - Index below middle → Scroll down  
- 🔎 **Zoom In / Zoom Out** –  
  - Thumb + Index pinch → Zoom In (`Ctrl + +`)  
  - Thumb + Middle pinch → Zoom Out (`Ctrl + -`)  
- ✊ **Drag & Drop** – Thumb + Ring pinch to drag, release to drop.  
- ⚡ **Smooth cursor movement** with interpolation.  

---

## 🛠️ Tech Stack  
- [Python 3.x](https://www.python.org/)  
- [OpenCV](https://opencv.org/) – Computer vision & image processing  
- [MediaPipe](https://developers.google.com/mediapipe) – Real-time hand landmark detection  
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) – Mouse & keyboard control  

---

## 📂 Project Structure
virtual-mouse/
│── virtual_mouse.py # Main Python script
│── requirements.txt # List of dependencies
│── README.md # Project documentation


---

## ⚙️ Installation  

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/virtual-mouse.git
   cd virtual-mouse

2. **Install dependencies using requirements.txt:**
   pip install -r requirements.txt
3. **python virtual_mouse.py**

## 🎮 Usage Instructions
- Move cursor → Use your index finger
- Left click → Tap index & thumb quickly
- Double click → Hold index & thumb together for 1+ second
- Scroll → Keep index & middle fingers close:
  - Index above middle → Scroll up
  - Index below middle → Scroll down
- Zoom In → Pinch index + thumb
- Zoom Out → Pinch middle + thumb
- Drag & Drop → Pinch thumb + ring finger
➡️ Press ESC to quit the program.

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📜 License

This project is licensed under the MIT License.
