from datetime import date
class Task:
    def __init__(self, title: str, date: date, description:str):
        self.__title = title
        self.__date = date
        self.__description = description
        self.__id = f"{self.__title}-{self.__date}-{self.__description}"
    
    def __str__(self):
            return f"({self.__title}, {self.__date.isoformat()}, {self.__description}, {self.__id})"
    
    @property #Getter
    def title(self):
         return self.__title
    @title.setter
    def title(self,new_title):
         self.__title = new_title
    
    @property
    def date(self):
         return self.__date
    @date.setter
    def date(self,new_date):
         self.__date = new_date
    
    @property
    def description(self):
         return self.__description
    @description.setter
    def description(self, new_description):
         self.__description = new_description
    
    @property
    def id(self):
         return self.__id
   
    