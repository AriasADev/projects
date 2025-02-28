import sys
import os
import cv2
import pygame
from tkinter import *
from PIL import Image, ImageTk

def enforce_aspect(event):
    if event.widget == root:
        w, h = root.winfo_width(), root.winfo_height()
        if w / h != aspect_ratio:
            root.geometry(f"{int(h * aspect_ratio)}x{h}" if w > h * aspect_ratio else f"{w}x{int(w / aspect_ratio)}")

def fish():
    global root, aspect_ratio, video, canvas, img_tk
    root = Tk()
    aspect_ratio = 3 / 4
    root.title("Horizontal Spinning Fish")
    root.geometry("300x400")
    root.minsize(300, 400)

    # Handle icon for bundled executable
    if getattr(sys, 'frozen', False):  # If running as a bundled executable
        icon_path = os.path.join(sys._MEIPASS, 'icon.ico')
    else:  # If running as a script
        icon_path = 'icon.ico'

    try:
        root.iconbitmap(default=icon_path)
    except Exception as e:
        print(f"Error loading icon: {e}")

    root.bind("<Configure>", enforce_aspect)

    # Open video and audio
    video = cv2.VideoCapture("fish.mp4")
    pygame.mixer.init()
    pygame.mixer.music.load("fish.mp3")  # Use your video audio if it's separate
    pygame.mixer.music.play(-1, 0.0)  # Loop the audio indefinitely

    # Create canvas to display the video
    canvas = Canvas(root, width=300, height=400)
    canvas.pack()

    def update_frame():
        ret, frame = video.read()
        if ret:
            # Convert the frame to RGB (Tkinter uses RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(img)

            # Update the canvas with the new frame
            canvas.create_image(0, 0, anchor=NW, image=img_tk)
            canvas.img_tk = img_tk

            # Repeat this function after a short delay
            root.after(10, update_frame)

    # Start the video update loop
    update_frame()

    # Run the Tkinter main loop
    root.mainloop()

    # Release the video object after exiting the loop
    video.release()

fish()
