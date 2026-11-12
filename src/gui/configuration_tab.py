from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QListWidget,
    QPushButton,
    QLineEdit,
    QGroupBox
)


class ConfigurationTab(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        main_layout = QHBoxLayout()

        main_layout.addWidget(
            self.build_module_panel()
        )

        main_layout.addWidget(
            self.build_parameter_panel()
        )

        main_layout.addWidget(
            self.build_simulation_panel()
        )

        self.setLayout(main_layout)

    def build_module_panel(self):

        box = QGroupBox("Modules")

        layout = QVBoxLayout()

        self.module_list = QListWidget()

        self.add_button = QPushButton(
            "Add Module"
        )

        self.remove_button = QPushButton(
            "Remove Module"
        )

        layout.addWidget(
            self.module_list
        )

        layout.addWidget(
            self.add_button
        )

        layout.addWidget(
            self.remove_button
        )

        box.setLayout(layout)

        return box

    def build_parameter_panel(self):

        box = QGroupBox(
            "Module Parameters"
        )

        form = QFormLayout()

        self.name_edit = QLineEdit()

        self.z_min_edit = QLineEdit()
        self.z_max_edit = QLineEdit()

        self.ex_edit = QLineEdit()
        self.ey_edit = QLineEdit()
        self.ez_edit = QLineEdit()

        self.bx_edit = QLineEdit()
        self.by_edit = QLineEdit()
        self.bz_edit = QLineEdit()

        form.addRow(
            "Name",
            self.name_edit
        )

        form.addRow(
            "z min",
            self.z_min_edit
        )

        form.addRow(
            "z max",
            self.z_max_edit
        )

        form.addRow(
            "Ex",
            self.ex_edit
        )

        form.addRow(
            "Ey",
            self.ey_edit
        )

        form.addRow(
            "Ez",
            self.ez_edit
        )

        form.addRow(
            "Bx",
            self.bx_edit
        )

        form.addRow(
            "By",
            self.by_edit
        )

        form.addRow(
            "Bz",
            self.bz_edit
        )

        box.setLayout(form)

        return box

    def build_simulation_panel(self):

        box = QGroupBox(
            "Simulation"
        )

        form = QFormLayout()

        self.particles_edit = QLineEdit(
            "100"
        )

        self.q_over_m_edit = QLineEdit(
            "9.578833156e7"
        )

        self.dt_edit = QLineEdit(
            "0.01"
        )

        self.steps_edit = QLineEdit(
            "1000"
        )

        self.run_button = QPushButton(
            "Run Simulation"
        )

        form.addRow(
            "Particles",
            self.particles_edit
        )

        form.addRow(
            "q/m",
            self.q_over_m_edit
        )

        form.addRow(
            "dt",
            self.dt_edit
        )

        form.addRow(
            "Steps",
            self.steps_edit
        )

        form.addRow(
            self.run_button
        )

        box.setLayout(form)

        return box