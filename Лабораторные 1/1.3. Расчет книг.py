# Начальные данные
memory = 1.44 # количество мб
pg_num_ = 100 # количество страниц
str_per_pg_ = 50 # количество строк на странице
symb_per_str_ = 25 # количество символов в строке
BYTES_FOR_SYMB = 4 # количество байт

full_symb = symb_per_str_ * str_per_pg_ * pg_num_ # количество символов в 1 книге
mem_for_1book = full_symb * BYTES_FOR_SYMB # память в кб на 1 книгу
amount_of_books = int(memory * 1024 * 1024 // mem_for_1book)

print("Количество книг, помещающихся на дискету:", amount_of_books)
