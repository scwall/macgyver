from structures.windowsmain import WindowsMain
import sys

if __name__ == '__main__':
    try:
        assert sys.version_info >= (3, 4)
        __import__('imp').find_module('pygame')
        main = WindowsMain()
        main.mainloop()
    except ImportError:
        print("The pygame module is not installed: launch pip install pygame")
    except AssertionError:
        print("Request version 3.4 python or more")
