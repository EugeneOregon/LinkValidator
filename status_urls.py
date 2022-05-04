import requests
from PyQt5 import QtCore
from requests.exceptions import MissingSchema


class StatusUrl(QtCore.QThread):
    infoStatus = QtCore.pyqtSignal(str)
    monitorStatus = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.status_urls = None
        self.urls = None
        self.resp = None
        self.data = None

    def init_url(self, urls):
        self.urls = urls

    def run(self):
        self.status_urls = []
        for self.url in self.urls:
            try:
                self.resp = requests.get(self.url, verify=True)
                if not self.resp:
                    self.resp = requests.get(self.url, verify=False)

                if self.resp.history:
                    self.status_urls.append({
                        'url': self.url,
                        'status_url': self.resp.history[0].status_code,
                        'count_redirect_url': len(self.resp.history),
                        'redirect_url': self.resp.url,
                        'status_redirect_url': self.resp.status_code,
                    })

                elif not self.resp.history:
                    self.status_urls.append({
                        'url': self.url,
                        'status_url': self.resp.status_code,
                    })

            except MissingSchema:
                self.status_urls.append({
                    'url': self.url,
                    'status_url': 'is not a link',
                })

            except requests.exceptions.TooManyRedirects:
                self.status_urls.append({
                    'url': self.url,
                    'status_url': 301,
                    'count_redirect_url': "many redirects, more than 30",
                    'redirect_url': 'undefined',
                    'status_redirect_url': 'undefined',
                })

            except requests.exceptions.SSLError:
                self.status_urls.append({
                    'url': self.url,
                    'status_url': 'Error validating SSL certificate, possibly internal domain',
                })

        intermediate_list1 = [x['status_url'] for x in self.status_urls if type(x['status_url']) == int]
        intermediate_list2 = [x for x in self.status_urls if len(x) == 5]
        intermediate_list3 = [x['status_redirect_url'] for x in intermediate_list2 if
                              type(x['status_redirect_url']) == int]
        final_list = intermediate_list1 + intermediate_list3

        total = len(self.status_urls)
        success = len([x for x in final_list if 200 <= x < 300])
        redirect = len([x for x in final_list if 300 < x < 400])
        error = len([x for x in final_list if 400 < x < 500])

        self.data = {'total': total, 'success': success, 'redirect': redirect, 'error': error}

        self.monitorStatus.emit(self.data)
        self.infoStatus.emit('ok')
