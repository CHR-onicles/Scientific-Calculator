def main_window_style():
    return """
    QWidget {
       font: 13pt segoe UI;
    }
    QWidget#mainwindow {
        background-color: #333;
        
    }
    
    QLineEdit#calc-screen {
        border: none;
        font-size: 30pt;
        background-color: transparent;
        color: white;
        font-weight: bold;
        
    }
    """