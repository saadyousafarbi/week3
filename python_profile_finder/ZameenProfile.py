from BaseProfile import BaseProfile


class ZameenProfile(BaseProfile):

    def __init__(self, name, email, phone_number, address, country):
        """
        Inherits from BaseProfile and adds Zameen specific fields.

        Attributes:
            name (str) : name of the user
            email (str) : email of the user
            phone_number (number) : phone number of user
            address (string) : address of user
            country (string) : country of user

        """
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.country = country

    def print_user_profile(self):
        """
        Prints out all information present in A Zameen profile.
        """
        print ('User Name: {name}').format(name=self.name)
        print ('User Email: {email}').format(email=self.email)
        print ('User Phone Number: {birthday}').format(birthday=self.phone_number)
        print ('User Country: {country}').format(country=self.country)
        print ('User Address: {address}').format(address=self.address)
