# Счетчик словарного запаса

## Описание
Решила я учить иностранный язык, но не просто по словам, которые в учебнике, а по тем, что использую в повседневном общении при переписке.

Это скрипт на Python, который подсчитывает частоту слов в текстовом файле или коллекции текстовых файлов. Он использует библиотеку BeautifulSoup для разбора HTML-файлов и модуль регулярных выражений для разделения слов.

## Предварительные условия

Перед запуском скрипта убедитесь, что у вас установлено следующее:

- Python 3.x
- Библиотека BeautifulSoup

## Использование

1. Экспортируйте историю чата из Telegram.
2. Поместите ваши HTML-файлы в каталог с именем "ChatExport" в том же каталоге, что и скрипт.
3. Запустите скрипт с помощью интерпретатора Python.

## Алгоритм

1. Создаётся пустой словарь под названием "vocabulary" для хранения частот слов.
2. Выполните итерацию по каждому файлу в каталоге "ChatExport".
3. Каждый файл анализируется с помощью BeautifulSoup.
4. Происходит поиск сообщений в тегах "div" c классом "text".
5. Каждое сообщения преобразуется в текст в нижним регистре и разделяется на слова с помощью регулярных выражений.
6. Проверяется, чтобы слова были только на русском.
7. Для каждого слова провяется, существует ли оно уже в словаре vocabulary.
8. Если этого слова нет в словаре, оно добавляется в качестве нового ключа со значением 1.
9. Если слово уже есть в словаре, увеличивается его значение на 1.
10. Словарь сортируется по ключам.
11. В файл с именем "vocabulary.txt " и добавляются слова с частотой, превышающей 3.
12. Выводится общее количество уникальных слов в словаре.

## Результаты

Скрипт сгенерирует файл с именем "vocabulary.txt ", содержащий слова с частотой, превышающей 3.

Пожалуйста, обратите внимание, что скрипт предполагает, что текстовые файлы закодированы в UTF-8. Если ваши файлы имеют другую кодировку, вам может потребоваться изменить параметр "encoding" в строке 11 скрипта.
