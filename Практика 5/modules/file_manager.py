class FileManager:
    def __init__(self, words_file="modules\\words.txt", record_file="record.txt"):
        self.words_file = words_file
        self.record_file = record_file

    def load_words(self):
        try:
            with open(self.words_file, "r", encoding="utf-8") as f:
                return [word.strip().upper() for word in f if word.strip()]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при загрузке слов: {e}")
            return []

    def save_record(self, record):
        try:
            with open(self.record_file, "w") as f:
                f.write(str(record))
        except Exception as e:
            print(f"Ошибка при сохранении рекорда: {e}")

    def load_record(self):
        try:
            with open(self.record_file, "r") as f:
                return int(f.read())
        except (FileNotFoundError, ValueError):
            return 0
        except Exception as e:
            print(f"Ошибка при загрузке рекорда: {e}")
            return 0