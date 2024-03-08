from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import random
import pyperclip
class main(qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.showFullScreen
        self.setWindowTitle("مولد كلمات المرور العشوائية")
        self.إظهار=qt.QLabel("كلمة المرور العشوائية")
        self.النتيجة = qt.QLineEdit()
        self.النتيجة.setAccessibleName("كلمة المرور العشوائية هي")
        self.النتيجة.setReadOnly(True)
        self.نسخ = qt.QPushButton("نسخ كلمة المرور العشوائية")
        self.نسخ.setDefault(True)
        self.نسخ.clicked.connect(self.copy)
        self.صغيرة = qt.QCheckBox("حروف صغيرة")        
        self.كبيرة = qt.QCheckBox("حروف كبيرة")
        self.أرقام = qt.QCheckBox("أرقام")        
        self.إظهار1=qt.QLabel("تحديد طول كلمة المرور من 4 الى 1024")
        self.الطول = qt.QSlider()
        self.الطول.setRange(4, 1024)
        self.الطول.setAccessibleName("إختيار طول كلمة المرور")
        self.الطول.setSingleStep(4)
        self.توليد = qt.QPushButton("توليد كلمة المرور العشوائية")
        self.توليد.setDefault(True)
        self.توليد.clicked.connect(self.generate)
        l=qt.QVBoxLayout()        
        l.addWidget(self.إظهار)
        l.addWidget(self.النتيجة)
        l.addWidget(self.نسخ)
        l.addWidget(self.صغيرة)
        l.addWidget(self.كبيرة)
        l.addWidget(self.أرقام)
        l.addWidget(self.إظهار1)
        l.addWidget(self.الطول)
        l.addWidget(self.توليد)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)
    def generate(self):
        #إنشاء قائمة تحتوي على المسموح به لإنشاء كلمة المرور العشوائية
        المسموح = []
        صغيرة = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        كبيرة = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        أرقام = "1 2 3 4 5 6 7 8 9 0"
        if self.صغيرة.isChecked():
            #هنا الدالة extend تستخدم لإضافة عناصر من قائمة أو تسلسل الى نهاية قائمة أخرى في السياق الخاص بهذا الكود, تقوم بإضافة عناصر الحروف الصغيرة الى قائمة المسموح باستخدام قيم السلسلة المنفصلة بمسافات من قائمة صغيرة 
            المسموح.extend(صغيرة.split(" "))
        if self.كبيرة.isChecked():
            المسموح.extend(كبيرة.split(" "))
        if self.أرقام.isChecked():
            المسموح.extend(أرقام.split(" "))
        if not المسموح:
            qt.QMessageBox.warning(self, "عفواً", "يرجى اختيار خيار واحد على الأقل لإنشاء كلمة مرور عشوائية")
            return
        #قمنا باستخدام return حتى يتم إيقاف العملية إذا لم يتم إختيار أي شيء
        توليد_كلمة_المرور = [random.choice(المسموح) for _ in range(0, self.الطول.value())]
        self.النتيجة.setText("".join(توليد_كلمة_المرور))
        self.النتيجة.setFocus()
    def copy(self):
        pyperclip.copy(self.النتيجة.text())
app = qt.QApplication([])
app.setStyle('fusion')              
w = main()
w.show()
app.exec()