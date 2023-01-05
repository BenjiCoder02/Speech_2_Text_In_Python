# Speech_2_Text_In_Python

This Python program makes use of the Speech Recognition library in Python and uses Google Speech to Text api to generate transcripts.

It converts mp4 clips to mp3 and then to wav using ffmpeg.

It splits the .wav audio file into chunks using silence as a break point.

Once all chunks are generated it itertates over the chunks and sends each one to Google's Speech to Text api. The accuracy varies based on audio quality and how coherent the speech is.

Before running the script install ffmpeg.
Then use pip to install `pydub` `mutagen` `SpeechRecognition`
Or copy the below command and paste in your terminal

pip install pydub mutagen SpeechRecognition


To use this
1. Create a folder titled "Clips" in the same directory as the .py script.
2. Add your clip to the Clips folder
3. The clip should be in .mp4 format. (I intend to change this so you can use any format)
4. Then run "python3 speechToTxt.py {clipname_without_extension}"  Replace {clipname_without_extension} with the name of the clip that you want without the  extension.
5. Hit Enter. 
