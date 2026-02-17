from fastapi import FastAPI

app = FastAPI()

books = [
    {"title": "Clean Code", "author": "Robert C. Martin", "publisher": "Prentice Hall"},
    {"title": "Atomic Habits", "author": "James Clear", "publisher": "Avery"},
    {"title": "Deep Work", "author": "Cal Newport", "publisher": "Grand Central"},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "publisher": "Addison-Wesley"}
]

@app.get("/search_books/{key}")
def search_books(key:str):
    for i in books:
        if(
            key.lower() in i["title"].lower()
            or key.lower() in i["author"].lower()
            or key.lower() in i["publisher"].lower()
        ):
            
         return i