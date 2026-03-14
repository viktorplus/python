
class SecureUSB:
    def __init__(self, data, password):
        self.__data = data
        self.__password = password
        self.__locked = True

    def lock(self):
        self.__locked = True
        print("Флешка заблокирована")

    def unlock(self, password):
        if password == self.__password:
            self.__locked = False
            print("Флешка разблокирована")
            return True
        print("Флешка не разлокирована")
        return False

    # def read(self):
    #     if self.__locked:
    #         raise PermissionError("Доступ запрещен")
    #     return self.__data

    @property
    def data(self):
        if self.__locked:
            raise PermissionError("Доступ запрещен")
        return self.__data

    @data.setter
    def data(self, new_data):
        if self.__locked:
            raise PermissionError("Доступ запрещен")
        self.__data = new_data


usb = SecureUSB("Secret plan", "12345")
# print(usb.read())
# try:
#     usb.unlock("12345")
#     print(usb.read())
#
#     usb.lock()
#     print(usb.read())
#
# except PermissionError as e:
#     print(e)

try:
    usb.unlock("12345")
    print(usb.data)

    usb.data = "New Plan"
    print(usb.data)

    usb.lock()
    print(usb.data)

except PermissionError as e:
    print(e)