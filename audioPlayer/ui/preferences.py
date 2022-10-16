from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from tools.preference_handler import PreferenceFileHandler

class PreferencesDialog(QDialog):
    
    def init_main_window(self):
        """
        Creates main window and the two main layouts
        """
        self.setObjectName("Preferences")
        self.resize(551, 140)
        self.setModal(True)
        # Main vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        # 
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

    def __init__(self):
        super().__init__()
        self.init_main_window()
        
        ## Base folder label
        self.baseFolderLabel = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.baseFolderLabel.setFont(font)
        self.baseFolderLabel.setObjectName("baseFolderLabel")
        self.horizontalLayout.addWidget(self.baseFolderLabel)
        ## Line edit
        self.pathToBaseFolder = QtWidgets.QLineEdit(self)
        self.pathToBaseFolder.setFont(font)
        self.pathToBaseFolder.setObjectName("pathToBaseFolder")
        self.horizontalLayout.addWidget(self.pathToBaseFolder)
        self.pathToBaseFolder.setText(PreferenceFileHandler.get_base_directory())
        ## Browse button
        self.browseButton = QtWidgets.QPushButton(self)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        ## Adding to layout
        self.horizontalLayout.addWidget(self.browseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        ## Ok button
        self.savePreferences = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.savePreferences.setFont(font)
        self.savePreferences.setObjectName("savePreferences")
        self.horizontalLayout_2.addWidget(self.savePreferences)
        self.exitPreferences = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exitPreferences.setFont(font)
        self.exitPreferences.setObjectName("exitPreferences")
        self.horizontalLayout_2.addWidget(self.exitPreferences)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(self)
        self.savePreferences.clicked.connect(self.save_base_directory)
        self.exitPreferences.clicked.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.pathToBaseFolder, self.browseButton)
        self.setTabOrder(self.browseButton, self.savePreferences)
        self.setTabOrder(self.savePreferences, self.exitPreferences)

        # Button actions
        self.browseButton.clicked.connect(self.browse_action)

    def retranslateUi(self, Preferences):
        _translate = QtCore.QCoreApplication.translate
        Preferences.setWindowTitle(_translate("Preferences", "Preferences"))
        self.baseFolderLabel.setText(_translate("Preferences", "Base folder:"))
        self.browseButton.setText(_translate("Preferences", "Browse"))
        self.savePreferences.setText(_translate("Preferences", "Ok"))
        self.exitPreferences.setText(_translate("Preferences", "Cancel"))

    def browse_action(self):
        pathName = QtWidgets.QFileDialog.getExistingDirectory(self, QtCore.QDir.rootPath())
        self.pathToBaseFolder.setText(pathName)

    def save_base_directory(self):
        PreferenceFileHandler.set_base_directory(self.pathToBaseFolder.text())
        self.accept()



    