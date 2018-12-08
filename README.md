# WaveShare 4.3inch e-paper

### [> Read the Documentation here < ](https://neoctobers.readthedocs.io/en/latest/dev/wave_share_4d3inch_epaper.html)

For [WaveShare 4.3inch e-paper UART module](http://www.waveshare.net/wiki/4.3inch_e-Paper_UART_Module)

![Screen](screen.jpg)

```python
import wave_share_4d3inch_epaper

# init on COM3
ep = wave_share_4d3inch_epaper.EPaper('COM3')

# clear
ep.clear()

# rotation 0
ep.set_rotation(ep.ROTATION_0)

# black
ep.set_color(ep.COLOR_BLACK)

# rect
ep.rect(0, 0, 799, 599)

# text
ep.set_font_size_en(ep.FONT_SIZE_48)
ep.set_font_size_zh(ep.FONT_SIZE_48)
ep.text(20, 50, 'WaveShare 4.3inch e-paper UART module')

# dark gray
ep.set_color(ep.COLOR_DARK_GRAY)

# rect
ep.rect(10, 10, 790, 590)

# text
ep.set_font_size_en(ep.FONT_SIZE_32)
ep.set_font_size_zh(ep.FONT_SIZE_32)
ep.text(20, 150, 'pip3 install -U wave-share-4d3inch-epaper')

# dark gray
ep.set_color(ep.COLOR_GRAY)

# author
ep.text(20, 300, 'Author: neoctober')
ep.text(20, 350, 'Github: https://git.io/wave_share_4.3inch_epaper')

# circle
ep.fill_circle(75, 525, 25)
ep.circle(175, 525, 25)

# tri
ep.fill_tri(275, 500, 250, 550, 300, 550)
ep.tri(375, 500, 350, 550, 400, 550)

# rect
ep.fill_rect(450, 500, 500, 550)
ep.rect(550, 500, 600, 550)

# line
ep.line(700, 300, 700, 550)
ep.line(710, 300, 710, 550)
ep.line(720, 300, 720, 550)

# bmp
ep.bmp(625, 125, 'FNUT.BMP')

# update
ep.update()
```