# pyuic5 LinkValidator.ui -o LinkValidator.py

import re

import pyperclip as pyperclip
from PyQt5.QtWidgets import QInputDialog

from excel import Excel
from faq_manual import faq
from LinkValidator import *
import webbrowser

from gdoc import GDoc
from manual import Manual

from status_urls import StatusUrl


class GUI(QtWidgets.QMainWindow):
    validateStatus = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LinkValidator()
        self.ui.setupUi(self)

        self.manual_thread = Manual()
        self.link_thread = StatusUrl()
        self.gdoc_thread = GDoc()
        self.excel_thread = Excel()

        self.website = webbrowser
        self.url = None
        self.urls = None
        self.gdoc_name = None
        self.spreadsheet = None
        self.account = None

        self.bool_answer = None
        self.gdoc_bool_answer = None
        self.excel_file_answer = None

        self.ui.manualButton.clicked.connect(self._get_manual)
        self.ui.faqButton.clicked.connect(self._get_faq)
        self.ui.designButton.clicked.connect(self.show_author)
        self.ui.copyButton.clicked.connect(self.copy_google_account)

        self.ui.checkLinkButton.clicked.connect(self.check_link)
        self.ui.gDocsButton.clicked.connect(self.create_report_in_google_docs)
        self.ui.excelButton.clicked.connect(self.create_report_in_excel)
        self.ui.stopValidateButton.clicked.connect(self.stop_validate)

        self.validateStatus.connect(self.show_result)
        self.gdoc_thread.validateStatus.connect(self.show_result)

        self.link_thread.infoStatus.connect(self.show_result)
        self.link_thread.monitorStatus.connect(self.show_monitor)

        self.gdoc_thread.bugStatus.connect(self.bug_report)
        self.gdoc_thread.progressStatus.connect(self.show_result)
        self.gdoc_thread.monitorStatus.connect(self.show_monitor)

        self.excel_thread.errorStatus.connect(self.show_error)
        self.excel_thread.progressStatus.connect(self.show_result)
        self.excel_thread.monitorStatus.connect(self.show_monitor)

    def _get_manual(self):
        self.manual_thread.start()

    def _get_faq(self):
        QtWidgets.QMessageBox.about(self, 'FAQ', faq)

    def show_author(self):
        self.website.open_new('https://github.com/EugeneOregon')

    def copy_google_account(self):
        self.account = pyperclip.copy('mom-s-seo@momsseo.iam.gserviceaccount.com')

    def check_link(self):
        self.url, self.bool_answer = QInputDialog.getMultiLineText(self, 'Check Link', 'Enter link')
        self.urls = re.split(';|, |,| |\n', self.url)
        self.condition_check(self.url)

    def create_report_in_google_docs(self):
        self.gdoc_name, self.gdoc_bool_answer = QInputDialog.getText(self, 'Google doc report',
                                                                     'Add Google account\n'
                                                                     'to document with "can edit" permissions')
        self.condition_check(self.gdoc_name)

    def create_report_in_excel(self):
        self.spreadsheet, self.excel_file_answer = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File')
        self.condition_check(self.spreadsheet)

    def condition_check(self, check):
        data = {'total': 0, 'success': 0, 'redirect': 0, 'error': 0}
        self.show_monitor(data)

        if check == self.url:
            if self.bool_answer and self.bool_answer is not None and len(self.url):
                self.link_thread.init_url(self.urls)
                self.link_thread.start()
                self.lock_buttons(True)

        if check == self.gdoc_name:
            if self.gdoc_bool_answer and self.gdoc_bool_answer is not None and len(self.gdoc_name):
                self.gdoc_thread.init_name(self.gdoc_name)
                self.gdoc_thread.start()
                self.lock_buttons(True)

        if check == self.spreadsheet:
            if self.excel_file_answer and self.excel_file_answer is not None and self.spreadsheet:
                self.excel_thread.init_spreadsheet(self.spreadsheet)
                self.excel_thread.start()
                self.lock_buttons(True)

    def bug_report(self, bug_status):
        if bug_status == 'incorrect link':
            QtWidgets.QMessageBox.warning(self, 'Error', 'Incorrect link')
        elif bug_status == 'access error':
            QtWidgets.QMessageBox.warning(self, 'Error', 'Access error\n'
                                                         'Add Google account\n'
                                                         'to document with "can edit" permissions')

    def stop_validate(self):
        url = self.link_thread.isRunning()
        gdoc = self.gdoc_thread.isRunning()
        excel = self.excel_thread.isRunning()

        if url:
            self.link_thread.exit()
            self.link_thread.wait(2000)
            self.link_thread.terminate()
            self.validateStatus.emit('stop')
        if gdoc:
            self.gdoc_thread.exit()
            self.gdoc_thread.wait(2000)
            self.gdoc_thread.terminate()
            self.validateStatus.emit('stop')

        self.gdoc_thread.stop()

        if excel:
            self.excel_thread.exit()
            self.excel_thread.wait(2000)
            self.excel_thread.terminate()
            self.validateStatus.emit('stop')

    def lock_buttons(self, lock_value):
        buttons = [self.ui.faqButton, self.ui.manualButton, self.ui.checkLinkButton, self.ui.gDocsButton,
                   self.ui.excelButton, self.ui.copyButton]
        stop_button = self.ui.stopValidateButton

        for button in buttons:
            button.setDisabled(lock_value)

        stop_button.setEnabled(lock_value)

    def show_result(self, info_status):
        self.ui.logMonitor.clear()
        if info_status == 'ok':
            links = self.link_thread.status_urls
            for link in links:
                if len(link) == 2:
                    url_value = str(link['url'])
                    status_url_value = str(link['status_url'])

                    self.ui.logMonitor.appendPlainText(f'url: {url_value}'
                                                       f'\n'
                                                       f'status url: {status_url_value}'
                                                       f'\n')
                else:
                    url_value = str(link['url'])
                    status_url_value = str(link['status_url'])
                    count_redirect_url_value = str(link['count_redirect_url'])
                    redirect_url_value = str(link['redirect_url'])
                    status_redirect_url_value = str(link['status_redirect_url'])

                    self.ui.logMonitor.appendPlainText(f'url: {url_value}'
                                                       f'\n'
                                                       f'status url: {status_url_value}'
                                                       f'\n'
                                                       f'count redirect url: {count_redirect_url_value}'
                                                       f'\n'
                                                       f'redirect url: {redirect_url_value}'
                                                       f'\n'
                                                       f'status redirect url: {status_redirect_url_value}'
                                                       f'\n')
            self.lock_buttons(False)

        elif info_status == 'start':
            self.ui.logMonitor.appendPlainText('The report is generated. Wait for the end\n')

        elif info_status == 'finish':
            self.ui.logMonitor.appendPlainText('Report generated\n')
            self.lock_buttons(False)

        elif info_status == 'stop':
            self.ui.logMonitor.appendPlainText('Validation terminated\n')
            self.lock_buttons(False)

    def show_monitor(self, data):
        self.ui.totalEdit.setText(str(data['total']))
        self.ui.successEdit.setText(str(data['success']))
        self.ui.redirectEdit.setText(str(data['redirect']))
        self.ui.errorEdit.setText(str(data['error']))

    def show_error(self, error_status):
        if error_status == 'permission error':
            QtWidgets.QMessageBox.warning(self, 'Error', 'The file is open in another application. Close the file')
