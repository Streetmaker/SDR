#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Noisejammer
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
from gnuradio import analog
from gnuradio import filter
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

class Noisejammer(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Noisejammer")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Noisejammer")
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

        self.settings = Qt.QSettings("GNU Radio", "Noisejammer")

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
        self.tr_width_slider = tr_width_slider = 200e3
        self.samp_rate = samp_rate = 2e6
        self.cut_freq_slider = cut_freq_slider = 200e3
        self.center_freq_slider = center_freq_slider = 93e6

        ##################################################
        # Blocks
        ##################################################
        self._tr_width_slider_range = Range(50e3, 1e6, 50e3, 200e3, 200)
        self._tr_width_slider_win = RangeWidget(self._tr_width_slider_range, self.set_tr_width_slider, 'tr_width_slider', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tr_width_slider_win)
        self._cut_freq_slider_range = Range(100e3, 1e6, 50e3, 200e3, 200)
        self._cut_freq_slider_win = RangeWidget(self._cut_freq_slider_range, self.set_cut_freq_slider, 'cut_freq_slider', "counter_slider", float)
        self.top_grid_layout.addWidget(self._cut_freq_slider_win)
        self._center_freq_slider_range = Range(88e6, 108e6, 10e3, 93e6, 200)
        self._center_freq_slider_win = RangeWidget(self._center_freq_slider_range, self.set_center_freq_slider, 'center_freq_slider', "counter_slider", float)
        self.top_grid_layout.addWidget(self._center_freq_slider_win)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            center_freq_slider, #fc
            samp_rate, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(center_freq_slider, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(47, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                cut_freq_slider,
                tr_width_slider,
                firdes.WIN_HAMMING,
                6.76))
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_UNIFORM, 50, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Noisejammer")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tr_width_slider(self):
        return self.tr_width_slider

    def set_tr_width_slider(self, tr_width_slider):
        self.tr_width_slider = tr_width_slider
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cut_freq_slider, self.tr_width_slider, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cut_freq_slider, self.tr_width_slider, firdes.WIN_HAMMING, 6.76))
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.center_freq_slider, self.samp_rate)

    def get_cut_freq_slider(self):
        return self.cut_freq_slider

    def set_cut_freq_slider(self, cut_freq_slider):
        self.cut_freq_slider = cut_freq_slider
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cut_freq_slider, self.tr_width_slider, firdes.WIN_HAMMING, 6.76))

    def get_center_freq_slider(self):
        return self.center_freq_slider

    def set_center_freq_slider(self, center_freq_slider):
        self.center_freq_slider = center_freq_slider
        self.osmosdr_sink_0.set_center_freq(self.center_freq_slider, 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.center_freq_slider, self.samp_rate)



def main(top_block_cls=Noisejammer, options=None):

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
