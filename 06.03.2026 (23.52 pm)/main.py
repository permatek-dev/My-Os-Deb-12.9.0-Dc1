import subprocess
from PyQt6.QtWidgets import *

def install_node():
	subprocess.Popen([
		"pkexec",
		"apt",
		"install",
		"-y",
		"nodejs"
	])

app = QApplication([])

window = QWidget()
window.setWindowTitle("Developer Hub")
layout = QVBoxLayout()

btn = QPushButton("Install NodeJs")
btn.clicked.connect(install_node)

layout.addWidget(QPushButton("Install Rust"))
layout.addWidget(QPushButton("Install Python"))
layout.addWidget(QPushButton("Install Docker"))
layout.addWidget(QPushButton("Install VS Code"))
layout.addWidget(QPushButton("Setup Git"))

layout.addWidget(btn)



window.setLayout(layout)
window.resize(400,300)
window.show()

app.exec()


