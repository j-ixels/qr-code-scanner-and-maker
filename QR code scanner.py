import cv2
from pyzbar.pyzbar import decode
import qrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def scan_qr_code():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        for barcode in decode(frame):
            qr_data = barcode.data.decode('utf-8')
            print(f"QR Code Data: {qr_data}")
            cap.release()
            cv2.destroyAllWindows()
            result_label.config(text=f"QR Code Data: {qr_data}")
            return
        cv2.imshow('QR Code Scanner', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def generate_qr_code():
    url = url_entry.get()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)
        qr_code_display.config(image=img)
        qr_code_display.image = img
        result_label.config(text=f"QR Code saved to: {save_path}")

# Setting up the GUI
root = Tk()
root.title("QR Code Scanner and Generator")

# QR Code Scanner Section
scan_button = Button(root, text="Scan QR Code", command=scan_qr_code)
scan_button.pack(pady=10)

# QR Code Generation Section
url_label = Label(root, text="Enter URL:")
url_label.pack(pady=5)

url_entry = Entry(root, width=50)
url_entry.pack(pady=5)

generate_button = Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

qr_code_display = Label(root)
qr_code_display.pack(pady=10)

# Result Display Section
result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
