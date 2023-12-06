```python
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar, QLabel, QFileDialog, QCheckBox, QLineEdit
from PyQt5.QtCore import Qt
import sys

class VRPApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.upload_button = QPushButton('Upload .xlsx file')
        self.upload_button.clicked.connect(self.upload_file)
        layout.addWidget(self.upload_button)

        self.confirmation_message = QLabel('')
        layout.addWidget(self.confirmation_message)

        self.num_techs = QLineEdit('Enter number of techs')
        layout.addWidget(self.num_techs)

        self.num_time_windows = QLineEdit('Enter number of time windows')
        layout.addWidget(self.num_time_windows)

        self.time_windows = QLineEdit('Enter time windows')
        layout.addWidget(self.time_windows)

        self.max_jobs_per_day_per_tech = QLineEdit('Enter max jobs per day per tech')
        layout.addWidget(self.max_jobs_per_day_per_tech)

        self.avg_job_duration = QLineEdit('Enter average job duration')
        layout.addWidget(self.avg_job_duration)

        self.break_time_per_tech = QLineEdit('Enter break time per tech')
        layout.addWidget(self.break_time_per_tech)

        self.days_of_week = [QCheckBox(day) for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
        for checkbox in self.days_of_week:
            layout.addWidget(checkbox)

        self.enter_button = QPushButton('Enter')
        self.enter_button.clicked.connect(self.enter_button_clicked)
        layout.addWidget(self.enter_button)

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def upload_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName()
        if file_path.endswith('.xlsx'):
            self.confirmation_message.setText('File has been uploaded.')
            self.file_path = file_path
        else:
            self.confirmation_message.setText('Invalid file. Please upload a .xlsx file.')

    def enter_button_clicked(self):
        # Call the function to solve the VRP problem
        pass

def main():
    app = QApplication(sys.argv)

    vrp_app = VRPApp()
    vrp_app.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```