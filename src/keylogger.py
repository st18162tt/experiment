import os
from pynput.keyboard import Listener
from datetime import datetime as dt
import time

# OSに依存しない形でpathを生成
FILE_NAME = 'keylog(' + dt.now().strftime('%Y-%m-%d %H;%M;%S') + ').csv'
FILE_PATH = os.path.normpath(os.path.join('.' , FILE_NAME))

out = []

def on_press(key):
    now_ut = time.time()
    try:
        char = key.char

        # shift + q
        # 終了する
        if char == 'Q':
            return False

        if char in ['j', 'f', 'k', 'd']:
            out.append(char + ',' + str(now_ut))
    except AttributeError:
        pass

def on_release(key):
    pass

if __name__ == '__main__':
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            print('Recording...')
            listener.join()
    except Exception:
        pass

    with open(FILE_PATH, mode='w') as f:
        f.write('\n'.join(out))
        print('Keylogs have been saved as ' + FILE_NAME)
