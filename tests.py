from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Война и мир', 'Ужасы']
        ]
    )
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_name_zero_lengh(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_name_more_40_symbols(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить, а вы этого не видите')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_correct_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_incorrect_genre(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Классика')
        assert collector.get_books_genre() == {name: ''}

    def test_get_books_with_specific_genre_check_return_count(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Дум. По колено в крови')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Дум. По колено в крови', 'Ужасы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_genre_equally_3(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Дум. По колено в крови')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Дум. По колено в крови', 'Ужасы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')
        assert len(collector.get_books_genre()) == 3

    def test_get_books_for_children_check_correctly_age_restriction(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Незнайка', 'Мультфильмы')
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_success_add(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    def test_add_book_in_favorites_double_to_favorites(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert collector.favorites.count(name) == 1

    def test_delete_book_from_favorites_check_delete(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Незнайка', 'Мультфильмы')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Незнайка')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.favorites) == 1 and 'Незнайка' in collector.favorites

    def test_get_list_of_favorites_books_check_getter(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        assert len(collector.favorites) == 1
