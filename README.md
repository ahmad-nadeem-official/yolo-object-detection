YOLOv8n VIDEO OBJECT DETECTION PROJECT 🎥📦
===========================================

**ABOUT THIS PROJECT**
----------------------

This project uses a pretrained **YOLOv8n** model from **Ultralytics** to detect objects in video files. It's designed for simplicity and ease of use, particularly for beginners in the field of computer vision.

* * *

**WHAT IS YOLO?**
-----------------

**YOLO** (You Only Look Once) is a popular object detection algorithm that can detect and classify objects in images or videos in real-time.

*   **Real-time object detection** 🕒
    
*   **High-speed inference** ⚡
    
*   **Efficient and scalable** 🌍
    

YOLO is known for its ability to process images and videos quickly while maintaining high accuracy. It’s widely used in various applications, from surveillance to autonomous driving.

* * *

**PURPOSE OF YOLOv8n**
----------------------

**YOLOv8n** is the nano version of YOLOv8, offering a good balance between speed and accuracy, but with a smaller model size, making it ideal for low-resource environments. This version of YOLO is optimized to run efficiently while maintaining acceptable levels of object detection performance.

*   **Small and Fast** 🏃‍♂️
    
*   **Suitable for real-time applications**
    
*   **Uses less computational power**
    

* * *

**MODEL USED**
--------------

*   **Model**: YOLOv8n (nano version)
    
*   **Pretrained Weights**: Loaded directly from Ultralytics
    
*   **No Training or Dataset Preparation**: Just run the script and get results!
    

* * *

**GOOGLE COLAB**
----------------

You can easily run this project in your browser with Google Colab!  
▶️ **Google Colab Link**: [google-colab](https://colab.research.google.com/drive/1-fgqFvB_vSj5WYme0i7aNUcBwFlhz1i9#scrollTo=bSmR2qKiT-OG)

* * *

**VIDEO DEMOS**
---------------

**🎬 Input Video**:  
[![Output Video](https://github.com/user-attachments/assets/d523e3ee-7b0e-40c9-825b-5d5b3f486f97)](https://github.com/user-attachments/assets/d523e3ee-7b0e-40c9-825b-5d5b3f486f97)

**📤 Output Video**:  
[![Input Video](https://github.com/user-attachments/assets/5399d00c-bf87-4b4a-819c-5a732e35e0f9)](https://github.com/user-attachments/assets/5399d00c-bf87-4b4a-819c-5a732e35e0f9)


* * *

**FOLDER STRUCTURE**
--------------------

Here's the simplified folder structure of the project:

**YOLO/**  
├── **input videos/** → Place your `.mp4` video files here.  
├── **output video/** → Processed videos are saved here.  
├── **runs/detect/** → YOLO auto-generates output here (detection results).  
├── **src/** → Contains your main Python script (`Function.py`).  
├── **requirements.txt** → Python dependencies list.  
├── **yolo\_object\_detection.ipynb** → Optional Jupyter notebook.  
├── **README.md** → This file.  
├── **LICENSE** → Project license.  
├── **.gitignore** → Specifies files/folders to exclude from version control.

* * *

**HOW TO USE**
--------------

1.  Install dependencies from `requirements.txt` using pip.
    
2.  Place your input video inside `input videos/`.
    
3.  Run the `Function.py` script to start detection.
    
4.  Output will be saved in both `output video/` and `runs/detect/`.


***Thanks for your time***
---------------
<b><h5>Best Regards</h5></b>
<h5>Muhammad Ahmad Nadeem</h5>