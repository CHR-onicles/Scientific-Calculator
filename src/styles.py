def main_window_style():
    return """
    QWidget {
       font: 13pt segoe UI;
    }
    QWidget#mainwindow {
        background-color: #333;
    }
    
    QLineEdit#calc-screen {
        border: 1px solid silver; /* will remove later */
        font-size: 30pt;
        background-color: transparent;
        color: white;
        font-weight: bold;
        padding-bottom: 10px;
        padding-top: 10px;        
    }
    """