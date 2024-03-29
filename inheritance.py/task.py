##q3
# class member:
#     def __init__(self,name, age, phone_number,address,salary):
#         self.name=name
#         self.age=age
#         self.phone_number=phone_number
#         self.address=address
#         self.salary=salary

#     name=""
#     age=0
#     phone_number=234567890
#     address=""
#     salary=0.0

#     def print_salary(self):
#         print("salary ", self.salary)

# class employee(member):
#     def __init__(self,name,age,phone_number,address,salary, spec):
#         super().__init__(name,age,phone_number,address,salary)
#         self.specialization=spec
#     specialization=""

# class manager(member):
#     def __init__(self,name,age,phone_number,address,salary, depart):
#         super().__init__(name,age,phone_number,address,salary)
#         self.department=depart
#     department=""


# class test:
#     shivam=manager("shivam",20,1234567890,"hschdshcid",100000,"iot")
#     suruchi=employee("suruchi",20,23456789,"dgduihcwjd",3000,"ds")

#     shivam.print_salary()
#     print(shivam.age)
    


##q2
# class parent:
#     def display(self):
#         print("this is a parent  class")

# class child(parent):
#     def show(self):
#         print("this is a child class")

# class test:
#     a=parent()
#     b=child()
#     a.display()
#     b.display()
#     b.show()

##q1
# class Rectangle:

#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
    
#     length=0
#     breadth=0

#     def area(self):
#         print("area is : ", self.length*self.breadth)


#     def perimeter(self):
#         print("perimeter is :", (self.length+self.breadth))

# class test:
#     a=Rectangle(20,20)
#     a.area()

#     a.perimeter()


##
# class instrument:
#     def __init__(self,name,purpose):
#         self.name=name
#         self.purpose=purpose
        
#     name=""
#     purpose=""
#     def display_info(self):
#         print("name is",self.name," and purpose is ",self.purpose )
        

# class microscope(instrument):
#     def __init__(self, name, purpose,magnification,illumination):
#         super().__init__(name, purpose)
#         self.illumination=illumination
#         self.magnification=magnification
    
#     magnification=""
#     illumination=""
#     def display_info(self):
#         print("magnification is",self.magnification," and illumination is ",self.illumination)
        

# class test:
#     a=instrument("guhb","fyg")
#     b=microscope("uisdhui","dij","jfiojf","fewifjwe")
#     a.display_info()
#     b.display_info()


''' q2 - Create a base class (`Instrument`) with attributes for the name and category of an instrument
- Derive a subclass (`Guitar`) from `Instrument` with additional attributes like the number of strings and guitar type.
- Implement a method (`play()`) in the base class to simulate playing the instrument.'''

# class instrunment:
#     def __init__(self,name,category):
#         self.name=name
#         self.category=category


#     name=""
#     category=""

#     def play(self):
#         print(f"name of guitar is {self.name} and category is {self.category}")


# class guitar(instrunment):
#     def __init__(self,name,category,no_of_string,typr_of_guitar):
#         super().__init__(name,category)
#         self.no_of_string=no_of_string
#         self.type_of_guitar=typr_of_guitar

#     def play(self):
#         print(f"name of guitar is : {self.name} , category is : {self.category} ,no os strings are : {self.no_of_string} and type of guitar is : {self.type_of_guitar} ")


#     no_of_string=0
#     type_of_guitar= ""


# a=instrunment("sdchgv","dtrdyf")
# b=guitar("guyg","hjgg",25,"jhgy")
# a.play()
# b.play()

''' q3 - Create a base class (`Ingredient`) with attributes for the name and category of an ingredient.
- Derive a subclass (`Vegetable`) from `Ingredients` with additional attributes like color and cooking method.
- Further derive a subclass (`RootVegetable`) from `Vegetable` with an extra attribute for nutrient content.
- Implement a method (`display_info()`) in each class to show information about each ingredient.'''

# class ingredient:
#     def __init__(self,name,category):
#         self.name=name
#         self.category=category
        
#     name=""
#     category=""
#     def display_info(self):
#         print(f"name is {self.name} , category is {self.category}")

# class vegetable(ingredient):
#     def __init__(self, name, category,color,cooking_method):
#         super().__init__(name, category)
#         self.color=color
#         self.cooking_method=cooking_method

#     color=""
#     cooking_method=""
#     def display_info(self):
#         super().display_info()
#         print(f"color is {self.color} , cooking method is {self.cooking_method}")
        
    
    

# class root_vegetable(vegetable):
#     nutrient_content=""
#     def __init__(self, name, category, color, cooking_method,nutrient_content):
#         super().__init__(name, category, color, cooking_method)
#         self.nutrient_content = nutrient_content

#     def display_info(self):
#          return super().display_info()
#          print(f"nutrient content is {self.nutrient_content}")



# z=ingredient("raddish","dry")
# a=vegetable("potato","dry","brown","fire_less")
# b=root_vegetable("tomato","wet","red","fire","fibre")
# b.display_info()
    


''' q4 - Establish a base class (`ElectronicDevice`) with attributes for the brand and power consumption of a device.
- Derive two subclasses (`Television` and `Refrigerator`) from `ElectronicDevice`.
- Implement a method (`display_info()`) in each class to print out details.
- Add specific functionalities such as screen size for the television and cooling capacity for the refrigerator.'''

# class electronic_device:
#     def __init__(self,brand,power_consuption):
#         self.brand=brand
#         self.power_consjuption=power_consuption
        
#     brand=""
#     power_consjuption=0

#     def display_info(self):
#         print(f"brand is {self.brand} and power consuption is {self.power_consjuption}")


# class television(electronic_device):
#     def display_info(self):
#         return super().display_info()
    

# class refrigerator(electronic_device):
#     def display_info(self):
#         return super().display_info()
    
# a=refrigerator("lg",1250)
# a.display_info()

''' q5 - Create a base class (`Vehicle`) with attributes for the model and fuel type of a vehicle.
- Derive two subclasses (`Car` and `Bicycle`) from `Vehicle`.
- Further derive a subclass (`ElectricCar`) from `Car` to represent electric cars.
- Implement a method (`display_info()`) in each class to print out details.
- Add specific functionalities such as the number of doors for the car and range per charge for the electric car.
'''

# class vechile:
#     model=""
#     fuel_type=""
#     def __init__(self,model,fuel_type):
#         self.model=model
#         self.fuel_type=fuel_type

#     def display_info(self):
#         print(f"model is {self.model} and fuel type is {self.fuel_type}")
        


# class car(vechile):
#     def display_info(self):
#         return super().display_info()

# class bicycle(vechile):
#     def display_info(self):
#         return super().display_info()

# class electric_car(car):
#     def __init__(self, model, fuel_type, no_of_doors, range):
#         super().__init__(model, fuel_type)
#         self.no_of_doors=no_of_doors
#         self.range=range

#     def display_info(self):
#         print(f"no of doors {self.no_of_doors} and range is {self.range}")
#         return super().display_info()
        
    
# x=electric_car("xyz","CNG",2,55)
# x.display_info()

