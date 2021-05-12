def main_window_style():
    return """
    QWidget {
       font: 13pt segoe UI;
       color: white;
    }
    QWidget#mainwindow {
        background-color: #353535;
    }
    
    QLineEdit#calc-screen {
        border: 1px solid silver; /* will remove later */
        border-radius: 3px;
        font-size: 30pt;
        background-color: transparent;
        font-weight: bold;
        padding-bottom: 10px;
        padding-top: 10px;
        selection-background-color: #666;        
    }
    
    QPushButton {
        font-weight: normal;
        min-width:64px;        
        min-height: 70px;
        margin: -5px;
        background-color: #202020;
    }
        
    QPushButton:hover, QPushButton#num-btn:hover{
        background-color: #505050;
        border: 6px solid silver;  /* have to up the pixels cuz the margin eats into it */
    }
    
    QPushButton#equal-to-btn {
        background-color: #505050;
    }
    
    QPushButton#equal-to-btn:hover {
        background-color: #818181;
    }
    
    QPushButton#num-btn {
        background-color: #111;
    }
    
    """