#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        assert isinstance(name, str) and 0 < len(name) <= 25, "Name must be a string between 1 and 25 characters."
        self.name = name.title()

        assert isinstance(job, str), "Job must be a string."
        assert job in Person.APPROVED_JOBS, "Job must be in the list of approved jobs."
        self.job = job

    def talk(self):
        print("Hello, World!")

    def walk(self):
        print("The person is walking.")