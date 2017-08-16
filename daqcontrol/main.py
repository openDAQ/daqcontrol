#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import glob

import serial
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import matplotlib
from opendaq import DAQ
from opendaq.models import DAQModel

import daq_control
import config


def list_serial_ports():
    #  Serial port names
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class MyApp(QtGui.QMainWindow, daq_control.Ui_mainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.Y = []
        self.X = []
        self.names = ['AGND', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'VREF']
        self.cfg = QtCore.QSettings('opendaq')
        port_opendaq = str(self.cfg.value('port').toString())
        try:
            self.daq = DAQ(port_opendaq)
        except:
            port_opendaq = ''
        self.tabWidget.setEnabled(False if port_opendaq == '' else True)
        if port_opendaq:
            self.GetcbValues()
        self.toolBar.actionTriggered.connect(self.GetPort)
        self.Bstart_capture.clicked.connect(self.start_capture)
        self.Bstop_capture.clicked.connect(self.stop_capture)
        self.Bstart_counter.clicked.connect(self.start_counter)
        self.Bstop_counter.clicked.connect(self.stop_counter)
        self.Bstop_pwm.clicked.connect(self.stop_pwm)
        self.Breset_pwm.clicked.connect(self.reset_pwm)
        self.Bset_pwm.clicked.connect(self.set_pwm)
        self.Bstart_encoder.clicked.connect(self.start_encoder)
        self.Bstop_encoder.clicked.connect(self.stop_encoder)
        self.Bupdate.clicked.connect(self.Digital_ports)
        self.Bset_voltage.clicked.connect(self.set_DAC)
        self.Bplay.clicked.connect(self.play)
        self.mode_encoder.currentIndexChanged.connect(self.status_resolution)
        try:
            self.statusBar.showMessage("Hardware Version: %s   Firmware Version: %s" % (self.daq.hw_ver[1], self.daq.fw_ver))
        except:
            pass

    def set_DAC(self):
        self.daq.set_analog(self.dac_value.value())

    def play(self):
        self.plotWidget.canvas.ax.cla()
        self.plotWidget.canvas.ax.grid(True)
        self.plotWidget.canvas.xtitle = "Time (s)"
        self.plotWidget.canvas.ytitle = "Voltage (V)"
        self.X = []
        self.Y = []
        self.update()

    def update(self):
        ninput = self.names.index(self.neg_channel.currentText())
        if ninput > 8:
            ninput = 25
        pinput = self.names.index(self.pos_channel.currentText())
        if pinput > 8:
            pinput = 25
        period = self.sb_period.value()
        self.daq.conf_adc(pinput, ninput, self.range.currentIndex())
        self.daq.read_adc()
        value = self.daq.read_analog()
        self.Y.append(value)
        self.X.append(period * len(self.X))
        self.last_value.setText(str(value))
        self.plotWidget.canvas.ax.plot(self.X, self.Y, color='#4d94ff', linewidth=0.7)
        self.plotWidget.canvas.draw()

        if self.Bplay.isChecked():
            timer = QtCore.QTimer()
            timer.timeout.connect(self.update)
            timer.start(period)
            QtCore.QTimer.singleShot(period * 1000, self.update)

    def GetcbValues(self):
        model = DAQModel.new(*self.daq.get_info())
        for ninput in model.adc.ninputs:
            if ninput < 9:
                self.neg_channel.addItem(self.names[ninput])
            else:
                self.neg_channel.addItem(self.names[9])
        for pinput in model.adc.pinputs:
            if pinput < 9:
                self.pos_channel.addItem(self.names[pinput])
            else:
                self.pos_channel.addItem(self.names[9])
        for gain in model.adc.pga_gains:
            self.range.addItem(str(gain))
        self.dac_value.setMinimum(model.dac.vmin)
        self.dac_value.setMaximum(model.dac.vmax)

    def GetPort(self):
        dlg = Configuration(self)
        if dlg.exec_() != '':
            port_opendaq = dlg.ReturnPort()
        self.cfg.setValue('port', port_opendaq)
        self.daq = DAQ(str(port_opendaq))
        self.tabWidget.setEnabled(False if port_opendaq == '' else True)
        self.statusBar.showMessage("Hardware Version: %s   Firmware Version: %s" % (self.daq.hw_ver[1], self.daq.fw_ver))
        self.GetcbValues()

    def start_counter(self):
        self.daq.init_counter(0)

    def stop_counter(self):
        self.daq.stop_capture()
        self.counter_result.setText(str(self.daq.get_counter(0)))

    def start_capture(self):
        self.daq.init_capture(self.reference_period.value())

    def stop_capture(self):
        self.daq.stop_capture()
        modo = self.cbTime.currentIndex()
        self.lEPeriod.setText(str(self.daq.get_capture(modo)[1]))

    def stop_pwm(self):
        self.daq.stop_capture()
        self.daq.stop_pwm()

    def set_pwm(self):
        self.period = self.periodPWM.value()
        self.duty = self.dutyPWM.value() * 1023 / 100
        self.daq.init_pwm(self.duty, self.period)

    def reset_pwm(self):
        self.stop_pwm()
        self.set_pwm()

    def status_resolution(self):
        self.resolution_encoder.setEnabled(False if self.mode_encoder.currentIndex() else True)

    def start_encoder(self):     
        self.daq.init_encoder(self.resolution_encoder.value())

    def stop_encoder(self):
        self.daq.stop_encoder()
        self.result_encoder.setText(str(self.daq.get_encoder()))

    def Digital_ports(self):
        ports_mode = [self.cbD1, self.cbD2, self.cbD3, self.cbD4, self.cbD5, self.cbD6]
        slider_out = [self.SDO1, self.SDO2, self.SDO3, self.SDO4, self.SDO5, self.SDO6]
        display_out = [self.DDI1, self.DDI2, self.DDI3, self.DDI4, self.DDI5, self.DDI6]

        for i in range(6):
            self.daq.set_pio_dir((i+1), ports_mode[i].currentIndex())
            if ports_mode[i].currentIndex():
                self.daq.set_pio((i+1), slider_out[i].value())

            else:
                value = 1 if self.daq.read_pio(i+1) else 0
                palette = display_out[i].palette()
                palette.setColor(QPalette.WindowText, QtCore.Qt.green if value else QtCore.Qt.red)
                display_out[i].setPalette(palette)
                display_out[i].display(value)


class Configuration(QtGui.QDialog, config.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Configuration, self).__init__(parent)
        self.setupUi(self)
        for portO in list_serial_ports():
            self.cbport.addItem(portO)
        self.connectButton.clicked.connect(self.ReturnPort)

    def ReturnPort(self):
        port = self.cbport.currentText()
        self.close()
        return port


def main():
    app = QtGui.QApplication(sys.argv)
    dlg = MyApp()
    dlg.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()