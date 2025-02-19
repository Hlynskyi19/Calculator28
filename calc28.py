import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QMessageBox,
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 250)

        layout = QVBoxLayout()

        self.label1 = QLabel("Введіть перше число:")
        layout.addWidget(self.label1)
        self.num1_input = QLineEdit()
        layout.addWidget(self.num1_input)

        self.label2 = QLabel("Введіть друге число:")
        layout.addWidget(self.label2)
        self.num2_input = QLineEdit()
        layout.addWidget(self.num2_input)

        self.operation_label = QLabel("Оберіть операцію:")
        layout.addWidget(self.operation_label)

        self.operation_box = QComboBox()
        self.operation_box.addItems(["+", "-", "*", "/", "//", "%"])
        layout.addWidget(self.operation_box)

        self.calculate_button = QPushButton("Обчислити")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Результат: ")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            operation = self.operation_box.currentText()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Ділення на нуль!")
                result = num1 / num2
            elif operation == "//":
                if num2 == 0:
                    raise ZeroDivisionError("Ділення на нуль!")
                result = num1 // num2
            elif operation == "%":
                if num2 == 0:
                    raise ZeroDivisionError("Ділення на нуль!")
                result = num1 % num2

            self.result_label.setText(f"Результат: {result}")
        except ValueError:
            QMessageBox.warning(self, "Помилка", "Введіть коректні числа!")
        except ZeroDivisionError as e:
            QMessageBox.warning(self, "Помилка", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
