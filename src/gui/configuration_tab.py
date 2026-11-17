from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QListWidget,
    QPushButton,
    QLineEdit,
    QGroupBox,
    QMessageBox,
    QTextEdit
)

from config.module_config import ModuleConfig
from config.simulation_config import SimulationConfig
from simulation import engine
from simulation.simulation_builder import SimulationBuilder


class ConfigurationTab(QWidget):

    def __init__(self):
        super().__init__()

        self.modules = []

        self.setup_ui()
        self.setup_connections()

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

        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 2)
        main_layout.setStretch(2, 1)

        self.setLayout(main_layout)

    def setup_connections(self):

        self.add_button.clicked.connect(
            self.add_module
        )

        self.remove_button.clicked.connect(
            self.remove_module
        )

        self.module_list.currentRowChanged.connect(
            self.load_module
        )

        self.run_button.clicked.connect(
            self.run_simulation
        )

        editors = [

            self.name_edit,

            self.z_min_edit,
            self.z_max_edit,

            self.ex_edit,
            self.ey_edit,
            self.ez_edit,

            self.bx_edit,
            self.by_edit,
            self.bz_edit
        ]

        for editor in editors:

            editor.editingFinished.connect(
                self.save_module
            )

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

        container = QWidget()

        layout = QVBoxLayout()

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

        layout.addWidget(box)

        layout.addWidget(
            self.build_help_panel()
        )

        container.setLayout(layout)

        return container

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

    def add_module(self):

        module_number = (
            len(self.modules) + 1
        )

        module = ModuleConfig(

            name=f"Module {module_number}",

            z_min=0.0,
            z_max=1.0,

            Ex="0",
            Ey="0",
            Ez="0",

            Bx="0",
            By="0",
            Bz="0"
        )

        self.modules.append(
            module
        )

        self.module_list.addItem(
            module.name
        )

        self.module_list.setCurrentRow(
            len(self.modules) - 1
        )

    def load_module(self, index):

        if index < 0:
            return

        module = self.modules[index]

        self.name_edit.setText(
            module.name
        )

        self.z_min_edit.setText(
            str(module.z_min)
        )

        self.z_max_edit.setText(
            str(module.z_max)
        )

        self.ex_edit.setText(
            module.Ex
        )

        self.ey_edit.setText(
            module.Ey
        )

        self.ez_edit.setText(
            module.Ez
        )

        self.bx_edit.setText(
            module.Bx
        )

        self.by_edit.setText(
            module.By
        )

        self.bz_edit.setText(
            module.Bz
        )

    def save_module(self):

        index = self.module_list.currentRow()

        if index < 0:
            return

        module = self.modules[index]

        try:

            module.name = (
                self.name_edit.text()
            )

            module.z_min = float(
                self.z_min_edit.text()
            )

            module.z_max = float(
                self.z_max_edit.text()
            )

            module.Ex = self.ex_edit.text()
            module.Ey = self.ey_edit.text()
            module.Ez = self.ez_edit.text()

            module.Bx = self.bx_edit.text()
            module.By = self.by_edit.text()
            module.Bz = self.bz_edit.text()

            self.module_list.item(
                index
            ).setText(
                module.name
            )

        except ValueError:
            pass

    def remove_module(self):

        index = self.module_list.currentRow()

        if index < 0:
            return

        del self.modules[index]

        self.module_list.takeItem(
            index
        )

        if self.modules:

            self.module_list.setCurrentRow(
                0
            )

        else:

            self.clear_editor()

    def clear_editor(self):

        self.name_edit.clear()

        self.z_min_edit.clear()
        self.z_max_edit.clear()

        self.ex_edit.clear()
        self.ey_edit.clear()
        self.ez_edit.clear()

        self.bx_edit.clear()
        self.by_edit.clear()
        self.bz_edit.clear()

    def build_simulation_config(self):

        try:

            self.save_module()

            config = SimulationConfig(

                particles=int(
                    self.particles_edit.text()
                ),

                q_over_m=float(
                    self.q_over_m_edit.text()
                ),

                dt=float(
                    self.dt_edit.text()
                ),

                n_steps=int(
                    self.steps_edit.text()
                ),

                modules=self.modules.copy()
            )

            config.validate()

            print(
                "\nSimulation configuration valid:"
            )

            print(config)

            QMessageBox.information(
                self,
                "Success",
                "SimulationConfig created successfully."
            )

            return config

        except Exception as error:

            QMessageBox.critical(
                self,
                "Configuration Error",
                str(error)
            )

            return None

            
    def run_simulation(self):
        print("1")
        try:

            config = self.build_simulation_config()
            print("2")
            engine = SimulationBuilder.build(
                config
            )
            print("3")
            print()

            print("Engine created")

            print(engine)

            print()

            print("Modules:")

            for module in engine.modules:

                print(module.name)

            print()

            print("Particles:")

            print(
                engine.beam.n_particles
            )

            engine.run(
                n_steps=config.n_steps,
                dt=config.dt
            )
            print("simulation completed successfully.")
            print(engine.history.get_trajectories().shape)
            self.last_history = engine.history
            if hasattr(self, "analysis_tab"):

                self.analysis_tab.set_history(
                    engine.history
                )
            if hasattr(self, "animation_tab"):

                self.animation_tab.set_history(
                    engine.history
                )

        except Exception as error:

            print(error)
    def build_help_panel(self):

        box = QGroupBox(
            "Formula Syntax Guide"
        )

        layout = QVBoxLayout()

        help_text = QTextEdit()

        help_text.setReadOnly(True)

        help_text.setPlainText(
            """
    SUPPORTED VARIABLES
    -----------------------------------------------------------------------------------
    x : X position    y : Y position    z : Z position    t : Simulation time

    SUPPORTED CONSTANTS
    -----------------------------------------------------------------------------------
    pi : 3.141592...        E  : 2.718281...

    SUPPORTED FUNCTIONS
    -----------------------------------------------------------------------------------
    sin()       cos()       tan()
    exp()       sqrt()      abs()
    COMMON OPERATORS
    -----------------------------------------------------------------------------------
    +   Addition        -   Subtraction
    *   Multiplication  /   Division
    **  Power

    EXAMPLES
    -----------------------------------------------------------------------------------

    Uniform field:              100

    Oscillating field:          100*sin(pi*z)

    Time dependent field:       100*cos(t)

    Gaussian profile:           exp(-z**2)

    Radial profile:             sqrt(x**2 + y**2)

    Exponential decay:          E**(-z)

    IMPORTANT
    -----------------------------------------------------------------------------------
    Use ** for powers.

    Correct:
    z**2

    Wrong:
    z^2
    """
        )

        layout.addWidget(
            help_text
        )

        box.setLayout(layout)

        return box