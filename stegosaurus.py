import argparse
import os
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

    frame = wav_file.readframes(4).hex()
    frame_list = list(frame)
    
    hexy = "0x"
    for i in range(0,4):
        hexy += frame_list[0+(i*8)]
        hexy += frame_list[4+(i*8)]

    message_len = int(hexy, 16)

    print("Encoded message length:", message_len)

    result = ""

    message = args.message

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

def encode():
    wav_file = wave.open(args.wav, 'r')
    message = open(args.message, 'r')

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

    message_len = os.stat(args.message).st_size 
    print("Size of message to be encoded:", message_len)

    length_of_message_hex = hex(message_len)

    padded = str.format('0x{:08X}', int(length_of_message_hex, 16))
    padded_list = list(padded)
    
    frame = wav_file.readframes(4)
    frame_list = list(frame.hex())
    frame_list[0] = str(padded[2])
    frame_list[4] = str(padded[3])
    frame_list[8] = str(padded[4])
    frame_list[12] = str(padded[5])
    frame_list[16] = str(padded[6])
    frame_list[20] = str(padded[7])
    frame_list[24] = str(padded[8])
    frame_list[28] = str(padded[9])
    frame_bytes = bytes.fromhex(''.join(frame_list))
    frame = bytes(frame_bytes)
    output.writeframes(frame)

    wav_length = 300000 #temporary to shorten process of encoding

    for i in range(0, wav_length):
        frame = wav_file.readframes(1)
        frame_list = list(frame.hex())
        ch = message.read(1)

        if ch:
            hexy = str(hex(ord(ch)))

            padded = str.format('0x{:02X}', int(hexy, 16))

            frame_list[0] = str(padded[2])
            frame_list[4] = str(padded[3])

            frame_bytes = bytes.fromhex(''.join(frame_list))
            frame = bytes(frame_bytes)

        output.writeframes(frame)

    wav_file.close()
    output.close() 
    message.close()   

if __name__ == "__main__":

    print("Welcome to Stegosaurus")

    parser = argparse.ArgumentParser(description='Stegosaurus - Encode/Decode secret messages in WAV files')

    parser.add_argument('wav', help='Path to input WAV audio file.')
    parser.add_argument('message', help='Path to text file to be encoded in the given WAV file')
    parser.add_argument('-d', action='store_true', help='Decode input_file')

    args = parser.parse_args()

    if args.d:
        decode()
    else:
        time_before = time.time()
        encode()
        time_after = time.time()
        print("Total running time:", time_after - time_before)



