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
    <form action="" method="GET">
        <input type="hidden" name="barcode" id="barcode">
    </form>
    <script src="https://unpkg.com/@zxing/library@latest"></script>
    <script>
        const codeReader = new ZXing.BrowserBarcodeReader();
        const videoElement = document.getElementById('video');

        navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
            videoElement.srcObject = stream;
        });

        codeReader.decodeFromVideoDevice(undefined, 'video', (result, err) => {
            if (result) {
                document.getElementById('barcode').value = result.text;
                document.forms[0].submit();
            }
        });
    </script>
</body>
</html>
"""

# Встраивание HTML с камерой на страницу Streamlit
components.html(scanner_html, height=500)

# Получение данных из формы
barcode_data = st.experimental_get_query_params().get('barcode', [''])[0]
if barcode_data:
    st.write(f"Отсканированный штрих-код: {barcode_data}")
