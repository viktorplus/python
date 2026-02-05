import os
# Список содержимого текущей директории
contents = os.listdir(".")
print("Содержимое текущей директории:", contents)
# Список содержимого указанной директории
specific_dir = "report"
if os.path.exists(specific_dir):
    print(f"Содержимое директории '{specific_dir}':",
os.listdir(specific_dir))