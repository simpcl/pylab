#!/usr/bin/python3

import sys
from pydub import AudioSegment


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("invalid args")
        sys.exit(-1)

    input_file_name = sys.argv[1]
    start_pos = int(sys.argv[2]) * 1000
    end_pos = int(sys.argv[3]) * 1000
    print(input_file_name, start_pos, end_pos)
    #sys.exit(0)

    sound = AudioSegment.from_mp3(input_file_name)
    sound_slice = sound[start_pos:end_pos]
    output_file_name_slice = input_file_name + "_slice"

    sound_slice.export(output_file_name_slice, format="mp3")
