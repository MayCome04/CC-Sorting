import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import re  # Импортируем модуль для работы с регулярными выражениями

def sort_files():
    mods_folder = folder_path.get()  # Получаем путь к папке с файлами
    sorted_folder = os.path.join(mods_folder, "Отсортированные CC")

    if not os.path.exists(sorted_folder):
        os.makedirs(sorted_folder)

        # Ключевые слова для сортировки
        keywords = {
            r'.*?hairstyle.*?': 'Hairstyle',
            r'.*?boot.*?': 'Обувь',
            r'.*?shoe.*?': 'Обувь',
            r'.*?sneaker.*?': 'Обувь',
            r'.*?sandals.*?': 'Обувь',
            r'.*?panti.*?': 'Нижнее бельё',
            r'.*?bikini.*?': 'Нижнее бельё',
            r'.*?lingerie.*?': 'Нижнее бельё',
            r'.*?skirt.*?': 'Нижняя часть одежды',
            r'.*?underwear.*?': 'Нижнее бельё',
            r'.*?outerwear.*?': 'Верхняя одежда',
            r'.*?coat.*?': 'Верхняя одежда',
            r'.*?sweater.*?': 'Верхняя часть одежды',
            r'.*?nose.*?': 'Нос',
            r'.*?liner.*?': 'Подводка',
            r'.*?lip.*?': 'Губы(помада)',
            r'.*?lash.*?': 'Ресницы',
            r'.*?swimsuit.*?': 'Нижнее бельё',
            r'.*?short.*?': 'Нижнее бельё',
            r'.*?sweamwear.*?': 'Нижнее бельё',
            r'.*?beachwear.*?': 'Нижнее бельё',
            r'.*?panty.*?': 'Нижнее бельё',
            r'.*?blouse.*?': 'Верхняя часть одежды',
            r'.*?loafers.*?': 'Обувь',
            r'.*?dres.*?': 'Одежда',
            r'.*?overalls.*?': 'Одежда',
            r'.*?suit.*?': 'Верхняя часть одежды',
            r'.*?shorts.*?': 'Нижняя часть одежды',
            r'.*?shirt.*?': 'Верхняя часть одежды',
            r'.*?pants.*?': 'Нижняя часть одежды',
            r'.*?joggers.*?': 'Нижняя часть одежды',
            r'.*?legging.*?': 'Нижняя часть одежды',
            r'.*?crocs.*?': 'Обувь',
            r'.*?cardigan.*?': 'Верхняя часть одежды',
            r'.*?hoodie.*?': 'Верхняя часть одежды',
            r'.*?jacket.*?': 'Верхняя часть одежды',
            r'.*?robe.*?': 'Одежда',
            r'.*?uniform.*?': 'Одежда',
            r'.*?belt.*?': 'Аксессуары',
            r'.*?glasses.*?': 'Очки',
            r'.*?gloves.*?': 'Перчатки',
            r'.*?choker.*?': 'Аксессуары для шеи',
            r'.*?hat.*?': 'Головные уборы',
            r'.*?nails.*?': 'Ногти',
            r'.*?ring.*?': 'Кольца',
            r'.*?necklace.*?': 'Аксессуары для шеи',
            r'.*?watch.*?': 'Наручные аксессуары',
            r'.*?socks.*?': 'Носки',
            r'.*?stocking.*?': 'Носки',
            r'.*?tights.*?': 'Носки',
            r'.*?earrings.*?': 'Серьги',
            r'.*?bracelet.*?': 'Наручные аксессуары',
            r'.*?scarf.*?': 'Аксессуары для шеи',
            r'.*?eyeshadow.*?': 'Тени для глаз',
            r'.*?eyelash.*?': 'Ресницы(тушь)',
            r'.*?blush.*?': 'Румянец(пудра)',
            r'.*?freckles.*?': 'Особенности кожи',
            r'.*?pajama.*?': 'Нижнее бельё',
            r'.*?mole.*?': 'Особенности кожи',
            r'.*?armuff.*?': 'Аксессуары',
            r'.*?cap.*?': 'Головные уборы',
            r'.*?goggles.*?': 'Очки',
            r'.*?beanie.*?': 'Головные уборы',
            r'.*?pijama.*?': 'Нижнее бельё',
            r'.*?corset.*?': 'Верхняя часть одежды',
            r'.*?blazer.*?': 'Верхняя часть одежды',
            r'.*?pumps.*?': 'Обувь',
            r'.*?slippers.*?': 'Обувь',
            r'.*?accessories.*?': 'Аксессуары',
            r'.*?sleeves.*?': 'Наручные аксессуары',
            r'.*?jeans.*?': 'Нижняя часть одежды',
            r'.*?tatoo.*?': 'Тату',
            r'.*?mask.*?': 'Особенности кожи',
            r'.*?hat.*?': 'Головные уборы',
            r'.*?tatoo.*?': 'Тату',
            r'.*?mark.*?': 'Особенности кожи',
            r'.*?scar.*?': 'Особенности кожи',
            r'.*?eye.*?': 'Глаза',
            r'.*?bra.*?': 'Нижнее бельё',
            r'.*?outfit.*?': 'Одежда',
            r'.*?costume.*?': 'Одежда',
            r'.*?suit.*?': 'Одежда',
            r'.*?fullbody.*?': 'Одежда',
            r'.*?neck.*?': 'Аксессуары',
            r'.*?cloth.*?': 'Одежда',
            r'.*?top.*?': 'Верхняя часть одежды',
            r'.*?hair.*?': 'Hairstyle',
            r'.*?makeup.*?': 'Макияж',
            r'.*?slider.*?': 'Слайдеры',
            r'.*?skin.*?': 'Кожа',
            r'.*?object.*?': 'Объекты',
            # можно добавить больше категорий
        }

    for file_name in os.listdir(mods_folder):  # Меняем folder_path на mods_folder
        file_path = os.path.join(mods_folder, file_name)

        if os.path.isfile(file_path):
            category = None

            # Проверяем ключевые слова в имени файла
            for keyword, folder_name in keywords.items():
                if re.search(keyword, file_name.lower()):  # Используем регулярное выражение
                    category = folder_name
                    break

            if category:
                category_folder = os.path.join(sorted_folder, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                shutil.move(file_path, os.path.join(category_folder, file_name))
            else:
                # Файлы без определенного типа отправляем в "Прочее"
                other_folder = os.path.join(sorted_folder, 'Прочее')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, file_name))

    messagebox.showinfo("Готово!", "Сортировка завершена!")

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

app = tk.Tk()
app.title("Сортировка CC для The Sims 4")

folder_path = tk.StringVar()

tk.Label(app, text="Выберите папку с модами:").pack(pady=10)
tk.Entry(app, textvariable=folder_path, width=50).pack(pady=5)
tk.Button(app, text="Выбрать папку", command=select_folder).pack(pady=5)
tk.Button(app, text="Сортировать CC", command=sort_files).pack(pady=20)

app.mainloop()
