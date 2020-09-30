This project simply takes a face and recognises it.
At present it can recognise only 8 faces because its known faces database isnt big enough.
The program starts with encoding process which takes some time, so reman patient. When the System notifies, the process of encoding is finished and it can be carried forward to recognition.

Further improvements:
optimize the encoding, separate it into a different py file and make it save the list of encodings into a file
make the main program read that list from that file. This was we wont have to run the encoding again and again.
