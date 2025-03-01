from project.wizard import Wizard


class DarkWizard(Hero):
    def __str__(self):
        return f"{self.username} of type {DarkWizard.__name__} has level {self.level}"
