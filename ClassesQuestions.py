print("\nQ1a\n")
# Q1a: Create a class which of a country (include continent, climate, language etc in the inputs)


class Country:

    def __init__(self, continent, country_name, climate, language):
        self.continent = continent
        self.country_name = country_name
        self.climate = climate
        self.language = language



# A1a:


print("\nQ1b\n")
# Q1b: Create a subclass of a city which inherits from the country class


class City(Country):

    def __init__(self, continent, country_name, climate, language, city, population_city):
        super().__init__(continent, country_name, climate, language)
        self.city = city
        self.population_city = population_city


city1 = City('Europe', 'Spain', 'Mild', 'Spanish', 'Barcelona', 500000)
# print(city1.continent)


# A1b:


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False

# A2a:
list_of_primes = []
num1 = Number(1)
for num in list_of_numbers:
    list_num = Number(num)
    if list_num.is_prime() == True:
        list_of_primes.append(num)

print(list_num.is_prime())

print("\nQ2b\n")
# Q2b: Now create a list of numbers from list_of_numbers that are divisible
# by both 3 and 4 using the divisible_by_n method above

# A2b:
divisible_by_3_4 = []
for num in list_of_numbers:
    number = Number(num)
    if number.divisible_by_n(3) and number.divisible_by_n(4):
        divisible_by_3_4.append(number.integer)

print(divisible_by_3_4)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)


class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)

    def encourage(self):
        print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


# A3a:


# -------------------------------------------------------------------------------------- #






