#include <iostream>
#include <stdint.h>


#include "stegosaurus.h"
#include "Wav.h"

using namespace std;

// unsigned char buffer4[4];
// unsigned char buffer2[2];
// unsigned char buffer138[138];

int main(int argc, char* argv[])
{
    const char* filePath;
    string input;
    if (argc <= 1)
    {
        cout << "Input wave file name: ";
        cin >> input;
        cin.get();
        filePath = input.c_str();
    }
    else
    {
        filePath = argv[1];
        cout << "Input wave file name: " << filePath << endl;
    }

    Wav wav_read = Wav(filePath);
    
    // print_char_array(wav_read.getRIFF(),4);


    long num_samples;
    long size_of_each_sample;


    return 0;

    // cout << "Welcome to Stegosaurus" << endl;
    // wav_hdr wave_header;
    // int headerSize = sizeof(wav_hdr), filelength = 0;

    // ofstream wave_out ("test.wav", ofstream::binary);

    // if(wav_file.is_open())
    // {   
    //     wav_file.read(wave_header.RIFF, 4);         //RIFF string
    //     wave_out.write(wave_header.RIFF, 4);
        
    //     wav_file.read((char*)buffer4, 4);                  //chunk_size 
    //     wave_out.write((char*)buffer4, 4);                  //chunk_size 

    //     wave_header.chunk_size = buffer4[0] | (buffer4[1] << 8) | (buffer4[2] << 16) | (buffer4[3] << 24);

    //     wav_file.read(wave_header.WAVE, 4);         //WAVE string
    //     wave_out.write(wave_header.WAVE, 4);         //WAVE string

    //     wav_file.read(wave_header.sub_chunk1ID, 4);          //fmt header (Subchunk1ID)
    //     wave_out.write(wave_header.sub_chunk1ID, 4);          //fmt header (Subchunk1ID)
        
    //     wav_file.read((char*)buffer4, 4);                  //TODO implement
    //     wave_out.write((char*)buffer4, 4);
        
    //     wav_file.read((char*)buffer2, 2);
    //     wave_out.write((char*)buffer2, 2);                  //audio_format
    //     wave_header.audio_format = buffer2[0] | (buffer2[1] << 8);
        
    //     wav_file.read((char*)buffer2, 2);                  //num_channels
    //     wave_out.write((char*)buffer2, 2);
    //     wave_header.num_channels = buffer2[0] | (buffer2[1] << 8);
        
    //     wav_file.read((char*)buffer4, 4);                  //sample_rate
    //     wave_out.write((char*)buffer4, 4); 

    //     wave_header.sample_rate = buffer4[0] | (buffer4[1] << 8) | (buffer4[2] << 16) | (buffer4[3] << 24);

    //     wav_file.read((char*)buffer4, 4);                  //TODO implement byte_rate
    //     wave_out.write((char*)buffer4, 4);

    //     wav_file.read((char*)buffer2, 2);                  //TODO implement block align
    //     wave_out.write((char*)buffer2, 2); 

    //     wav_file.read((char*)buffer2, 2);                  //TODO implement bits_per_sample
    //     wave_out.write((char*)buffer2, 2);

    //     wave_header.bits_per_sample = buffer2[0] | (buffer2[1] << 8);
        
    //     wav_file.read((char*)wave_header.sub_chunk2ID, 4); //sub_chunk2ID. Shoud contain word "data".
    //     wave_out.write((char*)wave_header.sub_chunk2ID, 4);
        
    //     wav_file.read((char*)buffer4, 4);                  //sub_chunk2_Size
    //     wave_out.write((char*)buffer4, 4);
        
    //     wav_file.read((char*)buffer138, 138); 
    //     wave_out.write((char*)buffer138, 138);
        
    //     cout << "--------------LIST----------------" << endl;
    //     print_bytes((char*)buffer138, 138);
    //     cout << "--------------END LIST----------------" << endl;
    //     print_bytes(wave_header.sub_chunk2ID, 4);
    //     char         WAVEE[4];            // WAVE Header
    //     wav_file.read((char*)WAVEE, 4);                  //sub_chunk2_Size
    //     wave_out.write((char*)WAVEE, 4);
    //     print_bytes(WAVEE,4);   
    //     wav_file.read((char*)buffer4, 4);
    //     wave_out.write((char*)buffer4, 4);
        
    //     wave_header.data_size = buffer4[0] | (buffer4[1] << 8) | (buffer4[2] << 16) | (buffer4[3] << 24);

    //     num_samples = (8 * wave_header.data_size) / (wave_header.num_channels * wave_header.bits_per_sample);
    //     size_of_each_sample = (wave_header.num_channels * wave_header.bits_per_sample) / 8;

    // }
    // else 
    // {
    //     cout << "Unable to open file" << endl;
    // }

    // print_bytes(wave_header.RIFF, 4);
    // cout << "chunk_size: " << wave_header.chunk_size << endl;
    // print_bytes(wave_header.WAVE, 4);
    // cout << "sub_chunk1ID: ";
    // print_bytes(wave_header.sub_chunk1ID, 4);
    // cout << "audio_format: " << wave_header.audio_format << endl;
    // cout << "num_channels: " << wave_header.num_channels << endl;
    // cout << "sample_rate: " << wave_header.sample_rate << endl;
    // cout << "bits_per_sample: " << wave_header.bits_per_sample << endl;
    // cout << "sub_chunk2ID: ";
    // print_bytes(wave_header.sub_chunk2ID, 4);
    // cout << "data_size: " << wave_header.data_size  << endl;
    // cout << "num_samples: " << num_samples << endl;
    // cout << "size_of_each_sample: " << size_of_each_sample << " bytes" << endl;

    // char data_buffer[1];


    // cout << "size!!!: " << wave_header.data_size << endl;
    // for (int i = 0; i < wave_header.data_size; i++)
    // {
    //     wav_file.read(data_buffer, 1);
    //     wave_out.write(data_buffer, 1);
    // }

    // wav_file.close();
    // wave_out.close();
    // cout << "wave closed" << endl;

}
