from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class PushButton(QPushButton):
    BASE_COLOR = '#202020'
    HOVER_COLOR = '#505050'
    PRESS_COLOR = '#707070'

    def __init__(self, parent=None):
        super(PushButton, self).__init__(parent)
        self._animation1 = QVariantAnimation(
            startValue=QColor(self.HOVER_COLOR),
            endValue=QColor(self.BASE_COLOR),
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._animation2 = QVariantAnimation(
            startValue=QColor(self.PRESS_COLOR),
            endValue=QColor(self.HOVER_COLOR),
            valueChanged=self._on_value_changed,
            duration=150,
        )

        self._update_stylesheet(QColor(self.BASE_COLOR))  # passing in default background color
        self.setCursor(Qt.PointingHandCursor)

    def _on_value_changed(self, color):
        self._update_stylesheet(color)

    def _update_stylesheet(self, background):
        self.setStyleSheet(
            f"""
            font-weight: normal;
            min-width:64px;        
            min-height: 70px;
            margin: -5px;
            background-color: {background.name()};
            """
        )

    def enterEvent(self, event, *args, **kwargs):
        self._animation1.setDirection(QAbstractAnimation.Backward)
        self._animation1.start()
        super().enterEvent(event)

    def leaveEvent(self, event, *args, **kwargs):
        self._animation1.setDirection(QAbstractAnimation.Forward)
        self._animation1.start()
        super().leaveEvent(event)
        
    def mousePressEvent(self, event, *args, **kwargs):
        self._animation2.setDirection(QAbstractAnimation.Backward)
        self._animation2.start()
        super(PushButton, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event, *args, **kwargs):
        self._animation2.setDirection(QAbstractAnimation.Forward)
        self._animation2.start()
        super(PushButton, self).mouseReleaseEvent(event)

