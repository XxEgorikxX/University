from modules import *

while True:
    work_dir = filework.return_curr_dir()

    print(f'Нынешняя директория: {work_dir}')
    print('Выберите действие:\n\n0. Сменить рабочий каталог\n1. Преобразовать PDF в Docx\n2. Преобразовать Docx в '
          'PDF\n3. Произвести сжатие изображений\n4. Удалить группу файлов\n5. Выход')
    

    while True:
        choice = input('Выбор: ')

        if not choice.isdigit() or choice not in ['0', '1', '2', '3', '4', '5']:
            print('Вы неправильно выбрали действие или ввели не число! \nВведите ещё раз: ')

        else:
            break


    if choice == '0':
        while True:

            try:
                dirc = input('Введите новый путь к рабочей директории: ')
                filework.os.chdir(dirc)
                print(f'Путь успешно изменён. \nНовая рабочая директория: {dirc}')
                break

            except (NotADirectoryError, IsADirectoryError, FileNotFoundError, OSError):
                print('Путь не существует...')


    elif choice == '1':
        docs = filework.find_files('.pdf', type=0)

        if docs == {}:
            pass

        else:
            while True:
                choice = input('Выберите файл для преобразования в .docx. \nВыберите 0, если необходимо конвентировать все. ')

                if not choice.isdigit() or (int(choice) not in list(docs.keys()) and int(choice) != 0):
                    print('Некорректный выбор документа.')

                else:
                    break

            pdf_docx_func.pdf_to_docx(choice, docs)


    elif choice == '2':
        docs = filework.find_files('.docx', type=0)

        if docs == {}:
            pass

        else:
            while True:
                choice = input('Выберите файл для преобразования в .pdf. \nВыберите 0, если необходимо конвентировать все. ')

                if not choice.isdigit() or (int(choice) not in list(docs.keys()) and int(choice) != 0):
                    print('Некорректный выбор документа.')

                else:
                    break

            pdf_docx_func.docx_to_pdf(choice, docs)


    elif choice == '3':
        images = filework.find_files('.jpg', '.jpeg', '.png', type=0)

        if images == {}:
            pass

        else:
            while True:
                choice = input('Выберите изображение, которое необходимо сжать. \nВыберите 0, если необходимо сжать все. ')

                if not choice.isdigit() or (int(choice) not in list(images.keys()) and int(choice) != 0):
                    print('Выбрано неправильное изображение!')

                else:
                    break

            while True:
                compression = input('Введите на сколько процентов от 0% до 100% вы хотите сжать изображение: ')

                if not compression.isdigit():
                    print('Введено не число!')

                elif not (1 <= int(compression) <= 100):
                    print('Введите число от 1 до 100')

                else:
                    break

            compress_image.compress_img(choice, images, compression)


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
        filework.delete_files(choice, podstr)


    elif choice == '5':
        print('Выход из программы, всем пока :)')
        exit()