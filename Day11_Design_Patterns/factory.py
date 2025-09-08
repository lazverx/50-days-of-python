from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        return "Rendering a Windows button"


class MacOSButton(Button):
    def render(self):
        return "Rendering a MacOS button"


class ButtonFactory:
    @staticmethod
    def create_button(os_type: str) -> Button:
        if os_type == "windows":
            return WindowsButton()
        elif os_type == "macos":
            return MacOSButton()
        else:
            raise ValueError("Unknown OS type")


if __name__ == "__main__":
    button = ButtonFactory.create_button("macos")
    print(button.render())
