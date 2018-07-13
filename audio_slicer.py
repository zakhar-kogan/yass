import pydub, sys, os, click

@click.command()
@click.option("duration", '--d', default=40, help='duration of each slice in seconds, 40 by default')
@click.option("remove", '--r', is_flag=True, help='remove the source file?')
@click.option("extension", '--e', help='optional file extension; e.g. mp3, or ogg')
@click.option("output_folder", '--f', default='', help='optional output folder; e.g. output')
@click.argument('filename')
def slice(filename, duration, remove, extension, output_folder):

    # Our file extension for future use
    default_ext = filename.split('.')[1]

    # Getting the audiofile handle
    audio_file = pydub.AudioSegment.from_file(filename, default_ext)

    # Creating a folder if it doesn't exist
    if output_folder:
        if os.path.exists(output_folder) == False:
            os.mkdir(output_folder)
        output_folder += "/"

    # Checking if there's slicing to be done at all
    if audio_file.duration_seconds > duration:

        # Doing the slicing bit
        chunks = audio_file[::duration * 1000]

        # Checking if optional extension is specified, otherwise using the file's default one
        if extension:
            for i, chunk in enumerate(chunks):
                # Saving while printing to console
                print ("Saving chunk {0}...".format(i))
                chunk.export("{2}chunk{0}.{1}".format(i, extension, output_folder), format=extension)
        else:
            for i, chunk in enumerate(chunks):
                # Saving while printing to console
                print ("Saving chunk {0}...".format(i))
                chunk.export("{2}chunk{0}.{1}".format(i, default_ext, output_folder), format=default_ext)
        print ("Done!")

    else:
        # Shouting out if audio's too short, or the chunk size too big
        print ("Audio is too short to be sliced")
        print ("It's {0} seconds long, and the selected chunk size is {1}".format(round(audio_file.duration_seconds, 3), duration))

    # If the remove flag is present, we remove the source file            
    if remove:
        os.remove(filename)

# Our main program
if __name__ == '__main__':
    slice()