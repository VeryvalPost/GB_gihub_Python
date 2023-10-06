import json
import os

def create_note():
    note_title = input("Введите заголовок заметки: ")
    note_content = input("Введите содержимое заметки: ")
    note = {"title": note_title, "content": note_content}
    save_note(note)
    print("Заметка успешно создана.")

def save_note(note):
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
    else:
        notes = []
    notes.append(note)
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def read_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
        if notes:
            for i, note in enumerate(notes, 1):
                print(f"Заметка {i}:")
                print(f"Заголовок: {note['title']}")
                print(f"Содержимое: {note['content']}")
                print()
        else:
            print("Нет доступных заметок.")
    else:
        print("Нет доступных заметок.")

def edit_note():
    note_number = int(input("Введите номер заметки, которую вы хотите отредактировать: "))
    with open("notes.json", "r") as file:
        notes = json.load(file)
    if note_number <= len(notes):
        new_content = input("Введите новое содержимое заметки: ")
        notes[note_number-1]["content"] = new_content
        with open("notes.json", "w") as file:
            json.dump(notes, file)
        print("Заметка успешно отредактирована.")
    else:
        print("Неверный номер заметки.")

def delete_note():
    note_number = int(input("Введите номер заметки, которую вы хотите удалить: "))
    with open("notes.json", "r") as file:
        notes = json.load(file)
    if note_number <= len(notes):
        del notes[note_number-1]
        with open("notes.json", "w") as file:
            json.dump(notes, file)
        print("Заметка успешно удалена.")
    else:
        print("Неверный номер заметки.")

def main():
    while True:
        print("Меню:")
        print("1. Создать заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()