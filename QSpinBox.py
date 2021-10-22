import sys
from PyQt6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('نمونه ساده از QSpinBox')
        hbox = QHBoxLayout()
        self.setLayout(hbox)

        #ایجاد یک اسپین باکس. بصورت پیش فرض روی 0 است و تا 99  بالا می رود
        self.spin = QSpinBox()
        hbox.addWidget(self.spin)

        #تعیین حد پایین 
        self.spin.setMinimum(-100)

        #تعیین حد بالا
        self.spin.setMaximum(100)

        #تعیین حد بالا و پایین با هم. اول حد پایین و دومی حد بالا
        self.spin.setRange(0, 30)

        #مقدار تغییر عدد در هر بار بالا و پایین رفتن
        self.spin.setSingleStep(5)

# تعیین یک اسم برای اسپین باکس
        self.spin.setAccessibleName('my spin box')
        self.spin.setAccessibleDescription('hello this is my test spin box')
        #وقتی مقدار اسپین باکس تغییر کند، تابع change صدا زده می شود
        self.spin.valueChanged.connect(self.change)

        #ایجاد یک lineEdit جهت نمایش مقدار موجود در اسپین باکس
        self.line = QLineEdit('مقدار اسپین باکس =')
        #ادیت باکس را فقط خواندنی می کنیم
        self.line.setReadOnly(True)
        hbox.addWidget(self.line)

        #ایجاد دگمه خروج
        x = QPushButton('خروج', self)
        hbox.addWidget(x)
        x.move(10, 10)
        x.clicked.connect(self.exit)

    def change(self):
        '''
        توسط متد value() مقداری را که در حال حاظر در اسپین باکس نشان داده می شود را استخراج کرده
        و چون عدد است، آن را بصورت رشته درآورده و با یک پیغام جمع کرده و با استفاده از متد
        setText() آنرا در کادر ویرایشی که قبلا درست کردیم نشان می دهیم
        '''
        self.line.setText('مقدار اسپین باکس = ' +str(self.spin.value()))

    def exit(self):
        exit()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())