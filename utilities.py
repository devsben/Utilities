import os
import time
import requests
import shutil
from pytz import timezone
from datetime import datetime
from hashlib import md5

class utilities:
    def __init__(self):
        self.session = requests.session()

    def get_between(self, data, first, last):
        """
        Returns the string between two other strings.
        """
        return data.split(first)[1].split(last)[1]

    def hash_value(self, data, salt):
        """
        Returns a MD5 hash of the data received.
        """
        return md5(data.encode() + salt).hexdigest()

    def compare_hash(self, data, hashed_value, salt):
        """
        Compares two MD5 hashes, returns True if they're equal.
        """
        return True if md5(data.encode() + salt).hexdigest() == hashed_value else False

    def contains(self, data, string):
        """
        Checks if a string is found within the given data.
        """
        return True if string in data else False

    def is_even(self, data):
        """
        Checks if the given data is an even number.
        """
        if int(data) % 2 == 0:
            return True

    def is_odd(self, data):
        """
        Checks if the given data is an odd number.
        """
        if int(data) % 2 != 0:
            return True

    def format_float(self, data):
        """
        Returns the correct (e-commerce) format for pricing.
        """
        return "{:.2f}".format(data)

    def timestamp_ms(self):
        """
        Returns the current time in milliseconds (MS).
        """
        return int(time.time() * 1000)

    def timestamp(self):
        """
        Returns the current time in seconds.
        """
        return int(time.time())

    def current_time(self, time_zone):
        """
        Returns the current time (HH:MM:SS) given the timezone.
        """
        return datetime.now(timezone(time_zone)).strftime("%H:%M:%S")

    def current_date(self, time_zone):
        """
        Returns the current date (DD/MM/YYYY) given the timezone.
        """
        return datetime.now(timezone(time_zone)).strftime("%d/%m/%Y")

    def verify_recaptcha(self, data):
        """
        Returns the result of a recaptcha request.
        """
        recaptcha_data = {'secret': 'YOUR SECRET KEY', 'response': data}
        response = self.session.get('https://www.google.com/recaptcha/api/siteverify', params=recaptcha_data)
        return response.json()['success']

    def delete_file(self, data):
        """
        Deletes a file if it exists within the current directory.
        """
        if os.path.exists(data):
            os.remove(data)

    def delete_folder(self, data):
        """
        Deletes a folder if it exists within the current directory.
        """
        if os.path.exists(data):
            shutil.rmtree(data)

    def create_file(self, data):
        """
        Creates a file if it doesn't already exist within the current directory.
        """
        if not os.path.exists(data):
            with open(data, 'a'):
                os.utime(data, None)

    def create_folder(self, data):
        """
        Creates a folder if it doesn't already exist within the current directory.
        """
        if not os.path.exists(data):
            os.mkdir(data)

    def backup_file(self, data, backup):
        """
        Creates a backup of a file if it doesn't already exist within the current directory.
        """
        if os.path.exists(data):
            shutil.copyfile(data, backup)

    def rename_file(self, data, value):
        """
        Renames a file if it exists within the current directory.
        """
        if os.path.exists(data):
            os.rename(data, value)
