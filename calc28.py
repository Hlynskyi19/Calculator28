import sys
import pytest
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox,
)


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 250)

        self.layout = QVBoxLayout()

        self.result_label = QLabel("Результат: ", self)
        self.layout.addWidget(self.result_label)

        self.num1_input = QLineEdit(self)
        self.num1_input.setPlaceholderText("Введіть перше число")
        self.layout.addWidget(self.num1_input)

        self.num2_input = QLineEdit(self)
        self.num2_input.setPlaceholderText("Введіть друге число")
        self.layout.addWidget(self.num2_input)

        self.add_button = QPushButton("+")
        self.add_button.clicked.connect(self.add)
        self.layout.addWidget(self.add_button)

        self.sub_button = QPushButton("-")
        self.sub_button.clicked.connect(self.subtract)
        self.layout.addWidget(self.sub_button)

        self.mul_button = QPushButton("*")
        self.mul_button.clicked.connect(self.multiply)
        self.layout.addWidget(self.mul_button)

        self.div_button = QPushButton("/")
        self.div_button.clicked.connect(self.divide)
        self.layout.addWidget(self.div_button)

        self.int_div_button = QPushButton("//")
        self.int_div_button.clicked.connect(self.integer_divide)
        self.layout.addWidget(self.int_div_button)

        self.mod_button = QPushButton("%")
        self.mod_button.clicked.connect(self.modulo)
        self.layout.addWidget(self.mod_button)

        self.setLayout(self.layout)

    def get_inputs(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            return num1, num2
        except ValueError:
            QMessageBox.warning(self, "Помилка", "Будь ласка, введіть коректні числа")
            return None, None

    def add(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            self.result_label.setText(f"Результат: {num1 + num2}")

    def subtract(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            self.result_label.setText(f"Результат: {num1 - num2}")

    def multiply(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            self.result_label.setText(f"Результат: {num1 * num2}")

    def divide(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                QMessageBox.warning(self, "Помилка", "Ділення на нуль неможливе")
            else:
                self.result_label.setText(f"Результат: {num1 / num2}")

    def integer_divide(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                QMessageBox.warning(
                    self, "Помилка", "Цілочисельне ділення на нуль неможливе"
                )
            else:
                self.result_label.setText(f"Результат: {num1 // num2}")

    def modulo(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                QMessageBox.warning(
                    self, "Помилка", "Остача від ділення на нуль неможлива"
                )
            else:
                self.result_label.setText(f"Результат: {num1 % num2}")


# Тестування функцій
@pytest.mark.parametrize("a, b, expected", [(5, 3, 8), (-2, 4, 2), (0, 0, 0)])
def test_addition(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize("a, b, expected", [(5, 3, 2), (4, 4, 0), (0, 5, -5)])
def test_subtraction(a, b, expected):
    assert a - b == expected


@pytest.mark.parametrize("a, b, expected", [(5, 3, 15), (0, 4, 0), (-2, 2, -4)])
def test_multiplication(a, b, expected):
    assert a * b == expected


@pytest.mark.parametrize("a, b, expected", [(6, 3, 2.0), (5, 2, 2.5), (-10, 2, -5.0)])
def test_division(a, b, expected):
    assert a / b == expected


@pytest.mark.parametrize("a, b, expected", [(6, 3, 2), (5, 2, 2), (-10, 3, -4)])
def test_integer_division(a, b, expected):
    assert a // b == expected


@pytest.mark.parametrize("a, b, expected", [(6, 4, 2), (5, 2, 1), (10, 3, 1)])
def test_modulo(a, b, expected):
    assert a % b == expected


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
