from supp_mods import *

while True:
    work_dir = files.return_curr_dir()
    print(f'Текущий каталог: {work_dir}')
    print('Выберите действие:\n\n0. Сменить рабочий каталог\n1. Преобразовать PDF в Docx\n2. Преобразовать Docx в '
          'PDF\n3. Произвести сжатие изображений\n4. Удалить группу файлов\n5. Выход')
    while True:
        choice = input('Выбор: ')
        if not choice.isdigit() or choice not in ['0', '1', '2', '3', '4', '5']:
            print('Введено неправильное действие!')
        else:
            break
    if choice == '0':
        while True:
            try:
                dirc = input('Введите новый путь: ')
                files.os.chdir(dirc)
                print('Путь успешно изменён')
                break
            except (NotADirectoryError, IsADirectoryError, FileNotFoundError, OSError):
                print('Неправильно введён путь!')
    elif choice == '1':
        docs = files.find_files('.pdf', type=0)
        if docs == {}:
            pass
        else:
            while True:
                choice = input(
                    'Выберите документ, который необходимо конвентировать в .docx (выберите 0, если необходимо конвентировать все): ')
                if not choice.isdigit() or (int(choice) not in list(docs.keys()) and int(choice) != 0):
                    print('Выбран неправильный документ!')
                else:
                    break
            PDF_docx.pdf_to_docx(choice, docs)
    elif choice == '2':
        docs = files.find_files('.docx', type=0)
        if docs == {}:
            pass
        else:
            while True:
                choice = input(
                    'Выберите документ, который необходимо конвентировать в .pdf (выберите 0, если необходимо конвентировать все): ')
                if not choice.isdigit() or (int(choice) not in list(docs.keys()) and int(choice) != 0):
                    print('Выбран неправильный документ!')
                else:
                    break
            PDF_docx.docx_to_pdf(choice, docs)
    elif choice == '3':
        images = files.find_files('.jpg', '.jpeg', '.gif', '.png', type=0)
        if images == {}:
            pass
        else:
            while True:
                choice = input(
                    'Выберите изображение, которое необходимо сжать (выберите 0, если необходимо сжать все): ')
                if not choice.isdigit() or (int(choice) not in list(images.keys()) and int(choice) != 0):
                    print('Выбрано неправильное изображение!')
                else:
                    break
            while True:
                compression = input('Введите степень сжатия (от наибольшей к наименьшей: 1-100): ')
                if not compression.isdigit():
                    print('Введено не число!')
                elif not (1 <= int(compression) <= 100):
                    print('Введите число от 1 до 100')
                else:
                    break
            img_comprs.compress_img(choice, images, compression)
    elif choice == '4':
        print('Выберите действие:\n\n1. Удалить все файлы начинающиеся на введенную подстроку\n2. Удалить все файлы '
              'оканчивающиеся на введенную подстроку\n3. Удалить все файлы содержащие введенную подстроку\n'
              '4. Удалить файлы по расширению')
        while True:
            choice = input('Выбор: ')
            if not choice.isdigit() or choice not in ['1', '2', '3', '4']:
                print('Введено неправильное действие!')
            else:
                break
        podstr = input('Введите подстроку: ')
        files.delete_files(choice, podstr)
    elif choice == '5':
        print('Goodbye :)')
        exit()
    else:  # на случай 'невозможного' случая, easter egg так сказать, ignore...
        print("\033[35m{}".format(' ' * 10 + 'Challenge Complete!\n'),
              "\033[0m{}".format(' ' * 9 + 'How Did We Get Here?'))
