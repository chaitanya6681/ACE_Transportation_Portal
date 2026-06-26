class Driver:
    def __init__(self,driver_id,name,license_number,contact):
        self.driver_id=driver_id
        self.name=name
        self._license_number=license_number
        self._contact=contact

    @property
    def license_number(self):
        return self._license_number

    @license_number.setter
    def license_number(self,value):
        if len(value)==16:
            self._license_number=value
        else:
            print("Invalid license number")

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self,value):
        if value.isdigit() and len(value)==10:
            self._contact=value
        else:
            print("Invalid contact number")

    @contact.deleter
    def contact(self):
        print("Contact deleted")
        del self._contact

    def display_info(self):
        print("Driver ID:",self.driver_id)
        print("Driver Name:",self.name)
        print("License Number:",self.license_number)
        if hasattr(self,"_contact"):
            print("Contact:",self.contact)
        else:
            print("Contact: Not Available")