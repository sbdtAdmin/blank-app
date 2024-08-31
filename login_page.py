import streamlit as st

# Функция для проверки логина и пароля
def check_login(username, password):
    if username == "user" and password == "pass":
        return True
    return False

# Функция для регистрации (заглушка)
def register_user(username, password):
    st.session_state['registered_users'][username] = password
    st.success("Регистрация прошла успешно! Теперь вы можете войти.")

# Страница входа
def login_page():
    st.title("Вход в Интернет-Магазин")
    
    username = st.text_input("Имя пользователя")
    password = st.text_input("Пароль", type="password")
    
    if st.button("Войти"):
        if check_login(username, password):
            st.success("Успешный вход!")
            st.session_state['logged_in'] = True
        else:
            st.error("Неверное имя пользователя или пароль")

    if st.button("Регистрация"):
        st.session_state['register'] = True

    if st.button("Войти как гость"):
        st.session_state['logged_in'] = True
        st.session_state['guest'] = True
        st.success("Вы вошли как гость!")

# Страница регистрации
def register_page():
    st.title("Регистрация")
    
    username = st.text_input("Придумайте имя пользователя")
    password = st.text_input("Придумайте пароль", type="password")
    confirm_password = st.text_input("Подтвердите пароль", type="password")
    
    if st.button("Зарегистрироваться"):
        if password == confirm_password:
            if username in st.session_state['registered_users']:
                st.error("Пользователь с таким именем уже существует.")
            else:
                register_user(username, password)
                st.session_state['register'] = False
        else:
            st.error("Пароли не совпадают.")

    if st.button("Назад к входу"):
        st.session_state['register'] = False