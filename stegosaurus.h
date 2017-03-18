// WAVE file header format
typedef struct  WAV_HEADER
{
    /* RIFF Chunk Descriptor */
    char         RIFF[4];               // RIFF Header Magic header
    uint32_t        chunk_size;         // RIFF Chunk Size
    char         WAVE[4];            // WAVE Header
    /* "fmt" sub-chunk */
    char            sub_chunk1ID[4];             // FMT header
    uint32_t        sub_chunk1_size;    // Size of the fmt chunk
    uint16_t        audio_format ;      // Audio format 1=PCM,6=mulaw,7=alaw,     257=IBM Mu-Law, 258=IBM A-Law, 259=ADPCM
    uint16_t        num_channels;          // Number of channels 1=Mono 2=Sterio
    uint32_t        sample_rate;  // Sampling Frequency in Hz
    uint32_t        bytesPerSec;    // bytes per second
    uint16_t        blockAlign;     // 2=16-bit mono, 4=16-bit stereo
    uint16_t        bits_per_sample;  // Number of bits per sample
    /* "data" sub-chunk */
    char            sub_chunk2ID[4]; // "data"  string
    uint32_t        data_size;  // Sampled data length
} wav_hdr;