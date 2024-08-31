import streamlit as st
import base64

# HTML и JS код для камеры и сканирования штрих-кодов
camera_html = """
<video id="preview"></video>
<script src="https://rawgit.com/schmich/instascan-builds/master/instascan.min.js"></script>
<script type="text/javascript">
    var scanner = new Instascan.Scanner({ video: document.getElementById('preview') });
    scanner.addListener('scan', function (content) {
        Streamlit.setComponentValue(content);
    });
    Instascan.Camera.getCameras().then(function (cameras) {
        if (cameras.length > 0) {
            scanner.start(cameras[0]);
        } else {
            console.error('No cameras found.');
        }
    }).catch(function (e) {
        console.error(e);
    });
</script>
"""

st.markdown(camera_html, unsafe_allow_html=True)

# Получение данных штрих-кода
barcode_data = st.text_input("Сканированный штрих-код:")

if barcode_data:
    st.success(f"Штрих-код распознан: {barcode_data}")
    # Логика добавления товара на склад по распознанному штрих-коду
