from abc import ABC, abstractmethod

# Abstract class
class SmartDevice(ABC):

    @abstractmethod
    def command(self):
        pass


# Different device classes
class Light(SmartDevice):
    def command(self):
        print("Light is turned on.")


class Fan(SmartDevice):
    def command(self):
        print("Fan is turned on.")


class TV(SmartDevice):
    def command(self):
        print("TV is turned on.")


# Polymorphism
devices = [Light(), Fan(), TV()]

for device in devices:
    device.command()