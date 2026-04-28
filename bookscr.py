import os
import pypandoc

# Ваш путь к папке
target_path = r"D:\Библиотека\Исследования\Искусственный интеллект\Languages\new_handbook_Languages\для гитхаба"

def convert_all_docx(root_path):
    # Проверяем наличие папки
    if not os.path.exists(root_path):
        print(f"Ошибка: Путь {root_path} не найден.")
        return

    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith(".docx") and not file.startswith("~$"):
                input_path = os.path.join(root, file)
                base_name = os.path.splitext(file)[0]
                output_path = os.path.join(root, f"{base_name}.md")
                
                print(f"Конвертирую: {file}...")
                try:
                    pypandoc.convert_file(
                        input_path, 
                        'commonmark', 
                        outputfile=output_path,
                        extra_args=['--extract-media=' + root]
                    )
                except Exception as e:
                    print(f"Ошибка в файле {file}: {e}")

if __name__ == "__main__":
    convert_all_docx(target_path)
    print("Готово. Теперь в папках появились .md файлы.")