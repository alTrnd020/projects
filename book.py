from tkinter import *
books = {
    "کتاب 1": {"نویسنده": "نویسنده 1", "ژانر": "ادبیات"},
    "کتاب 2": {"نویسنده": "نویسنده 2", "ژانر": "علمی"},
    "کتاب 3": {"نویسنده": "نویسنده 3", "ژانر": "تخیلی"},
    "کتاب 4": {"نویسنده": "نویسنده 1", "ژانر": "ادبیات"},
    "کتاب 5": {"نویسنده": "نویسنده 4", "ژانر": "تاریخی"},
    "کتاب 6": {"نویسنده": "نویسنده 2", "ژانر": "علمی"},
}


def categorize_books(books):
    categorized_books = {}
    
    for book, info in books.items():
        genre = info["ژانر"]
        author = info["نویسنده"]
        
        if genre not in categorized_books:
            categorized_books[genre] = {}
        
        if author not in categorized_books[genre]:
            categorized_books[genre][author] = []
        
        categorized_books[genre][author].append(book)
    
    return categorized_books


categorized_books = categorize_books(books)

for genre, authors in categorized_books.items():
    print(f"ژانر: {genre}")
    for author, titles in authors.items():
        print(f"  نویسنده: {author}")
        for title in titles:
            print(f"    - {title}")


root = Tk()
root.geometry("300x350")
root.resizable(False , False)
root.title ("book categories")
root.config("sky blue")

root.mainloop()