import argparse
import time
import wave, struct

# Glossary
# Frame - a frame consists of samples - one sample per channel
# Sample width - the width in bytes per sample
# Framerate - the number of frames per second

def decode():
    wav_file = wave.open("out.wav", 'r')

    channels = wav_file.getnchannels()
    print("Channels:", channels)
    sample_width = wav_file.getsampwidth()

    #get sample width (bytes per sample)
    print("Bytes per sample:", sample_width)

    #get frame rate. A frame consists of samples - one sample per channel.
    frame_rate = wav_file.getframerate()
    print("Frame rate:", frame_rate)

    length = wav_file.getnframes()
    print("Number of frames:", length)

    comp_type = wav_file.getcomptype()
    print("Compression type:", comp_type)
    comp_name = wav_file.getcompname()
    print("Compression name:", comp_name)

    result = ""

    message = args.message
    message_len = len(message)

    for i in range(0, message_len):
        frame = wav_file.readframes(1).hex()
        frame_list = list(frame)

        hexy = "0x"
        hexy += frame_list[0]
        hexy += frame_list[4]

        result += chr(int(hexy, 0))

    print("------------------")
    print("--DECODED RESULT--")
    print("------------------")
    print(result)

def reader():
    with open("stegosaurus.cpp") as f:
        while True:
            # read next character
            char = f.read(1)
            # if not EOF, then at least 1 character was read, and 
            # this is not empty
            if char:
                yield char
            else:
                return

def main():
    wav_file = wave.open(args.wav, 'r')

    channels = wav_file.getnchannels()
    print("Channels:", channels)
    sample_width = wav_file.getsampwidth()

    #get sample width (bytes per sample)
    print("Bytes per sample:", sample_width)

    #get frame rate. A frame consists of samples - one sample per channel.
    frame_rate = wav_file.getframerate()
    print("Frame rate:", frame_rate)

    wav_length = wav_file.getnframes()
    print("Number of frames:", wav_length)

    comp_type = wav_file.getcomptype()
    print("Compression type:", comp_type)
    comp_name = wav_file.getcompname()
    print("Compression name:", comp_name)

    output = wave.open('out.wav', 'w')

    output.setparams((channels, sample_width, frame_rate, wav_length, comp_type, comp_name))

    message = args.message
    message_len = len(message)

    # wav_length = 300000 #temporary to shorten process of encoding

    for i in range(0, wav_length):
        frame = wav_file.readframes(1)
        # print(frame)
        frame_list = list(frame.hex())
        # print(frame_list)
        if i < message_len:
            hexy = str(hex(ord(message[i])))

            frame_list[0] = str(hexy[2])
            frame_list[4] = str(hexy[3])

            frame_bytes = bytes.fromhex(''.join(frame_list))
            frame = bytes(frame_bytes)

        output.writeframes(frame)
        print(frame, end='')

    wav_file.close()
    output.close()    

if __name__ == "__main__":

    print("Welcome to Stegosaurus")

    parser = argparse.ArgumentParser(description='Stegosaurus - Encode/Decode secret messages in WAV files')

    parser.add_argument('wav', help='Path to input WAV audio file.')
    parser.add_argument('message', help='Message to be encoded in the given WAV file')
    parser.add_argument('-d', action='store_true', help='Decode input_file')

    args = parser.parse_args()

    if args.d:
        decode()
    else:
        time_before = time.time()
        main()
        time_after = time.time()
        print("Total running time:", time_after - time_before)



