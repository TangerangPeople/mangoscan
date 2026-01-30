import gradio as gr
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# 1. Load model dari folder yang sama
# Pastikan nama file .h5 lo sama persis dengan yang di bawah ini
model = load_model("MangoScanModel.h5")

# List class sesuai urutan di kodingan training lo
classes = ["Mentah", "Setengah Matang", "Matang", "Terlalu Matang", "Busuk"]

def predict_mango(img):
    try:
        # Pastikan gambar RGB dan resize ke ukuran 224x224 (sesuai training)
        img = img.convert("RGB").resize((224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)[0]
        
        # Format output biar jadi label yang cakep di Gradio
        return {classes[i]: float(prediction[i]) for i in range(len(classes))}
    except Exception as e:
        return {"Error": str(e)}

# 2. Interface Gradio
interface = gr.Interface(
    fn=predict_mango,
    inputs=gr.Image(type="pil", label="Upload Foto Mangga"),
    outputs=gr.Label(num_top_classes=5),
    title="🍋 MangoScan",
    description="Aplikasi AI untuk mendeteksi tingkat kematangan buah mangga secara otomatis."
)

if __name__ == "__main__":
    interface.launch()
