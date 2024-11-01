# Объявляем функцию single_root_words и пишем в ней параметры root_word и *other_words.
# Создаем внутри функции пустой список same_words.
def single_root_words(root_word, *other_words):
    same_words = []
# Далее выполняем следующее, по условию задачи функция должна составить новый список
# same_words только из тех слов списка other_words, которые содержат root_word или наоборот
# root_word содержит одно из этих слов. После чего должна вернуть список same_words
# в качестве результата своей работы.
# Пишем:
    words = list(other_words)
# При помощи цикла for перебираем подходящие слова.
# Пишем условие задачи, при котором добавляются слова в результирующий список same_words.
# После цикла возвращаем образованный функцией список same_words.
    for i in range(len(words)):
        if root_word.lower() in words[i].lower() or words[i].lower() in root_word.lower():
            same_words.append(words[i])
    return (same_words)
# Вызываем функцию single_root_words и выводим на экран(консоль) возвращённое ей значение.
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
#                Пример результата выполнения программы:
# result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# print(result1)
# print(result2)
# Вывод на консоль:
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']
