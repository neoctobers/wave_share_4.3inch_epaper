# -*- coding: utf-8 -*-
"""
a package for:
    [wave_share 4.3inch e-Paper UART Module](http://www.waveshare.net/wiki/4.3inch_e-Paper_UART_Module)

wave_share e-paper module user manual in pdf:
    http://www.waveshare.net/w/upload/9/9c/4.3inch-e-Paper-User-Manual-CN.pdf

Documentation：
    https://neoctobers.readthedocs.io/en/latest/dev/wave_share_4d3inch_epaper.html
"""
import serial
import struct


class EPaper(object):
    # serial
    SERIAL_BAUD_RATE = 115200
    SERIAL_TIMEOUT = 1

    # screen
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # color
    COLOR_BLACK = b'\x00'
    COLOR_DARK_GRAY = b'\x01'
    COLOR_GRAY = b'\x02'
    COLOR_WHITE = b'\x03'

    # font size
    FONT_SIZE_32 = b'\x01'
    FONT_SIZE_48 = b'\x02'
    FONT_SIZE_64 = b'\x03'

    # storage location
    STORAGE_FLASH = b'\x00'
    STORAGE_TF = b'\x01'

    # rotation
    ROTATION_0 = b'\x00'
    ROTATION_90 = b'\x01'
    ROTATION_180 = b'\x02'
    ROTATION_270 = b'\x03'

    # commands
    CMD_HANDSHAKE = b'\x00'

    CMD_GET_BAUD_RATE = b'\x02'
    CMD_SET_BAUD_RATE = b'\x01'

    CMD_GET_STORAGE = b'\x06'
    CMD_SET_STORAGE = b'\x07'

    CMD_CLEAR = b'\x2E'
    CMD_UPDATE = b'\x0A'
    CMD_SLEEP = b'\x08'

    CMD_GET_ROTATION = b'\x0C'
    CMD_SET_ROTATION = b'\x0D'

    CMD_LOAD_FONT = b'\x0E'
    CMD_LOAD_BMP = b'\x0F'

    CMD_GET_COLOR = b'\x11'
    CMD_SET_COLOR = b'\x10'

    CMD_GET_FONT_SIZE_EN = b'\x1C'
    CMD_GET_FONT_SIZE_ZH = b'\x1D'

    CMD_SET_FONT_SIZE_EN = b'\x1E'
    CMD_SET_FONT_SIZE_ZH = b'\x1F'

    CMD_DRAW_POINT = b'\x20'
    CMD_DRAW_LINE = b'\x22'

    CMD_DRAW_RECT = b'\x25'
    CMD_FILL_RECT = b'\x24'

    CMD_DRAW_CIRCLE = b'\x26'
    CMD_FILL_CIRCLE = b'\x27'

    CMD_DRAW_TRI = b'\x28'
    CMD_FILL_TRI = b'\x29'

    CMD_DRAW_STRING = b'\x30'
    CMD_DRAW_BMP = b'\x70'

    def __init__(self,
                 com_port: str,
                 baud_rate: int = SERIAL_BAUD_RATE,
                 timeout: int = SERIAL_TIMEOUT,
                 ):

        self._socket = None
        self._com_port = com_port
        self._baud_rate = baud_rate
        self._timeout = timeout
        self.connect()

    def set_com_port(self, com_port):
        self._com_port = com_port

    def set_baud_rate(self, baud_rate: int = SERIAL_BAUD_RATE):
        self._baud_rate = baud_rate

    def set_timeout(self, timeout: int = SERIAL_TIMEOUT):
        self._timeout = timeout

    def connect(self):
        self._socket = serial.Serial(port=self._com_port,
                                     baudrate=self._baud_rate,
                                     stopbits=serial.STOPBITS_ONE,
                                     bytesize=serial.EIGHTBITS,
                                     timeout=self._timeout)

    def disconnect(self):
        self._socket.close()

    @property
    def width(self):
        return self.SCREEN_WIDTH

    @property
    def height(self):
        return self.SCREEN_HEIGHT

    @staticmethod
    def _build_frame(cmd, args=None):
        header = b'\xA5'
        end = b'\xCC\x33\xC3\x3C'

        if args is None:
            frame = header + struct.pack('>h', 9) + cmd + end
        else:
            frame = header + struct.pack('>h', 9 + len(args)) + cmd + args + end

        parity = 0x00
        for _byte in frame:
            parity ^= _byte

        return frame + bytes([parity])

    def _send(self, cmd, args=None):
        if self._socket is None:
            print('>> NOT connected.')
            return

        frame = self._build_frame(cmd=cmd, args=args)

        self._socket.write(frame)
        self._socket.flushInput()

    def handshake(self):
        self._send(self.CMD_HANDSHAKE)

    def load_font(self):
        """
        Import the font files from TF card to FLASH.
        Font files include GBK32/48/64.FON
        LED will flicker 3 times when starts and ends.
        48MB allocated in FLASH for fonts.
        """
        self._send(self.CMD_LOAD_FONT)

    def load_bmp(self):
        """
        Import the image files from TF card to FLASH.
        LED will flicker 3 times when starts and ends.
        80MB allocated in FLASH for images.
        """
        self._send(self.CMD_LOAD_BMP)

    def clear(self):
        self._send(self.CMD_CLEAR)

    def update(self):
        self._send(self.CMD_UPDATE)

    def sleep(self):
        self._send(self.CMD_SLEEP)

    def set_rotation(self, rotation=ROTATION_0):
        if rotation not in [self.ROTATION_0, self.ROTATION_90, self.ROTATION_180, self.ROTATION_270]:
            print('>> Invalid rotation value.')
            return

        self._send(self.CMD_SET_ROTATION, rotation)

    def set_storage(self, storage=STORAGE_FLASH):
        if storage not in [self.STORAGE_FLASH, self.STORAGE_SD]:
            print('>> Invalid storage value.')
            return

        self._send(self.CMD_SET_STORAGE, storage)

    def set_font_size_en(self, font_size: int = 32):
        if font_size not in [self.FONT_SIZE_32, self.FONT_SIZE_48, self.FONT_SIZE_64]:
            print('>> Invalid font_size value.')
            return

        self._send(self.CMD_SET_FONT_SIZE_EN, font_size)

    def set_font_size_zh(self, font_size):
        if font_size not in [self.FONT_SIZE_32, self.FONT_SIZE_48, self.FONT_SIZE_64]:
            print('>> Invalid font_size value.')
            return

        self._send(self.CMD_SET_FONT_SIZE_ZH, font_size)

    def set_color(self, color):
        if color not in [self.COLOR_BLACK, self.COLOR_DARK_GRAY, self.COLOR_GRAY, self.COLOR_WHITE]:
            print('>> Invalid color value.')
            return

        self._send(self.CMD_SET_COLOR, color)

    def text(self, x0, y0, text):
        args = struct.pack('>hh', x0, y0) + bytearray(text, 'gb2312') + bytes(1)
        self._send(self.CMD_DRAW_STRING, args)

    def line(self, x0, y0, x1, y1):
        args = struct.pack('>hhhh', x0, y0, x1, y1)
        self._send(self.CMD_DRAW_LINE, args)

    def rect(self, x0, y0, x1, y1):
        args = struct.pack('>hhhh', x0, y0, x1, y1)
        self._send(self.CMD_DRAW_RECT, args)

    def fill_rect(self, x0, y0, x1, y1):
        args = struct.pack('>hhhh', x0, y0, x1, y1)
        self._send(self.CMD_FILL_RECT, args)

    def circle(self, x0, y0, r):
        args = struct.pack('>hhh', x0, y0, r)
        self._send(self.CMD_DRAW_CIRCLE, args)

    def fill_circle(self, x0, y0, r):
        args = struct.pack('>hhh', x0, y0, r)
        self._send(self.CMD_FILL_CIRCLE, args)

    def tri(self, x0, y0, x1, y1, x2, y2):
        args = struct.pack('>hhhhhh', x0, y0, x1, y1, x2, y2)
        self._send(self.CMD_DRAW_TRI, args)

    def fill_tri(self, x0, y0, x1, y1, x2, y2):
        args = struct.pack('>hhhhhh', x0, y0, x1, y1, x2, y2)
        self._send(self.CMD_FILL_TRI, args)

    def bmp(self, x0, y0, filename):
        cmdParm = struct.pack('>hh', x0, y0) + bytearray(filename.upper(), 'ascii') + bytes(1)
        self._send(self.CMD_DRAW_BMP, cmdParm)
