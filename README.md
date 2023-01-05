# Speech_2_Text_In_Python

This Python program makes use of the Speech Recognition library in Python and uses Google Speech to Text api to generate transcripts.

It splits the audio file into chunks using silence as a break point.

Once all chunks are generated it itertates over the chunks and sends each one to Google's Speech to Text api. The accuracy varies based on audio quality and how coherent the speech is.
