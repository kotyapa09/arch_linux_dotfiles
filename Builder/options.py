import os
from creators.builder import SystemConfiguration


class UserInterface:
    @staticmethod
    def start():
        UserInterface.welcome_banner()
        install_params = UserInterface.get_params()
        SystemConfiguration.start(*install_params)

    @staticmethod
    def welcome_banner():
        os.system("sh Builder/assets/startup.sh")        

    @staticmethod
    def is_verify_response(text) -> bool:
        if "y" in text.lower():
            return True
        else:
            return False

    @staticmethod
    def get_params():
        option_1 = UserInterface.is_verify_response(input("1) Install Base Packages [Y/n] "))

        option_2 = UserInterface.is_verify_response(input("2) Install Pentest Packages? [Y/n] "))

        option_3 = UserInterface.is_verify_response(input("3) Install Extra Packages [Y/n] "))

        return [option_1, option_2, option_3]
