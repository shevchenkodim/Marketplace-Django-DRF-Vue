import random


class GenerateOtpCode(object):
    """ class for generation otp code """

    @staticmethod
    def get_random():
        return random.randint(1000, 9999)
