#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Fish:
    def swin(self):
        print("The flying fish is soaring!")


class Bird:
    def fly(self):
        print("The flying fish is swimming!")


class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
