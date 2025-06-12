import os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1366x768')
        self.root.title("Train Data")

        # Title Label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        # Background Image
        img_top = Image.open(r"C:\Users\Akshi\FirstProject\FacialRecognitionSystem\Images\train.png")
        img_top = img_top.resize((1366, 768), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label = Label(self.root, image=self.photoimg_top)
        f_label.place(x=0, y=45, width=1366, height=768)

        # Train Button
        train_btn = Button(self.root, text="Train Data", cursor="hand2", font=("times new roman", 20, "bold"),
                           bg="red", fg="white", command=self.train_classifier)
        train_btn.place(x=400, y=500, width=200, height=40)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "'data' folder not found.")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image_path in path:
            try:
                img = Image.open(image_path).convert('L')  # Grayscale
                imgNp = np.array(img, 'uint8')
                filename = os.path.basename(image_path)
                parts = filename.split('.')

                # Check filename format: user.<id>.<img_num>.jpg
                # Some filenames may have multiple dots; handle that by checking first 4 parts minimum
                # Valid example parts: ['user', '1', '5', 'jpg']
                if len(parts) >= 4 and parts[0] == 'user' and parts[1].isdigit() and parts[2].isdigit():
                    id_num = int(parts[1])
                    faces.append(imgNp)
                    ids.append(id_num)
                    cv2.imshow("Training", imgNp)
                    cv2.waitKey(1)
                else:
                    print(f"Skipping invalid filename: {filename}")
            except Exception as e:
                print(f"Error processing {image_path}: {e}")

        if not faces:
            messagebox.showerror("Error", "No valid training images found.")
            return

        ids = np.array(ids)

        # Train and save the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed successfully")

# Utility function to fix invalid filenames like 'user..5.jpg'
def fix_invalid_filenames(data_dir):
    existing_ids = set()
    count_map = {}

    for filename in os.listdir(data_dir):
        parts = filename.split(".")
        if len(parts) >= 4 and parts[0] == "user" and parts[1].isdigit() and parts[2].isdigit():
            existing_ids.add(int(parts[1]))
            continue

    assign_id = max(existing_ids, default=0) + 1

    for filename in os.listdir(data_dir):
        parts = filename.split(".")
        if len(parts) >= 4 and parts[0] == "user" and parts[1].isdigit() and parts[2].isdigit():
            continue

        if len(parts) >= 3 and parts[0] == "user" and parts[1] == "":
            if assign_id not in count_map:
                count_map[assign_id] = 1

            while True:
                new_name = f"user.{assign_id}.{count_map[assign_id]}.jpg"
                new_path = os.path.join(data_dir, new_name)
                if not os.path.exists(new_path):
                    break
                count_map[assign_id] += 1

            old_path = os.path.join(data_dir, filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
            count_map[assign_id] += 1

    print("Fix completed.")



if __name__ == "__main__":
    fix_invalid_filenames("data")  # Run this to fix filenames before training
    root = Tk()
    obj = Train(root)
    root.mainloop()


