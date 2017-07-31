from BaseProfile import BaseProfile


class PakwheelsProfile(BaseProfile):
    def __init__(self, name, email, birthday, city, country):
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
        self.name = name
        self.email = email
        self.birthday = birthday
        self.city = city
        self.country = country

    def print_user_profile(self):
        """
        Prints out all information present in a Pakwheels profile.
        """
        print ('User Name: {name}').format(name=self.name)
        print ('User Email: {email}').format(email=self.email)
        print ('User Birthday: {birthday}').format(birthday=self.birthday)
        print ('User City: {city}').format(city=self.city)
        print ('User Country: {country}').format(country=self.country)
