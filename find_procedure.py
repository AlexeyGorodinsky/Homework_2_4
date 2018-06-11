import os

migrations = 'Migrations'
current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), migrations)


if __name__ == '__main__':
    def find_files():
        ext = '.sql'
        files = os.listdir(current_dir)
        while True:
            key_word = input('Введите строку:')
            files2 = []
            if not key_word:
                continue
            files_list = [i for i in files if ext and key_word in i]
            for file_name in files_list:
                files2.append(file_name)
                print(os.path.abspath(file_name))
            files = files2
            print('Всего: {}'.format(len(files_list)))
    pass


print(find_files())
