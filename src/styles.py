def main_window_style():
    return """
    QWidget {
       font: 13pt segoe UI;
       color: white;
    }
    QWidget#mainwindow {
        background-color: #515151;
    }
    
    QLineEdit#calc-screen {
        border: 1px solid silver; /* will remove later */
        font-size: 30pt;
        background-color: transparent;
        font-weight: bold;
        padding-bottom: 10px;
        padding-top: 10px;        
    }
    
    QPushButton, QToolButton {
        font-weight: bold;
        min-width:75px;        
        min-height: 70px;
        margin: -5px;
        background-color: #2b2b2b;
    }
    
    QPushButton:hover, QPushButton#num-btn:hover, QToolButton:hover {
        background-color: #505050;
        border: 6px solid silver;  /* have to up the pixels cuz the margin eats into it */
    }
    
    QPushButton#equal-to-btn {
        background-color: #777;
    }
    
    QPushButton#equal-to-btn:hover {
        background-color: #999;
    }
    
    QPushButton#num-btn {
        background-color: #111;
    }
    
    
    """