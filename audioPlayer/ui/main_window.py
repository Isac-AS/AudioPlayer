from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow
from ui.preferences import PreferencesDialog
from tools.preference_handler import PreferenceFileHandler
from tools.directory_handler import DirectoryHandler
from tools.audio_player import AudioPlayer


class MainWindow(QMainWindow):

    def init_buttons(self):
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./ui/images/back-backwards-repeat-arrows-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.backButton.setIcon(icon)
        self.backButton.setObjectName("backButton")
        self.buttonsLayout.addWidget(self.backButton)
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./ui/images/play-pause-control-go-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.playButton.setIcon(icon1)
        self.playButton.setObjectName("playButton")
        self.buttonsLayout.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./ui/images/pause-stop-control-play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.pauseButton.setIcon(icon2)
        self.pauseButton.setObjectName("pauseButton")
        self.buttonsLayout.addWidget(self.pauseButton)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./ui/images/forward-arrows-arrow-front-go.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.nextButton.setIcon(icon3)
        self.nextButton.setObjectName("nextButton")
        self.buttonsLayout.addWidget(self.nextButton)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./ui/images/square-stop-play-pause.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.stopButton.setIcon(icon4)
        self.stopButton.setObjectName("stopButton")
        self.buttonsLayout.addWidget(self.stopButton)

        self.playButton.clicked.connect(self.play)
        self.pauseButton.clicked.connect(self.pause)
        self.stopButton.clicked.connect(self.stop)

    def init_status_bar(self):
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def init_toolbar(self):
        self.toolBar = QtWidgets.QToolBar(self)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)

    def init_actions(self):
        self.actionPreferences = QtWidgets.QAction(self)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./ui/images/gear-setting-settings-wheel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.actionPreferences.setIcon(icon5)
        self.actionPreferences.setObjectName("actionPreferences")
        self.action_Go_Back = QtWidgets.QAction(self)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./ui/images/ic-back_left_arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.action_Go_Back.setIcon(icon6)
        self.action_Go_Back.setObjectName("action_Go_Back")
        self.action_Previous_File = QtWidgets.QAction(self)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./ui/images/back-backwards-repeat-arrows-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.action_Previous_File.setIcon(icon7)
        self.action_Previous_File.setObjectName("action_Previous_File")
        self.action_Play_File = QtWidgets.QAction(self)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./ui/images/play-pause-control-go-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.action_Play_File.setIcon(icon8)
        self.action_Play_File.setObjectName("action_Play_File")
        self.action_Pause_Playback = QtWidgets.QAction(self)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./ui/images/pause-stop-control-play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.action_Pause_Playback.setIcon(icon9)
        self.action_Pause_Playback.setObjectName("action_Pause_Playback")
        self.action_Next_File = QtWidgets.QAction(self)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./ui/images/forward-arrows-arrow-front-go.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.action_Next_File.setIcon(icon10)
        self.action_Next_File.setObjectName("action_Next_File")
        self.action_Stop_playback = QtWidgets.QAction(self)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./ui/images/square-stop-play-pause.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.action_Stop_playback.setIcon(icon11)
        self.action_Stop_playback.setObjectName("action_Stop_playback")
        # Connecting actions
        self.action_Go_Back.triggered.connect(lambda: self.browse(PreferenceFileHandler.get_base_directory()))
        self.action_Play_File.triggered.connect(lambda: self.play())
        self.action_Pause_Playback.triggered.connect(lambda: self.pause())
        self.action_Stop_playback.triggered.connect(lambda: self.stop())
        # Adds actions
        self.menuSettings.addAction(self.actionPreferences)
        self.menuActions.addAction(self.action_Go_Back)
        self.menuActions.addAction(self.action_Previous_File)
        self.menuActions.addAction(self.action_Next_File)
        self.menuActions.addAction(self.action_Play_File)
        self.menuActions.addAction(self.action_Pause_Playback)
        self.menuActions.addAction(self.action_Stop_playback)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.toolBar.addAction(self.actionPreferences)
        self.toolBar.addAction(self.action_Go_Back)

    def init_menu_bar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.setMenuBar(self.menubar)

    def init_main_frame(self):
        self.setObjectName("MainWindow")
        self.resize(1000, 500)
        # Central widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        # Vertical layout that will act as a browser
        self.explorerLayout = QtWidgets.QVBoxLayout()
        self.explorerLayout.setObjectName("explorerLayout")
        self.verticalLayout.addLayout(self.explorerLayout)
        # Horizontal layout for the push buttons
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.init_buttons()
        self.verticalLayout.addLayout(self.buttonsLayout)
        # Set central widget
        self.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AudioPlayer"))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionPreferences.setText(_translate("MainWindow", "&Preferences"))
        self.action_Go_Back.setText(_translate("MainWindow", "&Go Back"))
        self.action_Go_Back.setToolTip(_translate("MainWindow", "Moves to previous directory"))
        self.action_Go_Back.setShortcut(_translate("MainWindow", "Esc"))
        self.action_Previous_File.setText(_translate("MainWindow", "&Previous File"))
        self.action_Previous_File.setToolTip(_translate("MainWindow", "Plays from the start"))
        self.action_Previous_File.setShortcut(_translate("MainWindow", "P"))
        self.action_Play_File.setText(_translate("MainWindow", "&Play File"))
        self.action_Play_File.setToolTip(_translate("MainWindow", "Plays File"))
        self.action_Play_File.setShortcut(_translate("MainWindow", "Space"))
        self.action_Pause_Playback.setText(_translate("MainWindow", "&Pause Playback"))
        self.action_Pause_Playback.setToolTip(_translate("MainWindow", "Pauses playing file"))
        self.action_Pause_Playback.setShortcut(_translate("MainWindow", "<"))
        self.action_Next_File.setText(_translate("MainWindow", "&Next File"))
        self.action_Next_File.setShortcut(_translate("MainWindow", "N"))
        self.action_Stop_playback.setText(_translate("MainWindow", "&Stop playback"))
        self.action_Stop_playback.setToolTip(_translate("MainWindow", "Stops playback"))
        self.action_Stop_playback.setShortcut(_translate("MainWindow", "B"))

    def init_components(self):
        self.init_main_frame()
        self.init_menu_bar()
        self.init_status_bar()
        self.init_toolbar()
        self.init_actions()
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.backButton, self.playButton)
        self.setTabOrder(self.playButton, self.pauseButton)
        self.setTabOrder(self.pauseButton, self.nextButton)
        self.setTabOrder(self.nextButton, self.stopButton)
        self.init_connections()

    def init_connections(self):
        self.actionPreferences.triggered.connect(self.openPreferenceDialog)

    def delete_items_of_layout(self, layout):
     if layout is not None:
         while layout.count():
             item = layout.takeAt(0)
             widget = item.widget()
             if widget is not None:
                widget.setParent(None)
             else:
                self.delete_items_of_layout(item.layout())

    def update_explorer(self):
        self.delete_items_of_layout(self.explorerLayout)

        font = QtGui.QFont()
        font.setPointSize(14)

        # For each entry, create a horizontal layout with label and button
        for index, entry in enumerate(self.directory_handler.list_directory_contents()):
            filename, is_dir = entry

            # Create a horizontal layout
            entry_layout = QtWidgets.QHBoxLayout()
            entry_layout.setObjectName(f"file-layout-{index}")

            # Create the label
            entry_label = QtWidgets.QLabel()
            entry_label.setFont(font)
            entry_label.setObjectName(f"file-label-{index}")
            
            # Create the button
            entry_button = QtWidgets.QPushButton()
            entry_button.setFont(font)
            entry_button.setObjectName(f"file-button-{index}")

            # Depending on the filetype
            if is_dir:
                entry_label.setText(f"\tDirectory - " + filename)
                entry_button.setText(f"Browse")
                directory_path = f"{self.directory_handler.get_current_directory()}/{filename}"
                entry_button.clicked.connect(lambda ch, directory_path=directory_path: self.browse(directory_path))
            else:
                entry_label.setText(f"\tFile - \t" + filename)
                entry_button.setText(f"Select")
                filename_path = f"{self.directory_handler.get_current_directory()}/{filename}"
                entry_button.clicked.connect(lambda ch, filename_path=filename_path: self.select_file(filename_path))

            entry_layout.addWidget(entry_label)
            entry_layout.addWidget(entry_button)
            self.explorerLayout.addLayout(entry_layout)

    def check_for_base_dir(self):
        if PreferenceFileHandler.get_base_directory() is None:
            self.openPreferenceDialog()
        base_dir = PreferenceFileHandler.get_base_directory()
        self.directory_handler.set_base_directory(base_dir)
        self.directory_handler.set_current_directory(base_dir)
        self.update_explorer()

    def __init__(self):
        self.player = AudioPlayer()
        super().__init__()
        self.init_components()
        self.directory_handler = DirectoryHandler()
        self.check_for_base_dir()
    
    def openPreferenceDialog(self):
        dlg = PreferencesDialog()
        dlg.setWindowTitle("Preferences")
        dlg.exec()

    def browse(self, new_directory):
        self.directory_handler.set_current_directory(new_directory)
        self.update_explorer()

    def select_file(self, selected_file):
        self.directory_handler.set_selected_file(selected_file)
        self.player.set_file_path(selected_file)

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
        