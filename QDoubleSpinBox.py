
from PyQt6.QtWidgets import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #استفاده از این متد در این موقعیت تیتر پنجره را تنظیم می کند و متن setWindowTitle را نمی خواند
        self.setAccessibleName('یک نمونه برای doubleSpinBox')
        #تعیین سایز پنجره اصلی. چون layout عمودی است، ارتفاع را بیشتر گرفتم.
        self.resize(460, 500)
        page1 = QVBoxLayout()
        
        self.setLayout(page1)
        self.setWindowTitle('QDoubleSpinBox')

        #ایجاد doubleSpinBox و افزودن به layout
        self.dsb = QDoubleSpinBox()
        page1.addWidget(self.dsb)

        #برچسب محصوص که فقط برای صفحه خوان قابل شناسایی است
        self.dsb.setAccessibleName('وزن میوه مورد نظر خود را انتخاب کنید')

        #تغییر مقدار اعشار. داخل پرانتز عدد صحیح قبول می کند.
        self.dsb.setDecimals(1)

        #تعیین گام حرکت 
        self.dsb.setSingleStep(0.5)

        #با این متد محدوده حالت حلقه پیدا می کند و پس از رسیدن به انتها دوباره از اول شروع می کند
        self.dsb.setWrapping(True)

        #برای این که بصورت پیش فرض داخل اسپین باکس چیزی نشان داده شود. که می تواند یک نوشته هم باشد.
        #self.dsb.setSpecialValueText('50.00')

        #این ویژگی متن جعبه چرخش را بدون هرگونه پیشوند ، پسوند ، یا فضای خالی پیشرو یا عقب نگه می دارد.
        #self.dsb.cleanText()

        #پیشوند به شروع مقدار نمایش داده شده اضافه می شود. 
        self.dsb.setPrefix('وزن خالص')

        #پسوند به انتهای مقدار نمایش داده شده اضافه می شود.
        self.dsb.setSuffix('kg')

        #تعیین حد پایین و بالا. اولی برای حد پایین و دومی برای حد بالا
        #self.dsb.setRange(0.0, 50.0)

        #وقتی مقدار اسپین باکس تغییر کند، توابع change  و clean صدا زده می شوند
        self.dsb.valueChanged.connect(self.change)
        self.dsb.valueChanged.connect(self.clean)


        #ایجاد یک lineEdit برای نمایش کل متن اسپین باکس
        self.l1 = QLineEdit()
        self.l1.setAccessibleName('نمایش کل اسپین باکس')
        self.l1.setReadOnly(True)
        page1.addWidget(self.l1)

        #ایجاد ادیت باکس جهت نمایش مقدار عددی اسپین باکس
        self.l2 = QLineEdit()
        self.l2.setAccessibleName('مقدار عددی اسپین باکس')
        self.l2.setReadOnly(True)
        page1.addWidget(self.l2)


        #ایجاد دگمه خروج
        x = QPushButton('خروج', self)
        #page1.addWidget(x)
        x.move(10, 470)
        x.clicked.connect(self.exit)

        #تابع نمایش کل اسپین باکس
    def change(self):
        # با تابع text() کل متن اسپین باکس بیرون کشیده می شود با پیشوند و پسوند.
        self.l1.setText(self.dsb.text())

        #تابع نمایش مقدار عددی اسپین باکس
    def clean(self):
        #تابع cleanText مقدار عددی اسپین باکس را استخراج می کند. 
        self.l2.setText(str(self.dsb.cleanText()))

    def exit(self):
        exit()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())