#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: SPECAN
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import osmosdr
import time
from gnuradio import qtgui

class SPECAN(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "SPECAN")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("SPECAN")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "SPECAN")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 8e6
        self.if_gain_slider = if_gain_slider = 24
        self.centerfreq = centerfreq = 425e6

        ##################################################
        # Blocks
        ##################################################
        self._if_gain_slider_range = Range(0, 40, 8, 24, 200)
        self._if_gain_slider_win = RangeWidget(self._if_gain_slider_range, self.set_if_gain_slider, 'if_gain_slider', "counter_slider", float)
        self.top_grid_layout.addWidget(self._if_gain_slider_win)
        self._centerfreq_range = Range(400e6, 6e9, 100, 425e6, 200)
        self._centerfreq_win = RangeWidget(self._centerfreq_range, self.set_centerfreq, 'centerfreq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._centerfreq_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            8192, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            centerfreq, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/20)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(centerfreq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(if_gain_slider, 0)
        self.osmosdr_source_0.set_bb_gain(50, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(50, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "SPECAN")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(self.centerfreq, self.samp_rate)

    def get_if_gain_slider(self):
        return self.if_gain_slider

    def set_if_gain_slider(self, if_gain_slider):
        self.if_gain_slider = if_gain_slider
        self.osmosdr_source_0.set_if_gain(self.if_gain_slider, 0)

    def get_centerfreq(self):
        return self.centerfreq

    def set_centerfreq(self, centerfreq):
        self.centerfreq = centerfreq
        self.osmosdr_source_0.set_center_freq(self.centerfreq, 0)
        self.qtgui_sink_x_0.set_frequency_range(self.centerfreq, self.samp_rate)



def main(top_block_cls=SPECAN, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
