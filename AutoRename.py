from PyQt4 import QtGui
import os, sys
import ntpath,eyed3

class PrettyWidget(QtGui.QWidget):
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(600, 300, 400, 200)
        self.setWindowTitle('Rename Audio File')     
        
        btn = QtGui.QPushButton('BROWSE', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.MultipleBrowse)
        btn.move(150,100)     


    def MultipleBrowse(self):
        filePaths = QtGui.QFileDialog.getOpenFileNames(self, 
                                                       'Select Audio Files',
                                                       " ",
                                                      '*.mp3')
        for filePath in filePaths:
            head, tail = os.path.split(str(filePath))
            audio_file = eyed3.load(str(filePath))
            new_name = audio_file.tag.title + audio_file.tag.artist

            start=end=0
            while start != -1 and end != -1:
                start = new_name.find('(')
                end = new_name.find(')')
                if start != -1 and end != -1:
                    new_name=new_name[0:start] + new_name[end+1:]
            changed_name = new_name + ".mp3"
            os.rename(os.path.join(head, tail), os.path.join(head, changed_name))
           
        
def main():
    app = QtGui.QApplication(sys.argv)
    w = PrettyWidget()
    w.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
