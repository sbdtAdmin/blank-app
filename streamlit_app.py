import streamlit as st
import streamlit.components.v1 as components

st.title("Сканер штрих-кодов")

# JavaScript код для отображения камеры и интерфейса сканера
scanner_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Barcode Scanner</title>
    <style>
        #video {
            position: relative;
            width: 100%;
            max-width: 600px;
            border: 2px solid #000;
        }
        #scanner-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            box-shadow: 0 0 0 2000px rgba(0, 0, 0, 0.7);
            border: 5px solid rgba(255, 0, 0, 0.7);
            box-sizing: border-box;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        #scanner-overlay::before {
            content: "";
            display: block;
            width: 100%;
            height: 2px;
            background: red;
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
        }
    </style>
</head>
<body>
    <div style="position: relative;">
        <video id="video" autoplay></video>
        <div id="scanner-overlay"></div>
    </div>
    <script src="https://unpkg.com/@zxing/library@latest"></script>
    <script>
        const codeReader = new ZXing.BrowserBarcodeReader();
        const videoElement = document.getElementById('video');

        navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
            videoElement.srcObject = stream;
        });

        codeReader.decodeFromVideoDevice(undefined, 'video', (result, err) => {
            if (result) {
                window.parent.postMessage({ type: 'barcode', data: result.text }, '*');
            }
        });
    </script>
</body>
</html>
"""

# Встраивание HTML с камерой на страницу Streamlit
components.html(scanner_html, height=500)

# Получение сообщения от JavaScript
barcode = st.empty()

components.html("""
<script>
    window.addEventListener('message', (event) => {
        if (event.data.type === 'barcode') {
            const barcodeData = event.data.data;
            const streamlitData = JSON.stringify({data: barcodeData});
            fetch("/record_barcode", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: streamlitData
            });
        }
    });
</script>
""", height=0)

# Запрос POST для получения штрих-кода
import json
from streamlit.components.v1 import components

def record_barcode():
    st.write(st.experimental_get_query_params())

components.serve_request_path('/record_barcode', record_barcode)

# Вывод штрих-кода на страницу
barcode_data = st.experimental_get_query_params().get('data', [''])[0]
if barcode_data:
    barcode.text(f"Отсканированный штрих-код: {barcode_data}")
