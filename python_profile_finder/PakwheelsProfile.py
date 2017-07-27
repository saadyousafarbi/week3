from BaseProfile import BaseProfile


class PakwheelsProfile(BaseProfile):
    def __init__(self, name, email, birthday, city, country):
        """
        Inherits from BaseProfile and adds Pakwheel's specific fields.

         Attributes:
            name: Full name of the user
            email: Email address of user provided on website
            birthday: Birth date of user
            city: City of user
            country: Country of user

        """
        BaseProfile.__init__(self,name, email)
        self.birthday = birthday
        self.city = city
        self.country = country

    def print_user_profile(self):
        """
        Prints out all information present in a Zameen profile.

        """
        print ('User Name: {name}').format(name=self.name)
        print ('User Email: {email}').format(email=self.email)
        print ('User Birthday: {birthday}').format(birthday=self.birthday)
        print ('User City: {city}').format(city=self.city)
        print ('User Country: {country}').format(country=self.country)
