import json
FILENAME='books.json'
def load_book():
    with open(FILENAME, 'r',encoding='uft=8') as file:
        return json.load(file)
def save_books(books):
    with open(FILENAME, "w",encoding='uft=8') as file:
        json.dump(books,file,ensure_ascii=False,indent=4)
def add_book():
    with open(FILENAME, "w",encoding='uft=8') as file:
        name=input("введіть назву книги: ")
        autor=input("введіть автора книги: ")
        year=input("введіть рік написання книги: ")
    if not name or not autor or not year:
        return "Ви щось не ввели"
    books=load_book()
    new_book={'name':name,'autor':autor,'year':year}
    books.append(new_book)
    save_books(books)
    print("Все було додано успішно")
def del_book():
    del_books=input("введіть книгу для видалення: ")
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
while True: