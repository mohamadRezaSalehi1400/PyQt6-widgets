
from PyQt6.QtWidgets import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #افزودن عنوان به پنجره اصلی
        self.setWindowTitle('نمونه برای QLineEdit')

        #ایجاد یک صفحه چینشگر که ویجت ها را بصورت عمودی زیر هم قرار می دهد
        #اگر از چینشگر استفاده نشود با تب به ادیت باکس ها دسترسی نداریم
        self.vbox = QVBoxLayout()
        #layout یا چینشگر را به صفحه اصلی اضافه می کنیم
        self.setLayout(self.vbox)

        #ایجاد اولین QLineEdit. رشته ای را که به این متد می دهیم، به عنوان
        #متن پیش فرض ظاهر می شود که می تواند تا حدی به تشخیص ادیت باکس به ما کمک کند
        self.line1 = QLineEdit('متن اول را وارد کنید', self)
        #ایجاد کادر ویرایش دوم
        self.line2 = QLineEdit('متن دوم را وارد کنید')

        #افزودن دو کادر ویرایش به صفحه چینشگر
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.line2)

        #ایجاد و افزودن دگمه ای بنام {افزودن} به چینشگر QVBoxLayout و اتصال به تابع display
        btn = QPushButton('افزودن')
        self.vbox.addWidget(btn)
        btn.clicked.connect(self.display)

        # ساخت یک QLineEdit برای نمایش نتیجه
        self.line3 = QLineEdit()
        #محل قرار گیری ادیت باکس را تغییر می دهد
        #self.line3.move(50, 50)
        #تغییر اندازه کادر ویرایش
        #self.line3.resize(200, 50)
        # برای تغییر محل و سایز. به ترتیب x و yمحل قرارگیری و طول و عرض ویجت
        #self.line3.setGeometry(100, 100, 200, 50)
        #self.line3.setMaximumSize(60, 200)
        #self.line3.setMaximumWidth(300)
        #تعیین حد اکثر طول کادر ویرایش
        #self.line3.setMaxLength(350)
        #تنظیم ارتفاع نمایشگر
        self.line3.setFixedHeight(35)
        # تنظیم برای راست چین شدن. اما error می دهد
        #self.line3.setAlignment(Qt.AlignRight)
        # برای تثبیت خروجی، ادیت باکس را تنها خواندنی می کنیم
        self.line3.setReadOnly(True)
        #افزودن به چینشگر
        self.vbox.addWidget(self.line3)

        #ایجاد، تعیین کاربری و افزودن دگمه ای برای پاک کردن نتیجه
        btnClear =QPushButton('پاک کردن')
        self.vbox.addWidget(btnClear)
        btnClear.clicked.connect(self.clear)

        #ایجاد دگمه خروج
        x = QPushButton('خروج', self)
        self.vbox.addWidget(x)
        x.clicked.connect(self.exit)

    #تابع نمایش نتیجه
    def display(self):
        #با استفاده از متد text() متن کادر های اول و دوم را بصورت رشته دریافت می کنیم و سپس با هم جمع می کنیم
        # سپس با تابع setText متن را وارد کادر سوم می کنیم.
        self.line3.setText(self.line1.text() +' ' +self.line2.text())

    #تابع پاک کردن کادر ویرایش سوم
    def clear(self):
        self.line3.setText('')

    #تابع خروج
    def exit(self):
        exit()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())