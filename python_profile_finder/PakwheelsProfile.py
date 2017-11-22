class PakwheelsProfile:
    def __init__(self, first_name, last_name, gender, user_name, email, birthday, city, country):
        """
        User profile information on Pakwheels website.

        Inherits from BaseProfile and adds Pakwheel's specific fields.

         Attributes:
            name (str): Full name of the user
            email(str): Email address of user provided on website
            birthday (date): Birth date of user
            city (str): City of user
            country (str): Country of user

        """
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.user_name = user_name
        self.email = email
        self.birthday = birthday
        self.city = city
        self.country = country

    def print_user_profile(self):
        """
        Prints out all information present in a Pakwheels profile.
        """
        print ('First Name: {first_name}').format(first_name=self.first_name)
        print ('Last Name: {last_name}').format(last_name=self.last_name)
        print ('Gender: {gender}').format(gender=self.gender)
        print ('User Name: {user_name}').format(user_name=self.user_name)
        print ('User Email: {email}').format(email=self.email)
        print ('User Birthday: {birthday}').format(birthday=self.birthday)
        print ('User City: {city}').format(city=self.city)
        print ('User Country: {country}').format(country=self.country)
