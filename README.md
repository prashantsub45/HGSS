# **🎵 HGSS - Hand Gestured Sound System**
A gesture-controlled music player powered by OpenCV, cvzone, and a beautiful HTML/CSS/JS UI.
Control your music without touching a thing – just wave your hand!

## UI of the web app
![UI of web app] (C:/Users/ASUS/Desktop/Final minor project/HGSS/static/images/UI.png)


## **🧠 How It Works**
🎯 Functionality:
* 👆 Index Finger (only) → Previous Track

* ✌️ Peace Sign → Next Track

* 🖐️ All Fingers Open → Play Music

* ✊ Fist (All Fingers Closed) → Pause Music

## **📂 Project Structure**
```
HGSS/
├── back/
│   ├── app.js                  # JavaScript server logic (optional Node usage)
│   ├── package.json            # Node project setup
│   └── package-lock.json
├── gesture_engine/
│   ├── cam.py                  # Hand gesture recognition using cvzone/OpenCV
│   ├── endapi.py               # Backend API endpoint logic (e.g., Flask)
│   └── try.csv                 # (Optional) Dataset or logs
├── static/
│   ├── images/                 # Contains UI assets/images
│   ├── music/                  # Audio files used in the frontend player
│   ├── index.js                # JavaScript logic for UI & music control
│   └── style.css               # Styling for the web app
├── templates/
│   └── index.html              # HTML UI for the music player
├── app.py                      # Main Flask app (or backend runner)
├── .gitignore
└── README.md                   # You're here!
```

## 🚀 Getting Started
🔧 Prerequisites:
* Python 3.7+

* pip

* Node.js (if using backend in back/)

* Webcam

## **📦 Python Dependencies**
Install required Python packages:
```
pip install opencv-python cvzone flask numpy
```
**▶️ Run the Backend**
Make sure you are in the project root (HGSS/), then run:
```
python app.py
```
This will:

- Start the Flask app serving your UI

- Activate camera using cam.py

- Expose an API via endapi.py if applicable

Note: The backend serves the index.html and static files through Flask templates.

## **🌐 Using the Web Interface**
- Navigate to `http://127.0.0.1:5000/` in your browser.

- Use your webcam and perform gestures to control music:

  - One finger = Previous

  - Peace ✌️ = Next

  - Open palm = Play

  - Closed fist = Pause

Works with any `.mp3` files added to `/static/music/`. I haven't included those files here along with their images covers.

## 🖼️ UI & Assets
- UI assets and icons live in `static/images/`

- Music files are placed in `static/music/`

- Modify index.js to change how gestures trigger songs or actions.
  
