# Pixel Manipulation for Image Encryption (Prodigy InfoTech – Task 2)

## 🔍 Description
A simple Python program that encrypts and decrypts images using pixel manipulation.  
The program uses the XOR method — each pixel value is changed based on a key number.  
Using the same key again decrypts the image back to normal.

---

## ⚙️ Requirements
You need the **Pillow** library for image processing.  
Install it by running this command in PowerShell:
```
pip install pillow
```

---

## ▶️ How to Run (Windows PowerShell)

### 1. Open PowerShell in your project folder:
```
cd "F:\Prodigy Task 2 ImageEncryption"
```

### 2. Encrypt an image:
```
python main.py --mode encrypt --method xor --key 123 --input input.jpg --output encrypted.png
```

### 3. Decrypt the same image:
```
python main.py --mode decrypt --method xor --key 123 --input encrypted.png --output decrypted.png
```

After running these two commands:
- `encrypted.png` will look scrambled.  
- `decrypted.png` will look like the original image again.

---

## 🧩 Files in this Project
- `main.py` – Python code for encryption and decryption  
- `requirements.txt` – library dependency (Pillow)  
- `report.md` – short write-up of the task  
- `screenshots/` – folder for proof images  
- `input.jpg` – the test image used  

---

## 👨‍💻 Author
**Rafin**  
Cybersecurity Intern – *Prodigy InfoTech*
