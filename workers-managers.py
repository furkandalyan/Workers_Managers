import time

class Workers():
    def __init__(self, name, surname, age, salary, department):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        self.department = department

    @staticmethod
    def workers_num():
        print("Please Enter How Many Workers You Want To Add To The List..")
        time.sleep(2)
        worker_num = int(input("Enter the number of workers:"))

        workers_list = []  # Use a list to store worker objects
        for worker in range(1, worker_num + 1):
            print(f"Worker {worker}:")
            workers_name = input("Enter worker's name:")
            workers_surname = input("Enter worker's surname:")
            workers_age = input("Enter worker's age:")
            workers_salary = input("Enter worker's salary:")
            workers_department = input("Enter worker's department:")

            # Create a worker object and append it to the list
            worker_obj = Workers(workers_name, workers_surname, workers_age, workers_salary, workers_department)
            workers_list.append(worker_obj)

        return workers_list

    def information(self, worker_num):
        print("Working on process...")
        time.sleep(5)
        worker = workers_list[worker_num - 1]  # Adjust index since the list is 0-based
        print(f"""Info about worker {worker_num}...
              Name= {worker.name}
              Surname= {worker.surname}
              Age= {worker.age}
              Salary= {worker.salary}
              Department= {worker.department}""")

class Managers():
    def __init__(self, name, surname, age, salary, department, level):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        self.department = department
        self.level = level

    @staticmethod
    def managers_num():
        print("Please Enter How Many Managers You Want To Add To The List..")
        time.sleep(2)
        manager_num = int(input("Enter the number of managers:"))

        managers_list = []  # Use a list to store manager objects
        for manager in range(1, manager_num + 1):
            print(f"Manager {manager}:")
            managers_name = input("Enter manager's name:")
            managers_surname = input("Enter manager's surname:")
            managers_age = input("Enter manager's age:")
            managers_salary = input("Enter manager's salary:")
            managers_department = input("Enter manager's department:")
            managers_level = input("Enter manager's level:")

            # Create a manager object and append it to the list
            manager_obj = Managers(managers_name, managers_surname, managers_age, managers_salary, managers_department, managers_level)
            managers_list.append(manager_obj)

        return managers_list

    def information(self, manager_num):
        print("Working on process...")
        time.sleep(5)
        manager = managers_list[manager_num - 1]  # Adjust index since the list is 0-based
        print(f"""Info about manager {manager_num}...
              Name= {manager.name}
              Surname= {manager.surname}
              Age= {manager.age}
              Salary= {manager.salary}
              Department= {manager.department}
              Level= {manager.level}""")

# Example usage:
workers_list = Workers.workers_num()
managers_list = Managers.managers_num()

worker_number = int(input("Please write worker number to gain info:"))
workers_list[0].information(worker_number)

manager_number = int(input("Please write manager number to gain info:"))
managers_list[0].information(manager_number)
