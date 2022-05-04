import time

import gspread
from PyQt5 import QtCore
from gspread.exceptions import APIError, NoValidUrlKeyFound

from faq_manual import credentials
from status_urls import StatusUrl


class GDoc(QtCore.QThread):
    bugStatus = QtCore.pyqtSignal(str)
    progressStatus = QtCore.pyqtSignal(str)
    validateStatus = QtCore.pyqtSignal(str)
    monitorStatus = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.name = None
        self.urls = None
        self.worksheet = None
        self.open_book = None
        self.get_values_sheet = None

        self.link_thread = StatusUrl()
        self.gdoc_report_thread = GDocReport()
        self.link_thread.infoStatus.connect(self.create_report)
        self.credentials = credentials

        self.gc = gspread.service_account_from_dict(self.credentials)

        self.gdoc_report_thread.progressStatus.connect(self.emit_signal)

    def emit_signal(self):
        self.progressStatus.emit('finish')

    def init_name(self, name):
        self.name = name

    def run(self):
        self.progressStatus.emit('start')
        try:
            self.open_book = self.gc.open_by_url(self.name)
            self.get_values_sheet = self.open_book.get_worksheet(0).col_values(1)
            try:
                rows = len(self.open_book.get_worksheet(0).get()) + 10
                self.worksheet = self.open_book.add_worksheet(title="Status URL", rows=rows, cols="20")

            except APIError:
                sheet_report = self.open_book.worksheet("Status URL")
                self.open_book.del_worksheet(sheet_report)
                rows = len(self.open_book.get_worksheet(0).get()) + 10
                self.worksheet = self.open_book.add_worksheet(title="Status URL", rows=rows, cols="20")

            self.worksheet.update('A1:E1',
                                  [['url', 'status url', 'redirect url', 'count redirect url',
                                    'status redirect url']])

            self.urls = self.get_values_sheet
            self.link_thread.init_url(self.urls)
            self.link_thread.start()

        except NoValidUrlKeyFound:
            self.bugStatus.emit('incorrect link')

        except APIError:
            self.bugStatus.emit('access error')

    def create_report(self, info_status):
        if info_status == 'ok':
            self.monitorStatus.emit(self.link_thread.data)
            self.gdoc_report_thread.init_links(self.link_thread.status_urls)
            self.gdoc_report_thread.init_worksheet(self.worksheet)
            self.gdoc_report_thread.start()

    def stop(self):
        self.gdoc_report_thread.exit()
        self.gdoc_report_thread.wait(2000)
        self.gdoc_report_thread.terminate()
        self.validateStatus.emit('stop')


class GDocReport(QtCore.QThread):
    progressStatus = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.links = None
        self.worksheet = None

    def init_links(self, links):
        self.links = links

    def init_worksheet(self, worksheet):
        self.worksheet = worksheet

    def run(self):
        row = 2
        for link in self.links:
            if len(link) == 5:
                self.worksheet.update(f'A{row}:E{row}', [[link['url'], link['status_url'], link['redirect_url'],
                                                          link['count_redirect_url'], link['status_redirect_url']]])
                time.sleep(1)
            else:
                self.worksheet.update(f'A{row}:E{row}', [[link['url'], link['status_url'], 'undefined', 'undefined',
                                                          'no redirect']])
                time.sleep(1)
            row += 1

        self.progressStatus.emit('done')
