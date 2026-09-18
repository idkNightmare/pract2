import json
FILENAME='books.json'
def load_book():
    try:
        with open(FILENAME, 'r',encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return[]
def save_books(books):
    with open(FILENAME, "w",encoding='utf-8') as file:
        json.dump(books,file,ensure_ascii=False,indent=4)
def add_book():
    name=input("введіть назву книги: ").strip()
    autor=input("введіть автора книги: ").strip()
    year=input("введіть рік написання книги: ").strip()
    if not name or not autor or not year:
        print("Ви щось не ввели")
        return
    books=load_book()
    new_book={'name':name,'autor':autor,'year':year}
    books.append(new_book)
    save_books(books)
    print("Все було додано успішно")
def del_book():
    del_books=input("введіть книгу для видалення: ").lower().strip()
    books=load_book()
    lens=len(books)
    books=[book for book in books if book["name"].lower().strip() != del_books]
    if lens>len(books):
        save_books(books)
        print("книга успішно видалена!")
    else:
        print("книгу не знайдено")     
def show_book():
    books=load_book()
    if not books:
        print("не має книг")
        return 
    for index, books in enumerate(books,start=1):
        print(f"{index} - Назва:{books['name']} | Автор:{books['autor']} | Рік випуска:{books['year']}")
def main():
    while True:
        print("\n1 - додати книгу")
        print('2 - видалити книгу')
        print('3 - показати всі книги')
        act=input("виберіть дію 1-3 (або stop для закінчення): ")
        if act == "1":
            add_book()
        elif act == '2':
            del_book()
        elif act == '3':
            show_book()
        elif act == 'stop':
            break
        else:
            print("ви вибрали не існуючу дію!")
if __name__ == '__main__':
    main()