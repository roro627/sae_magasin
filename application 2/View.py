from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from productListWidget import productListWidget

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Choix du Magasin")
        self.showMaximized()
        self.setFixedSize(self.size())  

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        
        splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(splitter)

        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_widget.setLayout(left_layout)
        splitter.addWidget(left_widget)

        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_widget.setLayout(right_layout)
        splitter.addWidget(right_widget)

        splitter.setSizes([int(self.width() * 0.5), int(self.width() * 0.5)])  # Diviser la fenêtre également

        self.label_magasin = QLabel("Sélectionnez un magasin:")
        left_layout.addWidget(self.label_magasin)

        self.combo_magasin = QComboBox()
        left_layout.addWidget(self.combo_magasin)

        self.btn_selectionner = QPushButton("Sélectionner")
        self.btn_selectionner.clicked.connect(self.controller.selectionner_magasin)
        left_layout.addWidget(self.btn_selectionner)

        self.label_adresse = QLabel("")
        left_layout.addWidget(self.label_adresse)

        self.label_image = QLabel()
        left_layout.addWidget(self.label_image)

        self.product_list_widget = productListWidget()
        right_layout.addWidget(self.product_list_widget)

        self.selected_items_label = QLabel("Produits sélectionnés:")
        right_layout.addWidget(self.selected_items_label)
        self.selected_items = QListWidget()
        right_layout.addWidget(self.selected_items)

        self.product_list_widget.itemAdded.connect(self.controller.add_item)
        self.product_list_widget.itemDeleted.connect(self.controller.delete_item)
