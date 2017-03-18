#include "Wav.h"
#include "util.h"

unsigned char buffer4[4];
unsigned char buffer2[2];
unsigned char buffer138[138];
unsigned char buffer32[40];
unsigned char data[4] = {0x64, 0x61, 0x74, 0x61};

bool arrayCompare(unsigned char* ar1, unsigned char* ar2, int n);

Wav::Wav(const char* infile_path)
{
    cout << "constructor" << endl;

    ifstream wav_file;
    wav_file.open(infile_path, ofstream::binary);

    if(!wav_file.is_open())
    {
        cout << "Error opening file" << endl;
        return;
    }

    data_byte_offset = 0;

    ofstream wave_out ("out.wav", ofstream::binary);

    int count = 0;
    bool seek_data_marker = true;
    while(seek_data_marker)
    {
        wav_file.read((char*)buffer2, 2);
        wave_out.write((char*)buffer2, 2);

        data_byte_offset += 2;

        buffer4[2] = buffer2[0];
        buffer4[3] = buffer2[1];

        if(arrayCompare(data, buffer4, 4))
        {
            print_char_array((char*)buffer4, 4);
            wav_file.read((char*)buffer4, 4); //Read data size
            wave_out.write((char*)buffer4, 4);

            data_size = buffer4[0] | (buffer4[1] << 8) | (buffer4[2] << 16) | (buffer4[3] << 24);
            cout << "data size: " << data_size << endl;
            seek_data_marker = false;
        }
        buffer4[0] = buffer4[2];
        buffer4[1] = buffer4[3];
    }

    for (int i = 0; i < data_size; i++)
    {
        wav_file.read((char*)buffer4, 4);
        wave_out.write((char*)buffer4, 4);
    }

    cout << data_byte_offset << endl;

    wav_file.close();
    wave_out.close();
}

char* Wav::getRIFF()
{
    return RIFF;
}

int Wav::extractData()
{
    
}

bool arrayCompare(unsigned char* ar1, unsigned char* ar2, int n)
{
    for(int i = 0; i < n; i++)
    {
        if(ar1[i] != ar2[i]) 
            return false;
    }

    return true;
}

