'''Pygame提供了一个命名颜色列表，如果你不想使用[R,G,G]记法，就可以使用这些命名颜色。定义好的
颜色名有600多个，如果想看看到底有哪些颜色，可以在硬盘上搜索一个名为colordict.py的文件，然后在
文本编辑器中打开这个文件。
如果你想使用这些颜色名，必须在程序最前面增加下面这行代码：
from pygame.color import THECOLORS
然后，使用某个命名颜色时，可以这样做（我们的画圆例子中就是这样做的）:
pygame.draw.circle(screen,THECOLORS['red'],[100,100],30,0)
'''