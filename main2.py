import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Заголовок приложения
st.title('strelok047')

# Создание вкладки "Загрузка Excel-файла"
st.sidebar.header("Загрузка Excel-файла")
uploaded_file = st.sidebar.file_uploader("Excel", type=["xlsx"])

if uploaded_file is not None:
    # Чтение данных из Excel-файла
    xls = pd.ExcelFile(uploaded_file)

    # Выбор листа из файла Excel
    sheet_name = st.sidebar.selectbox("Выберите лист", xls.sheet_names)

    # Предполагаем, что данные находятся на выбранном листе
    df = xls.parse(sheet_name)

    # Удаление столбца с именем "Год" (замените его на имя вашего столбца)
    if "Год" in df.columns:
        df = df.drop(columns=["Год"])

    # Создание графика на основе данных (первый график - точечная диаграмма)
    x_col = st.sidebar.selectbox("Столбец для оси X", df.columns)
    y_col = st.sidebar.selectbox("Столбец для оси Y", df.columns)

    # Перенесено в этот блок
    st.write(f"### График: {x_col} по отношению к {y_col}")
    st.write("### График данных ")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df[x_col], df[y_col], marker='o')  # Используйте plt.plot для линейной диаграммы с точками
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

    # Кнопка для выполнения анализа данных на основе графика
    if st.button("Выполнить анализ данных"):
        st.write("### Результаты анализа данных")

        # Пример анализа данных с использованием библиотеки seaborn
        sns.pairplot(df[[x_col, y_col]])
        st.pyplot()
