import wave, struct


def main():
    wav_file = wave.open("get_lucky.wav", 'r')

    sample_width = wav_file.getsampwidth()
    print "sample width:", sample_width
    frame_rate = wav_file.getframerate()
    length = wav_file.getnframes()

    channel_count = wav_file.getnchannels()

    comp_type = wav_file.getcomptype()
    comp_name = wav_file.getcompname()

    message = "hello"

    d = ((length - 400)/8) / len(message)
    print "d", d
    
    result = []
    for c in message:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    print result

    # print "bit set:",set_bit(1,1,1)

    output = wave.open('out.wav', 'w')
    output.setparams((channel_count, sample_width, frame_rate, length, comp_type, comp_name))

    values = []

    k = 0
    n = 0
    for i in range(0, length):
        st = wav_file.readframes(1)
        j = 0
        
        for x in st:
            if(j == 0 and i > 100):
                # print "setting bit"
                # print "lengthy " , len(str(set_bit(ord(x),7,1))[:1])
                if((i) <= (100+(len(message)*8))): 
                    print "setting:", result[k],"at",n, ",",j
                    s = set_bit(ord(x),7,result[k])
                    k += 1
                    values.append(str(s)[:1])
                else:
                    values.append(x)
            else:
                values.append(x)
            j += 1
        n += 1

    value_str = ''.join(values)
    output.writeframes(value_str)

    wav_file.close()
    output.close()    

def set_bit(v, index, x):
  """Set the index:th bit of v to 1 if x is true, else to 0, and return the new value."""
  mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
  v &= ~mask          # Clear the bit indicated by the mask (if x is False)
  if x:
    v |= mask         # If x was True, set the bit indicated by the mask.
  return v            # Return the result, we're done.      

if __name__ == "__main__":
    main()



