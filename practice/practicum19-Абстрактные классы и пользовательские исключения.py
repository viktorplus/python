from datetime import datetime, timedelta
import time

class Door:

    def __init__(self, code, max_attempts=3, lock_time_minutes=15):
        self.__code = code

        self.__max_attempts = max_attempts
        self.__failed_attempt = 0

        self.__lock_time_minutes = timedelta(minutes=lock_time_minutes)
        self.__block_until = None



    def change_code(self, old_code, new_code):
        if self._is_valid_code(old_code):
            self.__code = new_code
            print("Access granted")
            self.__failed_attempt = 0
        else:
            self.__failed_attempt += 1
            print("Access denied, code is not changed")
            print(f"Попытка: {self.__failed_attempt}")

    def unlock(self, code):
        if self._is_valid_code(code):
            print("Access granted")
            self.__failed_attempt = 0
            return True

        print("Access denied")
        self.__failed_attempt += 1
        self.__check_attempts()
        print(f"Попытка: {self.__failed_attempt}")
        return False

    def __reset_attempts(self):
        self.__failed_attempt = 0

    def __check_attempts(self):
        if self.__failed_attempt >= self.__max_attempts:
            self.__block_until = datetime.now() + self.__lock_time_minutes
            print(f"Too many failed attempts,block until: {self.__check_block_time()}")
            print(f"$$$$$$TEST: {self.__block_until}")

    def __check_block_time(self):
        time_diff = self.__block_until - datetime.now()
        print(f"{time_diff}")

        return time_diff

    def _is_valid_code(self, code):
        return self.__code == code



d = Door(123)

d.unlock(123)
d.unlock(122)

d.change_code(122, 15445)
d.change_code(123, 15445)


d.unlock(123)
# d.unlock(15445)
d.unlock(123)
d.unlock(123)
d.unlock(123)
d.unlock(123)

time.sleep(5)
d.unlock(123)


