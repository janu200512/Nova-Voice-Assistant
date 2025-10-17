import time
from assistant import is_wake, process_command
from stt import listen
from tts import say

def main():
    print("Starting Nova Voice Assistant — say the wake word (e.g., 'Nova')")
    say("Nova Assistant started. Say Nova to wake me.", block=True)

    try:
        while True:
            print('\nListening for wake word...')
            text = listen(timeout=5, phrase_time_limit=4)
            print('Heard:', text)
            if is_wake(text):
                say('Yes? How can I help you?', block=True)
                cmd = listen(timeout=6, phrase_time_limit=6)
                print('Command:', cmd)
                response = process_command(cmd)
                say(response, block=True)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('Goodbye')

if __name__ == '__main__':
    main()
