from santa_mapper import SantaMapper
from workbook_helper import WorkbookHelper
from pandas import DataFrame

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem
import pandas as pd

class SecretSantaApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the user interface
        self.init_ui()

    def init_ui(self):
        # Set up the layout
        self.layout = QVBoxLayout()

        # Create buttons and connect them to functions
        self.btn_open_file = QPushButton("Open Excel File")
        self.btn_open_file.clicked.connect(self.open_file_dialog)

        self.btn_generate = QPushButton("Generate Mappings")
        self.btn_generate.clicked.connect(self.generate_dictionary)

        # Create a table widget to display the dictionary
        self.table_widget = QTableWidget()

        # Add widgets to the layout
        self.layout.addWidget(self.btn_open_file)
        self.layout.addWidget(self.btn_generate)
        self.layout.addWidget(self.table_widget)

        # Set the layout for the main window
        self.setLayout(self.layout)

    def open_file_dialog(self):
        # Open a file dialog to choose an Excel file
        file_dialog = QFileDialog()
        options = file_dialog.options()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx *.xls);;All Files (*)", options=options)

        # Save the selected file path
        if file_path:
            self.file_path = file_path

    def generate_dictionary(self):
        # Check if a file has been selected
        if hasattr(self, 'file_path'):
            # Read data from the Excel file and create a list of tuples
            wh: WorkbookHelper = WorkbookHelper()
            df: DataFrame = wh.readExcel(file_path="Sample.xlsx")
            data: list = list(zip(df['Name'], df['Address']))

            # Initialize SantaMapper and create Santa mappings
            sm: SantaMapper = SantaMapper(names=data)
            data_dict: dict = sm.map_santas()

            # Display the dictionary in the table widget
            self.display_dictionary(data_dict)
        else:
            print("Please select an Excel file first.")

    def display_dictionary(self, data_dict):
        # Clear the table widget
        self.table_widget.clear()

        # Set column headers
        if data_dict:
            column_headers = ["Santa", "Baby", "Address"]
            self.table_widget.setColumnCount(3)
            self.table_widget.setHorizontalHeaderLabels(column_headers)

            # Populate the table with data
            self.table_widget.setRowCount(len(data_dict))
            for row, (key, value) in enumerate(data_dict.items()):
                key_item = QTableWidgetItem(f'{key}')
                value_item = QTableWidgetItem(f'{value[0]}')
                address_item = QTableWidgetItem(f'{value[1]}')

                self.table_widget.setItem(row, 0, key_item)
                self.table_widget.setItem(row, 1, value_item)
                self.table_widget.setItem(row, 2, address_item)
        else:
            print("No data to display.")

if __name__ == '__main__':
    # Start the PyQt application
    app = QApplication(sys.argv)
    window = SecretSantaApp()
    window.setWindowTitle("Secret Santa Mapper")
    window.resize(640, 360)
    window.show()
    sys.exit(app.exec())