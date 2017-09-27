from structures.require import require

require('pygame', 'pytest')
from structures.windowsmain import WindowsMain

if __name__ == '__main__':
    main = WindowsMain()
    main.main_loop()
