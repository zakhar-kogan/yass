A small utility to slice audio files into arbitrary chunks.

Requires pydub and click libraries to be installed.

**Usage:**  
  audio_slicer.py [OPTIONS] FILENAME

**Options:**  
  --d INTEGER  duration of each slice in seconds, 40 by default  
  --r          remove the source file?  
  --e TEXT     optional file extension; e.g. mp3, or ogg  
  --f TEXT     optional output folder; e.g. output  
