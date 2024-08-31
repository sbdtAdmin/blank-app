import streamlit as st

# Функция для отображения карточки товара
def product_card(name, price, old_price, rating, sold_count, is_new_supplier):
    new_supplier_text = "Только новые поставщики" if is_new_supplier else ""
    st.markdown(f"""
    <div style="background-color: #ffffff; border-radius: 10px; padding: 20px; width: 200px; margin: 10px; text-align: center; box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);">
        <img src="https://via.placeholder.com/150" style="border-radius: 10px;"/>
        <h4 style="margin: 10px 0;">{name}</h4>
        <p style="margin: 0;"><strong style="color: red;">₪{price}</strong> <span style="text-decoration: line-through; color: gray;">₪{old_price}</span></p>
        <p>⭐ {rating} | {sold_count}+ продано</p>
        <p style="color: green; font-size: small;">{new_supplier_text}</p>
    </div>
    """, unsafe_allow_html=True)

# Заголовок и строка поиска
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <h1 style="margin: 0;">Интернет-Магазин</h1>
        <input type="text" placeholder="Поиск товаров" style="width: 50%; padding: 10px; border-radius: 10px; border: 1px solid #ccc;"/>
        <button style="padding: 10px 20px; border-radius: 10px; background-color: black; color: white; border: none; cursor: pointer;">Поиск</button>
    </div>
""", unsafe_allow_html=True)

# Категории товаров
st.markdown("### Категории")
st.markdown("""
    <div style="display: flex; overflow-x: auto; padding: 10px; background-color: #f5f5f5; border-radius: 10px;">
        <div style="min-width: 100px; padding: 20px; margin-right: 10px; background-color: #ffffff; border-radius: 10px; text-align: center;">
            <img src="https://via.placeholder.com/50" style="border-radius: 50%;"/>
            <p>Электроника</p>
        </div>
        <div style="min-width: 100px; padding: 20px; margin-right: 10px; background-color: #ffffff; border-radius: 10px; text-align: center;">
            <img src="https://via.placeholder.com/50" style="border-radius: 50%;"/>
            <p>Одежда</p>
        </div>
        <div style="min-width: 100px; padding: 20px; margin-right: 10px; background-color: #ffffff; border-radius: 10px; text-align: center;">
            <img src="https://via.placeholder.com/50" style="border-radius: 50%;"/>
            <p>Дом и сад</p>
        </div>
        <!-- Добавьте больше категорий при необходимости -->
    </div>
""", unsafe_allow_html=True)

# Товары
st.markdown("### Рекомендуемые товары")

st.markdown("""
<div style="display: flex; overflow-x: auto; padding: 10px;">
""", unsafe_allow_html=True)

# Пример товаров
products = [
    {"name": "Модуль ESP32", "price": 11.20, "old_price": 62.54, "rating": 4.7, "sold_count": 3000, "is_new_supplier": True},
    {"name": "Аккумулятор 18650", "price": 3.33, "old_price": 26.85, "rating": 4.9, "sold_count": 2000, "is_new_supplier": True},
    {"name": "Зарядное устройство", "price": 18.69, "old_price": 29.99, "rating": 4.8, "sold_count": 500, "is_new_supplier": False},
]

for product in products:
    product_card(product["name"], product["price"], product["old_price"], product["rating"], product["sold_count"], product["is_new_supplier"])

st.markdown("</div>", unsafe_allow_html=True)

# Нижняя навигационная панель
st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: white; box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.1); display: flex; justify-content: space-around; padding: 10px 0; z-index: 999;">
        <div style="text-align: center;">
            <img src="https://via.placeholder.com/30" />
            <p style="margin: 0; font-size: small;">Главная</p>
        </div>
        <div style="text-align: center;">
            <img src="https://via.placeholder.com/30" />
            <p style="margin: 0; font-size: small;">Магазин</p>
        </div>
        <div style="text-align: center;">
            <img src="https://via.placeholder.com/30" />
            <p style="margin: 0; font-size: small;">Корзина</p>
        </div>
        <div style="text-align: center;">
            <img src="https://via.placeholder.com/30" />
            <p style="margin: 0; font-size: small;">Мой профиль</p>
        </div>
    </div>
""", unsafe_allow_html=True)