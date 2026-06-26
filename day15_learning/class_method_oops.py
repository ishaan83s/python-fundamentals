class Person:
    name = "Coco"

    # def changeName(self,name):
    #     self.name = name
        # Person.name = name 
        #self.__class__.name = name
        #TWO METHODS TO CHANGE THE DEFAULT NAME OF PERSON.

    @classmethod  #SO THIS METHOD ALLOWS US TO CHANGE THE VALUE INSIDE OF THE CLASS ITSELF
    def changeName(cls,name): #HERE THE CLS IS BASICALLY POINTING TO CLASS(PERSON)
        cls.name = name

person1 = Person()
person1.changeName("YNW MELLY")
print(person1.name)
print(Person.name)