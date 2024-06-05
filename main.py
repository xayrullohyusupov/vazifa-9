import os
import threading


vowels = "aeiouAEIOU"

def count(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            count = sum(1 for char in text if char in vowels)
            print(f"{file_path} faylida {count} ta unli harf bor.")
    except Exception as e:
        print(f"{file_path} faylini o'qishda xato yuz berdi: {e}")

def main():
    current = os.getcwd()
    txt_files = [file for file in os.listdir(current) if file.endswith('.txt')]

    threads = []
    for txt_file in txt_files:
        thread = threading.Thread(target=count, args=(os.path.join(current, txt_file),))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
