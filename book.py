import json
FILENAME="tasks.json"
def load_tasks():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_tasks(tasks):
    with open(FILENAME,"w", encoding="utf-8") as file:
        json.dump(tasks,file,ensure_ascii=False,indent=4)
def add_tasks():
    name=input("введіть назву: ").strip()
    priority=input("який пріорітет: ").strip()
    deadline=input("який дедлайн: ").strip()
    if not name or not priority or not deadline:
        print("Помилка! ви ввели в якомусь полі нічого")
        return
    tasks = load_tasks()
    new_task={"name":name,"priority":priority,"deadline":deadline}
    tasks.append(new_task)
    save_tasks(tasks)
    print("все було успішно додано!")
def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("поки не має завдань")
        return
    for index, task in enumerate(tasks,start=1):
        print(f"{index}. {task['name']} | Пріорітет:{task['priority']} | Дедлайн:{task['deadline']}")
def delete_task():
    title_to_delete=input("виберіть те що видалити: ").strip().lower()
    tasks=load_tasks()
    initial_count=len(tasks)
    tasks=[task for task in tasks if task["name"].strip().lower() != title_to_delete]
    if len(tasks)<initial_count:
        save_tasks(tasks)
        print("успішно видалено!")
    else:
        print("завдання не знайдено")
def main():
    while True:
        print("\n === Меню Завдань === ")
        print("1: показати всі завданні")
        print("2: додати завдання")
        print("3: видалити завдання")
        print("4: вийти")
        choise=input("оберіть дію (1-4): ").strip()
        if choise=="1":
            show_tasks()
        elif choise=="2":
            add_tasks()
        elif choise=="3":
            show_tasks()
            delete_task()
        elif choise=="4":
            print("ви вийшли, до зустрічі!")
            break
        else:
            print("ви ввели не коректну дію!")
if __name__ == "__main__":
    main()

