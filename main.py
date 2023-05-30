# Ваша задача: починить адресную книгу, используя регулярные выражения.
# Структура данных будет всегда:
# lastname,firstname,surname,organization,position,phone,email
# Предполагается, что телефон и e-mail у человека может быть только один.
#
# Необходимо:
#
# Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.
# Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
# Объединить все дублирующиеся записи о человеке в одну.

from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
## Ваш код
num_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
             r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
             r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'

num_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\20'
contacts_list_new = []
for page in contacts_list:
    page_string = ','.join(page)  # объединение в строку
    format_page = re.sub(num_pattern, num_pattern_new, page_string)  # замена шаблонов в строке
    page_list = format_page.split(',')  # формируем список строк
    contacts_list_new.append(page_list)
    # print(contacts_list_new)

name_pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
               r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
name_pattern_new = r'\1\3\10\4\6\9\7\8'
contacts_list = []  # создаем список
for page in contacts_list_new:
    page_string = ','.join(page)  # объединение в строку
    format_page = re.sub(name_pattern, name_pattern_new, page_string)
    page_list = format_page.split(',')  # формируем список строк
    if page_list not in contacts_list:
        contacts_list.append(page_list)
        # print(contacts_list)

# убираем дубликаты
for i in contacts_list:
    for j in contacts_list:
        if i[0] == j[0] and i[1] == j[1]:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]


# pprint(contacts_list)


contact_list_upd = []
duplicate_check = []
for page in contacts_list:
    if page[0] not in duplicate_check:
        duplicate_check.append(page[0])
        contact_list_upd.append(page)

pprint(contact_list_upd)
## 2. Сохраните получившиеся данные в другой файл.
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contact_list_upd)
