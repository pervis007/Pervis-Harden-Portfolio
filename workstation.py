import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class PlannerSchedulerApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Planner and Scheduler")
        self.setGeometry(200, 200, 800, 600)

        self.tab_widget = QtWidgets.QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.planner_tab = QtWidgets.QWidget()
        self.scheduler_tab = QtWidgets.QWidget()
        self.calendar_tab = QtWidgets.QWidget()

        self.tab_widget.addTab(self.planner_tab, "Planner")
        self.tab_widget.addTab(self.scheduler_tab, "Scheduler")
        self.tab_widget.addTab(self.calendar_tab, "Calendar")

        self.setup_planner_tab()
        self.setup_scheduler_tab()
        self.setup_calendar_tab()

        self.setup_menu_bar()

    def setup_planner_tab(self):
        planner_layout = QtWidgets.QVBoxLayout(self.planner_tab)
        planner_label = QtWidgets.QLabel("Planner")
        planner_label.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Bold))

        self.planner_text = QtWidgets.QTextEdit()
        self.planner_text.setFixedHeight(400)
        self.planner_text.setFont(QtGui.QFont("Arial", 12))

        self.add_task_button = QtWidgets.QPushButton("Add Task")
        self.add_task_button.clicked.connect(self.add_task)

        planner_layout.addWidget(planner_label)
        planner_layout.addWidget(self.planner_text)
        planner_layout.addWidget(self.add_task_button, alignment=QtCore.Qt.AlignRight)

    def add_task(self):
        current_text = self.planner_text.toPlainText()
        new_task = QtWidgets.QInputDialog.getText(
            self, "Add Task", "Enter task description:"
        )[0]
        if new_task:
            if current_text:
                current_text += "\n"
            current_text += f"- {new_task}"
            self.planner_text.setPlainText(current_text)

    def setup_scheduler_tab(self):
        scheduler_layout = QtWidgets.QVBoxLayout(self.scheduler_tab)
        scheduler_label = QtWidgets.QLabel("Scheduler")
        scheduler_label.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Bold))

        self.scheduler_list = QtWidgets.QListWidget()
        self.scheduler_list.setFont(QtGui.QFont("Arial", 12))

        scheduler_layout.addWidget(scheduler_label)
        scheduler_layout.addWidget(self.scheduler_list)

    def setup_calendar_tab(self):
        calendar_layout = QtWidgets.QVBoxLayout(self.calendar_tab)
        calendar_label = QtWidgets.QLabel("Calendar")
        calendar_label.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Bold))

        self.calendar_widget = QtWidgets.QCalendarWidget()
        self.calendar_widget.clicked.connect(self.on_date_selected)

        calendar_layout.addWidget(calendar_label)
        calendar_layout.addWidget(self.calendar_widget)

    
    def on_date_selected(self, date):
        day = date.day()
        month = date.month()
        result = month * int(str(day)[::-1])
        todaysDate = date.today()
todaysDay10 = int(str(todaysDate)[9])
todaysDay01 = int(str(todaysDate)[8])
todaysDay11 = str(int(todaysDay10)) + str(int(todaysDay01))

todaysMonth = int(str(todaysDate)[5]) + int(str(todaysDate)[6])




dailyCode = todaysMonth * int(todaysDay11)


gangsta = Tk()

gangsta.title('onePOS Daily Code')
gangsta.iconbitmap()
gangsta.geometry("600x400")


caltech = Calendar(gangsta, selectmode="day", year=2023)
caltech.grid(row=1,column=1,padx=20,pady=30)
caltech.pack(pady=20)


def grab_date():
    da_label.config(text="Daily Code: " + str(dailyCode))

da_button = Button(gangsta, text="Get Today's Code", command=grab_date)
da_button.pack(pady=20)

da_label = Label(gangsta, text='')
da_label.pack(pady=20)

gangsta.mainloop()
message = f"The result of {month} times {day} flipped is: {result}"
QtWidgets.QMessageBox.information(self, "Equation Result", message)
        
        
def setup_menu_bar(self):
        main_menu = self.menuBar()
        mode_menu = main_menu.addMenu("Mode")

        dark_mode_action = QtWidgets.QAction("Dark Mode", self)
        dark_mode_action.triggered.connect(self.set_dark_mode)

        light_mode_action = QtWidgets.QAction("Light Mode", self)
        light_mode_action.triggered.connect(self.set_light_mode)

        system_mode_action = QtWidgets.QAction("System Mode", self)
        system_mode_action.triggered.connect(self.set_system_mode)

        mode_menu.addAction(dark_mode_action)
        mode_menu.addAction(light_mode_action)
        mode_menu.addAction(system_mode_action)
def set_dark_mode(self):
        style_sheet = """
            QMainWindow {background-color: #303030;}
            QLabel {color: white;}
            QTextEdit {background-color: #252525; color: white;}
            QListView {background-color: #252525; color: white;}
        """
        self.setStyleSheet(style_sheet)

    def set_light_mode(self):
        self.setStyleSheet("")

    def set_system_mode(self):
        self.setStyleSheet("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = PlannerSchedulerApp()
    window.show()
    sys.exit(app.exec_())