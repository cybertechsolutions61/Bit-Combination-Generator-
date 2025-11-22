==============================================================
                       Bit Combination Generator
                  PyQt5 GUI Tool with PDF Export
==============================================================

📌 Description:
This is a Python-based GUI tool built with PyQt5 to generate all possible 
bit combinations (2-bit, 3-bit, 4-bit, etc.) or within a user-specified 
range (X → Y). The tool features a modern dark-theme interface, tabbed layout,
file preview, PDF/TXT export, and EXE packaging support.

==============================================================
Features:
--------------------------------------------------------------
- Generate all possible bit combinations (customizable bit length)
- Generate combinations between a user-defined range (X → Y)
- Modern Dark Theme GUI with tabbed interface
- File preview of generated combinations
- Export generated combinations to TXT or PDF
- Speed counter to show generation rate
- Compatible with PyInstaller for EXE creation

==============================================================
Requirements:
--------------------------------------------------------------
Python 3.8+
PyQt5==5.15.9
reportlab==4.1.6
PyQt5-sip==12.12.1
pyinstaller==5.14.1
tqdm==4.66.1
numpy==1.27.5
PyQt5-tools==5.15.9.3
pyperclip==1.9.2
PyYAML==6.0

Install all requirements using:
pip install -r requirements.txt

==============================================================
Installation:
--------------------------------------------------------------
1. Clone the repository:
   git clone https://github.com/USERNAME/REPO-NAME

2. Navigate to the project folder:
   cd REPO-NAME

3. Install requirements:
   pip install -r requirements.txt

4. Run the tool:
   python main.py

==============================================================
How to Use:
--------------------------------------------------------------
1. Select the desired bit length or a range (X → Y)
2. Click "Generate"
3. Preview results in the second tab
4. Export results to TXT or PDF if needed

==============================================================
Project Structure:
--------------------------------------------------------------
Project/
│── main.py
│── ui/
│   └── main_window.ui
│── modules/
│   ├── generator.py
│   └── exporter.py
│── assets/
│   └── icon.png
│── requirements.txt
│── README.txt

==============================================================
License:
--------------------------------------------------------------
MIT License

==============================================================
Contact:
--------------------------------------------------------------
GitHub: https://github.com/cybertechsolutions61/Bit-Combination-Generator
