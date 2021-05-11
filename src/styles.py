def main_window_style():
    return """
    QWidget {
       font: 13pt segoe UI;
       color: white;
    }
    QWidget#mainwindow {
        background-color: #333;
    }
    
    QLineEdit#calc-screen {
        border: 1px solid silver; /* will remove later */
        font-size: 30pt;
        background-color: transparent;
        font-weight: bold;
        padding-bottom: 10px;
        padding-top: 10px;        
    }
    
    QPushButton {
        font-weight: bold;
        min-width:75px;        
        min-height: 70px;
        margin: -5px;         
    }
    """