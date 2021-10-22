

from PyQt6.QtWidgets import *
import sys
#from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('فرم ثبت نام برای آشنایی با QInputDialog')
        self.resize(300, 300)

        layout = QFormLayout()
        self.setLayout(layout)

        #ایجاد یک دگمه و ادیت لاین و افزودن به layout برای دریافت نام
        self.btn = QPushButton('نام کامل')
        self.btn.clicked.connect(self.text)

        self.le = QLineEdit()
        self.le.setAccessibleName('نام شما')
        #افزودن دو ویجت دگمه و ادیت باکس در قالب یک خط جدید به فرم.
        layout.addRow(self.btn, self.le)

        #ایجاد یک دگمه و ادیت لاین و افزودن به layout برای دریافت میزان تحصیلات
        self.btn1 = QPushButton('میزان تحصیلات')
        self.btn1.clicked.connect(self.choice)

        self.le1 = QLineEdit()
        self.le1.setAccessibleName('میزان تحصیلات:')
        layout.addRow(self.btn1, self.le1)

        self.btn2 = QPushButton('انتخاب سن')
        self.btn2.clicked.connect(self.Int)

        self.le2 = QLineEdit()
        self.le2.setAccessibleName('سن شما:')
        layout.addRow(self.btn2, self.le2)

        self.btn3 = QPushButton('انتخاب وزن')
        #self.btn3.clicked.connect(self.double)

        self.le3 = QLineEdit()
        self.le3.setAccessibleName('وزن خود را وارد کنید:')
        layout.addRow(self.btn3, self.le3)

        self.btn4 = QPushButton('ثبت نهایی')
        self.btn4.clicked.connect(self.sabt)

        self.le4 = QLineEdit()
        self.le4.setAccessibleName('نتیجه ثبت:')
        layout.addRow(self.btn4, self.le4)


        #ایجاد دگمه خروج
        x = QPushButton('خروج', self)
        #layout.addWidget(x)
        x.move(10, 290)
        x.clicked.connect(self.exit)

    def text(self):
        #متد getText یک رشته را به عنوان ورودی برای دیالوگ باکس می گیرد. 
        #اولین آرگومان رشته ای عنوان دیالوگ و دومی توضیح برای متن ورودی است.
        text, ok = QInputDialog.getText(self, 'دیالوگ دریافت نام', 'نام خود را بصورت کامل وارد کنید:')
        if ok:
            self.le.setText(str(text))

    def choice(self):
        items = ('بیسواد', 'زیر دیپلم', 'دیپلم', 'لیسانس', 'فوق لیسانس', 'دکترا')

        item, ok = QInputDialog.getItem(self, 'دیالوگ انتخاب آخرین مدرک تحصیلی', 'وضعیت تحصیلی خود را مشخص کنید:', items, 0, False)

        if ok and item:
            self.le1.setText(item)

    def Int(self):
        num, ok = QInputDialog.getInt(self, 'دیالوگ چرخشی عددی برای انتخاب سن', 'سن خود را انتخاب کرده یا بصورت دستی وارد کنید:')
        if ok:
            self.le2.setText(str(num))

    def double(self):
        num, ok = QInputDialog.getDouble(self, 'دیالوگ چرخشی اعشاری برای انتخاب وزن', 'وزن خود را انتخاب کرده یا بصورت دستی وارد کنید:')
        if ok:
            self.le3.setText(int(num))

    def sabt(self):
        info ='نام: ' +self.le.text() +'\n' +'میزان تحصیلات: ' +self.le1.text() +'\n' + 'سن: ' +self.le2.text() + '\n' + 'وزن: ' + self.le3.text()

        text, ok = QInputDialog.getText(self, 'بازبینی و ثبت نهایی', info)
        if ok:
            self.le4.setText('اطلاعات فردی شما با موفقیت ثبت شد.')

    def exit(self):
        exit()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())