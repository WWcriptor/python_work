from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.__name = name
        self.__emp_id = emp_id

    def getName(self):
        return self.__name

    def getEmp_id(self):
        return self.__emp_id

    def show_info(self):
        print(f"[{self.__emp_id}] {self.__name}")

    @abstractmethod
    def calculate_saraly(self):
        pass

    