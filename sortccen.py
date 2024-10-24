import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import re  # Импортируем модуль для работы с регулярными выражениями

def sort_files():
    mods_folder = folder_path.get()  # Получаем путь к папке с файлами
    sorted_folder = os.path.join(mods_folder, "Sorted_CC")

    if not os.path.exists(sorted_folder):
        os.makedirs(sorted_folder)

        # (Здесь можно вставить код для сортировки файлов)

        keywords = {
            r'.*?hairstyle.*?': 'Hairstyle',
            r'.*?boot.*?': 'Footwear',
            r'.*?shoe.*?': 'Footwear',
            r'.*?sneaker.*?': 'Footwear',
            r'.*?sandals.*?': 'Footwear',
            r'.*?panti.*?': 'Underwear',
            r'.*?bikini.*?': 'Underwear',
            r'.*?lingerie.*?': 'Underwear',
            r'.*?skirt.*?': 'Bottom of the clothes',
            r'.*?underwear.*?': 'Underwear',
            r'.*?outerwear.*?': 'Outerwear',
            r'.*?coat.*?': 'Outerwear',
            r'.*?sweater.*?': 'Upper part of the clothes',
            r'.*?liner.*?': 'Liner',
            r'.*?lip.*?': 'Lips',
            r'.*?lash.*?': 'Eyelash',
            r'.*?swimsuit.*?': 'Underwear',
            r'.*?short.*?': 'Underwear',
            r'.*?swimwear.*?': 'Underwear',
            r'.*?beachwear.*?': 'Underwear',
            r'.*?panty.*?': 'Underwear',
            r'.*?blouse.*?': 'Upper part of the clothes',
            r'.*?loafers.*?': 'Footwear',
            r'.*?dress.*?': 'Clothes',
            r'.*?overalls.*?': 'Clothes',
            r'.*?shorts.*?': 'Bottom of the clothes',
            r'.*?shirt.*?': 'Upper part of the clothes',
            r'.*?pants.*?': 'Bottom of the clothes',
            r'.*?joggers.*?': 'Bottom of the clothes',
            r'.*?legging.*?': 'Bottom of the clothes',
            r'.*?crocs.*?': 'Footwear',
            r'.*?cardigan.*?': 'Upper part of the clothes',
            r'.*?hoodie.*?': 'Upper part of the clothes',
            r'.*?jacket.*?': 'Upper part of the clothes',
            r'.*?robe.*?': 'Outerwear',
            r'.*?uniform.*?': 'Clothes',
            r'.*?belt.*?': 'Accessories',
            r'.*?glasses.*?': 'Glasses',
            r'.*?gloves.*?': 'Gloves',
            r'.*?choker.*?': 'Accessories for neck',
            r'.*?hat(s)?': 'Hats',
            r'.*?nails.*?': 'Nails',
            r'.*?ring.*?': 'Rings',
            r'.*?necklace.*?': 'Accessories for neck',
            r'.*?watch.*?': 'Accessories for arms',
            r'.*?sock.*?': 'Socks',
            r'.*?stocking.*?': 'Socks',
            r'.*?tights.*?': 'Socks',
            r'.*?earrings.*?': 'Earrings',
            r'.*?bracelet.*?': 'Accessories fo arms',
            r'.*?scarf.*?': 'Accessories for neck',
            r'.*?eyeshadow.*?': 'Eyeshadow',
            r'.*?eyelash.*?': 'Eyelash',
            r'.*?blush.*?': 'Blush',
            r'.*?freckles.*?': 'Skin Features',
            r'.*?pajama.*?': 'Underwear',
            r'.*?mole.*?': 'Skin Features',
            r'.*?armuff.*?': 'Accessories',
            r'.*?cap.*?': 'Hats',
            r'.*?goggles.*?': 'Glasses',
            r'.*?beanie.*?': 'Hats',
            r'.*?pijama.*?': 'Underwear',
            r'.*?corset.*?': 'Upper part of the clothes',
            r'.*?blazer.*?': 'Upper part of the clothes',
            r'.*?pumps.*?': 'Footwear',
            r'.*?slippers.*?': 'Footwear',
            r'.*?accessories.*?': 'Accessories',
            r'.*?sleeves.*?': 'Accessories for arms',
            r'.*?jeans.*?': 'Bottom of the clothes',
            r'.*?tatoo.*?': 'Tattoo',
            r'.*?mask.*?': 'Skin Features',
            r'.*?hat.*?': 'Hats',
            r'.*?mark.*?': 'Skin Features',
            r'.*?scar.*?': 'Skin Features',
            r'.*?eye.*?': 'Eye',
            r'.*?nose.*?': 'Nose',
            r'.*?bra.*?': 'Underwear',
            r'.*?outfit.*?': 'Clothes',
            r'.*?costume.*?': 'Clothes',
            r'.*?suit.*?': 'Clothes',
            r'.*?fullbody.*?': 'Clothes',
            r'.*?neck.*?': 'Accessories for neck',
            r'.*?cloth.*?': 'Clothes',
            r'.*?top.*?': 'Upper part of the clothes',
            r'.*?hair.*?': 'Hairstyle',
            r'.*?makeup.*?': 'Make up',
            r'.*?slider.*?': 'Sliders',
            r'.*?skin.*?': 'Skin',
            r'.*?object.*?': 'Objects',
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
                other_folder = os.path.join(sorted_folder, 'Others')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, file_name))

    messagebox.showinfo("Ready!", "Sorting completed!")

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

app = tk.Tk()
app.title("CC Sorting for The Sims 4")

folder_path = tk.StringVar()

tk.Label(app, text="Select folder with mods:").pack(pady=10)
tk.Entry(app, textvariable=folder_path, width=50).pack(pady=5)
tk.Button(app, text="Select folder", command=select_folder).pack(pady=5)
tk.Button(app, text="Sort CC", command=sort_files).pack(pady=20)

app.mainloop()
