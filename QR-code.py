import streamlit as st
import qrcode
import cv2

# Function to generate a QR code
def generate_qr(data):
    qr = qrcode.make(data)  # Generate QR code
    qr.save("qr_code.png")  # Save as an image
    return "qr_code.png"

# Function to decode a QR code
def decode_qr(image_path):
    img = cv2.imread(image_path)
    qr_code_detector = cv2.QRCodeDetector()
    data, _, _ = qr_code_detector.detectAndDecode(img)
    return data if data else "No QR code found."

# Streamlit UI
st.title("QR Code Generator & Decoder")

# QR Code Generation
st.subheader("Generate QR Code")
input_text = st.text_input("Enter text or URL")
if st.button("Generate"):
    qr_path = generate_qr(input_text)
    st.image(qr_path, caption="Generated QR Code")

# QR Code Decoding
st.subheader("Decode QR Code")
uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    with open("uploaded_qr.png", "wb") as f:
        f.write(uploaded_file.getbuffer())
    decoded_data = decode_qr("uploaded_qr.png")
    st.write("Decoded Data:", decoded_data)
