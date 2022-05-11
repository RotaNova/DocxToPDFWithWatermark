#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import os
from pathlib import Path
import sys
import time

from docx2pdf import convert
import PyPDF4
from PyPDF4 import PdfFileWriter, PdfFileReader
import logging

from PySide6.QtGui import *
from PySide6.QtWidgets import *
import ui_main
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.centralwidget.setLayout(self.ui.layout)
        # self.cwd = Path.cwd()
        self.setWindowTitle("批量PDF转换加水印工具")
        self.show()
        self.workPath = ""
        self.watermarkPath = ""
        self.ui.startConvert.clicked.connect(self.start_convert)
        self.ui.startConvert.setEnabled(False)
        self.ui.pickWorkPath.clicked.connect(self.choose_work_path)
        self.ui.chooseWaterMarkFile.clicked.connect(self.choose_watermark_file)

    def mylog(self, msg):
        logging.info(msg)
        self.ui.results.appendPlainText(msg)
        QApplication.processEvents()

    def logError(self, msg):
        logging.error(msg)
        self.ui.results.appendPlainText(msg)
        QApplication.processEvents()
        app.exit()

    def add_watermark(self, input_pdf, output_pdf, watermark):
        """

        :param input_pdf:
        :param output_pdf:
        :param watermark:
        :return:
            """
        # reads the watermark pdf file through
        # PdfFileReader
        QApplication.processEvents()
        try:
           watermark_instance = PdfFileReader(watermark)
        except Exception as e:
            self.logError(e)
        # fetches the respective page of
        # watermark(1st page)
        if watermark_instance.getNumPages() > 1:
            button = QMessageBox.critical(self, "警告",
                                          "您选取的水印文件好像有问题，请检查水印文件!",
                                          buttons = QMessageBox.Ignore | QMessageBox.NoToAll,
                                          defaultButton=QMessageBox.Ignore)
            if button == QMessageBox.NoToAll:
                self.logError("退出程序！")
        watermark_page = watermark_instance.getPage(0)

        # reads the input pdf file
        pdf_reader = PdfFileReader(input_pdf)

        # It creates a pdf writer object for the
        # output file
        pdf_writer = PdfFileWriter()

        # iterates through the original pdf to
        # merge watermarks
        for page in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page)
            # will overlay the watermark_page on top
            # of the current page.
            page.mergePage(watermark_page)
            # add that newly merged page to the
            # pdf_writer object.
            pdf_writer.addPage(page)

        with open(output_pdf, 'wb') as out:
            # writes to the respective output_pdf provided
            try:
                pdf_writer.write(out)
            except Exception as e:
                self.logError(e)


    def word2pdf(self, word_name, pdf_name=None):
        """

        :param word_name:
        :param pdf_name:
        :return:
        """
        QApplication.processEvents()
        if pdf_name:
            try:
                convert(word_name, pdf_name)
            except Exception as e:
                self.logError(e)
        else:
            try:
                convert(word_name)
            except Exception as e:
                self.logError(e)


    def start_convert(self):
        self.ui.results.clear()
        base_path = Path.cwd()
        target_path = Path(self.workPath)
        pdf_path = base_path.joinpath('PDF')
        pdf_mark_path = base_path.joinpath("PDFMarked")
        if not Path.exists(pdf_path):
            Path.mkdir(pdf_path)
        if not Path.exists(pdf_mark_path):
            Path.mkdir(pdf_mark_path)
        self.ui.startConvert.setEnabled(False)
        self.ui.startConvert.setText('开始处理文件，清耐心等待')
        QApplication.processEvents()

        files = []
        tfiles = Path(target_path).glob("*")
        for file in tfiles:
            files.append(file.name)
        files_num = 0
        for file in files:
            if file.split('.')[-1] != 'doc' and file.split('.')[-1] != 'docx':
                continue
            else:
                files_num += 1
        if files_num > 0:
            self.mylog('开始转换PDF...')
            count = 0
            for file in files:
                file_path = target_path.joinpath(file)
                if file.split('.')[-1] != 'doc' and file.split('.')[-1] != 'docx':
                    continue
                file_name = file.split('.')[0]
                pdf_file_path = pdf_path.joinpath(file_name+'.pdf')
                # print(file_path, pdf_file_path)
                if Path.exists(pdf_file_path):
                    self.mylog("《{}》已存在，如需重新转换请删除PDF目录下的该文件".format(file_name))
                else:
                    self.mylog("正在转换《{}》文件为pdf".format(file_name))
                    count += 1
                    self.word2pdf(word_name=str(file_path), pdf_name=str(pdf_file_path))
                    self.mylog("《{}》转换成功！".format(file_name))
            self.mylog("转换完成！总计处理文件{}个!".format(count))
        else:
            button = QMessageBox.question(self, "提示", "似乎没有需要转换的文件",
                                          QMessageBox.Yes)

        files = []
        tfiles = Path(pdf_path).glob("*")
        for file in tfiles:
            files.append(file.name)
        files_num = 0
        for file in files:
            if file.split('.')[-1] != 'pdf':
                continue
            else:
                files_num += 1
        if files_num > 0:
            self.mylog("开始添加水印...")
            markfile_path = self.watermarkPath
            count = 0
            for file in files:
                if file.split('.')[-1] != 'pdf':
                    continue
                input_path = pdf_path.joinpath(file)
                output_path = pdf_mark_path.joinpath(file)
                if Path.exists(output_path):
                    self.mylog("《{}》已存在，如需重新添加请删除PDFMarked目录下的该文件".format(file))
                else:
                    self.mylog("为《{}》添加水印".format(file))
                    count += 1
                    self.add_watermark(str(input_path), str(output_path), markfile_path)
                    self.mylog("《{}》添加成功！".format(file))
            self.mylog("添加完成！总计处理文件{}个!".format(count))
        else:
            button = QMessageBox.question(self, "提示", "似乎没有需要添加水印的文件",
                                          QMessageBox.Yes)
        self.ui.startConvert.setEnabled(True)
        self.ui.startConvert.setText("继续转换")

    def choose_work_path(self):
        self.workPath = QFileDialog.getExistingDirectory()
        self.ui.workPath.setText(self.workPath)
        logging.info(self.workPath)
        if self.workPath and self.watermarkPath:
            self.ui.startConvert.setEnabled(True)

    def choose_watermark_file(self):
        self.watermarkPath = QFileDialog.getOpenFileName(filter="pdf(*.pdf)")[0]
        self.ui.watermarkFile.setText(self.watermarkPath)
        logging.info(self.watermarkPath)
        if self.workPath and self.watermarkPath:
            self.ui.startConvert.setEnabled(True)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='info.log')
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='error.log')
    app = QApplication([])
    app.setWindowIcon(QIcon("logo.ico"))
    window = MainWindow()
    apply_stylesheet(app, theme='dark_teal.xml')
    sys.exit(app.exec())