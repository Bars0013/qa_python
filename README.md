# qa_python

Приложение BooksCollector и класс для тестирования его работы. Приложение позволяет установить жанр книг и добавить их в избранное
Тестовый класс содержит следующие методы:
* test_add_new_book_add_two_books - добавление двух книг
* test_add_new_book_name_zero_lengh - проверка добавления книги с нулевой длинной названия
* test_add_new_book_name_more_40_symbols - проверка добавления книги с длинной названия 41 символ
* test_set_book_genre_correct_genre - проверка корректности установления жанра книге
* test_set_book_genre_incorrect_genre - проверка невозможности установить книге отсутвующий жанр
* test_get_books_with_specific_genre_check_return_count - проверка метода фильтрации по жанру
* test_get_books_genre_equally_3 - проверка получения списка имеющихся книг
* test_get_books_for_children_check_correctly_age_restriction - проверка корректности работы метода ограничения по возрасту
* test_add_book_in_favorites_success_add - проверка механизма добавления в избранное
* test_add_book_in_favorites_double_to_favorites - проверка невозможности добавить два одинаковых фильма в избранное
* test_delete_book_from_favorites_check_delete - проверка метода удаления из избранного
* test_get_list_of_favorites_books_check_getter - проверка метода получения списка избранных фильмов
