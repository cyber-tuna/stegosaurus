import wave, struct


def main():
    wav_file = wave.open("out.wav", 'r')

    sample_width = wav_file.getsampwidth()
    print "sample width:", sample_width
    frame_rate = wav_file.getframerate()
    length = wav_file.getnframes()

    print "length:",length

    channel_count = wav_file.getnchannels()

    comp_type = wav_file.getcomptype()
    comp_name = wav_file.getcompname()
    
    message = ""

    message_length = 5

    d = ((length - 400)/8) / message_length
    print "d", d
    
    # result = []
    # for c in message:
    #     bits = bin(ord(c))[2:]
    #     bits = '00000000'[len(bits):] + bits
    #     result.extend([int(b) for b in bits])
    # print result

    # output = wave.open('out.wav', 'w')
    # output.setparams((channel_count, sample_width, frame_rate, length, comp_type, comp_name))

    values = []

    n = 0
    for i in range(0, length):
        st = wav_file.readframes(1)
        j = 0
        
        for x in st:
            if(j == 0 and i > 100):
                # print "setting bit"
                # print "lengthy " , len(str(set_bit(ord(x),7,1))[:1])
                if((i) <= (100+(message_length*8))):  
                    print "mod", get_bit(ord(x),7), "at",n, ",",j
                    s = get_bit(ord(x),7)
                    values.append(s)
     
            j += 1
        n += 1

    # value_str = ''.join(values)
    # output.writeframes(value_str)

    # output.close() 
    wav_file.close() 
    print values 

def get_bit(v, index):
  """Set the index:th bit of v to 1 if x is true, else to 0, and return the new value."""
  mask = 1            # Compute mask, an integer with just bit 'index' set.
  v >>= index
  v &= mask
#   v &= ~mask          # Clear the bit indicated by the mask (if x is False)
  return v            # Return the result, we're done.      

if __name__ == "__main__":
    main()



