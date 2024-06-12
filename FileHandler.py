class FileHandler:

    @staticmethod
    def append_to_file(text,file_name):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(text + "\n")

    @staticmethod
    def add_data(text):
        FileHandler.append_to_file(text,'user-name.txt')

    @staticmethod
    def log(text):
        FileHandler.append_to_file(text,'log.txt')
