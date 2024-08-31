import streamlit as st
from login_page import login_page, register_page

# Функция для отображения карточки товара
def product_card(name, price, description):
    st.markdown(f"""
    <div style="background-color: #f9f9f9; border-radius: 10px; padding: 20px; width: 200px; margin: 10px;">
        <h4 style="margin: 0;">{name}</h4>
        <p style="margin: 0;"><strong>Цена: ${price}</strong></p>
        <p>{description}</p>
        <button onclick="document.getElementById('{name}_order').click()">Заказать сейчас</button>
        <button onclick="document.getElementById('{name}_cart').click()">Добавить в корзину</button>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button(f"Заказать сейчас - {name}", key=f"{name}_order"):
        st.success(f"Вы заказали {name} на сумму ${price}.")
    
    if st.button(f"Добавить в корзину - {name}", key=f"{name}_cart"):
        if 'cart' not in st.session_state:
            st.session_state['cart'] = []
        st.session_state['cart'].append({"name": name, "price": price})
        st.success(f"{name} добавлен в корзину.")

# Функция отображения главной страницы
def main_page():
    st.title("Главная страница Интернет-Магазина")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("Перейти в корзину"):
            st.write("Переход в корзину...")
            if 'cart' in st.session_state and st.session_state['cart']:
                st.write("Ваши товары в корзине:")
                for item in st.session_state['cart']:
                    st.write(f"- {item['name']} (${item['price']})")
            else:
                st.write("Ваша корзина пуста.")

    with col2:
        if st.button("Поиск"):
            search_term = st.text_input("Введите поисковой запрос")
            if search_term:
                st.write(f"Результаты поиска для: {search_term}")

    with col3:
        if st.button("Каталог товаров"):
            st.write("Переход в каталог...")

    st.subheader("Рекомендуемые товары")

    # Рекомендуемые товары
    recommended_products = [
        {"name": "Smartphone X", "price": 799.99, "description": "Лучший смартфон года."},
        {"name": "Laptop Pro", "price": 1299.99, "description": "Высокопроизводительный ноутбук."},
    ]

    # Добавляем карусель для рекомендуемых товаров
    st.markdown("""
    <div style="display: flex; overflow-x: scroll;">
    """, unsafe_allow_html=True)

    for product in recommended_products:
        product_card(product["name"], product["price"], product["description"])

    st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("Товары по категориям")

    categories = {
        "Электроника": [
            {"name": "Телевизор Ultra HD", "price": 499.99, "description": "Телевизор с ультравысоким разрешением."},
            {"name": "Наушники Wireless", "price": 149.99, "description": "Беспроводные наушники с высоким качеством звука."}
        ],
        "Бытовая техника": [
            {"name": "Холодильник No Frost", "price": 699.99, "description": "Современный холодильник с функцией No Frost."},
            {"name": "Микроволновая печь", "price": 99.99, "description": "Компактная микроволновка для быстрого разогрева."}
        ],
        "Одежда": [
            {"name": "Куртка зимняя", "price": 199.99, "description": "Теплая зимняя куртка."},
            {"name": "Кроссовки спортивные", "price": 129.99, "description": "Удобные спортивные кроссовки для бега."}
        ]
    }

    for category, products in categories.items():
        st.write(f"### {category}")
        st.markdown("""
        <div style="display: flex; overflow-x: scroll;">
        """, unsafe_allow_html=True)

        for product in products:
            product_card(product["name"], product["price"], product["description"])

        st.markdown("</div>", unsafe_allow_html=True)

# Основная логика приложения
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'register' not in st.session_state:
    st.session_state['register'] = False

if 'registered_users' not in st.session_state:
    st.session_state['registered_users'] = {}

if st.session_state['logged_in']:
    main_page()
elif st.session_state['register']:
    register_page()
else:
    login_page()