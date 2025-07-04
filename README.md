# 📸 SnapCircle – Find Faces in Group Photos with AI

SnapCircle is a Python-based face recognition tool that helps you identify if a particular person appears in a group photo — ideal for sorting, tagging, and organizing images with AI.

## 🚀 Features

- ✅ Face encoding using `face_recognition`
- 🔍 Scans group photos for known individuals
- 🎯 ~97% accuracy for properly encoded faces
- 📂 Works with local folders of personal/group images
- 🧠 Built with `dlib`, `OpenCV`, and `numpy`

## 🛠️ How It Works

### ➤ Step 1: Encode Known Faces

Use `encode.py` to generate face encodings and store them in a `pickle` file (`EncodeFile.p`).

- Place clear images (one face per image) in a folder like `known_faces/`
- Update the script with the folder path
- Each image filename (without `.jpg`) is treated as the person’s ID

```bash
python encode.py
```

### ➤ Step 2: Detect Target in Group Photo

Use `snapcircle.py` to check whether a specific person appears in a group photo.

- Update the script manually with:
  - `given_id = "<target_name>"`
  - Path to group photo
- Output: Recognized faces will be printed with confidence scores
- Matched image filenames will be collected and displayed

```bash
python snapcircle.py
```

## 📂 Folder Structure

```
SnapCircle/
├── known_faces/         # Images of known individuals (for encoding)
├── testing_photo/       # Group photos to search in
├── EncodeFile.p         # Pickled face encodings
├── encode.py            # Script to generate encodings
├── snapcircle.py        # Script to detect known faces in group photos
└── requirements.txt     # Python dependencies
```

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Or individually:

```bash
pip install opencv-python face_recognition git+https://github.com/ageitgey/face_recognition_models numpy
```

## 🧠 Tech Stack

- `face_recognition` (dlib-based)
- `OpenCV` for image handling
- `pickle` for encoding storage
- `numpy` for calculations

## 📌 Notes

- Ensure good lighting and clear face images for accurate results
- Encoding is based on face geometry — slight variations may affect match confidence
- Recommended face match threshold: `0.50`

## 🤝 Contribution

This is a personal/academic project — contributions are welcome but not required.  
If you find it useful, feel free to ⭐️ the repo!

## 🙋‍♂️ Author
Developed by [Harsh Padsala](https://github.com/Harshpadsala)
