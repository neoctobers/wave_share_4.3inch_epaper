# -*- coding: utf-8 -*-
"""
a package for:
    [wave_share 4.3inch e-Paper UART Module](http://www.waveshare.net/wiki/4.3inch_e-Paper_UART_Module)

wave_share e-paper module user manual in pdf:
    http://www.waveshare.net/w/upload/9/9c/4.3inch-e-Paper-User-Manual-CN.pdf
"""



import serial


class EPaper(object):
    # color
    COLOR_BLACK = 0x00
    COLOR_DARK_GRAY = 0x01
    COLOR_GRAY = 0x02
    COLOR_WHITE = 0x03

    # font size
    FONT_SIZE_32 = 0x01
    FONT_SIZE_48 = 0x02
    FONT_SIZE_64 = 0x03

    # mem location
    MEM_FLASH = 0x00
    MEM_SD = 0x01

    # rotation
    ROTATION_NORMAL = 0x00
    ROTATION_90 = 0x01
    ROTATION_180 = 0x02
    ROTATION_270 = 0x03

    # commands
    CMD_HANDSHAKE = 0x00

    CMD_GET_BAUD_RATE = 0x02
    CMD_SET_BAUD_RATE = 0x01

    CMD_GET_MEMORY = 0x06
    CMD_SET_MEMORY = 0x07

    CMD_SCREEN_SLEEP = 0x08

    CMD_UPDATE = 0x0A

    CMD_GET_ROTATION = 0x0C
    CMD_SET_ROTATION = 0x0D

    CMD_LOAD_FONT = 0x0E
    CMD_LOAD_PIC = 0x0F

    CMD_GET_COLOR = 0x11
    CMD_SET_COLOR = 0x10

    CMD_GET_FONT_EN = 0x1C
    CMD_SET_FONT_EN = 0x1E

    CMD_GET_FONT_CN = 0x1D
    CMD_SET_FONT_CH = 0x1F

    CMD_DRAW_POINT = 0x20
    CMD_DRAW_LINE = 0x22

    CMD_DRAW_RECT = 0x25
    CMD_FILL_RECT = 0x24

    CMD_DRAW_CIRCLE = 0x26
    CMD_FILL_CIRCLE = 0x27

    CMD_DRAW_TRI = 0x28
    CMD_FILL_TRI = 0x29

    CMD_CLEAR = 0x2E

    CMD_DRAW_STRING = 0x30
    CMD_DRAW_BITMAP = 0x70

    def __init__(self, tty: str):
        self._tty = tty
        self._socket = None
