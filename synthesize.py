import sys
from midiutil import MIDIFile

from helpers import duration, frequency, is_rest
from wav import Song

def main():


    if len(sys.argv) != 2:
        print("Usage: python synthesize.py filename")
        sys.exit(1)


    s = Song(sys.argv[1])

    while True:


        try:
            line = input()
        except EOFError:
            break

        # Add note or rest to song
        if is_rest(line):
            s.add_rest(1)
        else:
            note, frac = line.split("@")
            s.add_note(frequency(note), duration(frac))

    # Write song to disk
    s.write()

if __name__ == "__main__":
    main()