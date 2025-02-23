class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, title, description):  # Добавил задачу
        self.__tasks.append({"title": title, "description": description, "done": False})

    def remove_task(self, title):  # убрал задачу
        self.__tasks = [task for task in self.__tasks if task['title'] != title]

    def mark_as_done(self, title):  # сделал
        for task in self.__tasks:
            if task['title'] == title:
                task['done'] = True
                break

    def show_tasks(self):  # что осталось сделать
        if not self.__tasks:
            print("Задач для выполнения нема")
        else:
            for task in self.__tasks:
                status = "Выполнено" if task['done'] else "Не выполнено"
                print(f"Задача: {task['title']} \nОписание: {task['description']} \nСтатус: {status}\n")

    def get_tasks(self):
        return self.__tasks

    def set_tasks(self, tasks):
        self.__tasks = tasks

    def __str__(self):  # чтобы когда я просил вывести выводилось строчкой
        return f"Количество задач: {len(self.__tasks)}"


if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.add_task("купить хлеб", "купить пепси)
    task_manager.add_task("встретиться с другом", "погулять")

    task_manager.mark_as_done("купить хлеб")
    task_manager.show_tasks()

    task_manager.remove_task("купить хлеб")  # типо я уже сделал дз по школе и я его не считаю
    task_manager.show_tasks()  # все что осталось сделать

    print(f"{task_manager}\nСПАСИБО ЗА ВНИМАНИЕ К МОЕМУ ТВОРЕНИЮ:)")
