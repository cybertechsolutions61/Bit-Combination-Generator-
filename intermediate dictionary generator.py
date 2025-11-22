from PyQt5 import QtWidgets, QtGui, QtCore
from itertools import product
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class BitGeneratorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Bit Combination Generator")
        self.setGeometry(200, 100, 800, 600)

        self.apply_dark_theme()
        self.initUI()

    # ---------------- DARK THEME ----------------
    def apply_dark_theme(self):
        dark_stylesheet = """
        QWidget {
            background-color: #1e1e1e;
            color: #ffffff;
            font-size: 14px;
        }
        QLineEdit, QTextEdit, QComboBox {
            background-color: #2e2e2e;
            border: 1px solid #444;
            padding: 5px;
            color: #fff;
        }
        QPushButton {
            background-color: #007acc;
            color: white;
            border-radius: 5px;
            padding: 6px;
        }
        QPushButton:hover {
            background-color: #005f99;
        }
        QTabWidget::pane {
            border: 1px solid #333;
        }
        QTabBar::tab {
            background-color: #2b2b2b;
            padding: 8px;
        }
        QTabBar::tab:selected {
            background-color: #007acc;
        }
        """
        self.setStyleSheet(dark_stylesheet)

    # ---------------- MAIN UI ----------------
    def initUI(self):
        self.tabs = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tabs)

        # Tabs
        self.tab_generate = QtWidgets.QWidget()
        self.tab_preview = QtWidgets.QWidget()

        self.tabs.addTab(self.tab_generate, "Bit Generator")
        self.tabs.addTab(self.tab_preview, "File Preview")

        self.build_generate_tab()
        self.build_preview_tab()

    # ---------------- TAB 1: BIT GENERATOR ----------------
    def build_generate_tab(self):
        layout = QtWidgets.QVBoxLayout()

        form_layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Select Bit Size:")

        self.bit_selector = QtWidgets.QComboBox()
        self.bit_selector.addItems([str(i) for i in range(1, 33)])
        self.generate_btn = QtWidgets.QPushButton("Generate")
        self.generate_btn.clicked.connect(self.generate_bits)

        form_layout.addWidget(label)
        form_layout.addWidget(self.bit_selector)
        form_layout.addWidget(self.generate_btn)

        self.speed_label = QtWidgets.QLabel("Speed: Waiting...")

        self.output_box = QtWidgets.QTextEdit()
        self.output_box.setReadOnly(True)

        self.save_pdf_btn = QtWidgets.QPushButton("Export as PDF")
        self.save_pdf_btn.clicked.connect(self.export_pdf)

        layout.addLayout(form_layout)
        layout.addWidget(self.speed_label)
        layout.addWidget(self.output_box)
        layout.addWidget(self.save_pdf_btn)

        self.tab_generate.setLayout(layout)

    # ---------------- TAB 2: FILE PREVIEW ----------------
    def build_preview_tab(self):
        layout = QtWidgets.QVBoxLayout()

        self.file_button = QtWidgets.QPushButton("Open File")
        self.file_button.clicked.connect(self.open_file)

        self.file_preview = QtWidgets.QTextEdit()
        self.file_preview.setReadOnly(True)

        layout.addWidget(self.file_button)
        layout.addWidget(self.file_preview)

        self.tab_preview.setLayout(layout)

    # ---------------- GENERATE BIT COMBINATIONS ----------------
    def generate_bits(self):
        self.output_box.clear()
        bit_count = int(self.bit_selector.currentText())

        start = QtCore.QTime.currentTime()

        combos = [''.join(p) for p in product("01", repeat=bit_count)]

        for c in combos:
            self.output_box.append(c)

        end = QtCore.QTime.currentTime()
        elapsed = start.msecsTo(end)

        self.speed_label.setText(f"Speed: Generated {len(combos)} combinations in {elapsed} ms")

    # ---------------- EXPORT AS PDF ----------------
    def export_pdf(self):
        text = self.output_box.toPlainText().strip()
        if not text:
            return

        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        if file_path == "":
            return

        pdf = canvas.Canvas(file_path, pagesize=A4)
        width, height = A4

        pdf.setFont("Helvetica", 11)
        y = height - 50

        for line in text.split("\n"):
            pdf.drawString(50, y, line)
            y -= 15
            if y < 50:
                pdf.showPage()
                pdf.setFont("Helvetica", 11)
                y = height - 50

        pdf.save()

        QtWidgets.QMessageBox.information(self, "Saved", "PDF exported successfully!")

    # ---------------- OPEN FILE PREVIEW ----------------
    def open_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if file_path == "":
            return
        with open(file_path, "r") as file:
            self.file_preview.setText(file.read())


# ---------------- RUN APP ----------------
app = QtWidgets.QApplication([])
window = BitGeneratorApp()
window.show()
app.exec_()
