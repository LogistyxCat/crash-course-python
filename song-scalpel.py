import sys
import csv
import subprocess

argv = sys.argv
if len(argv) != 3:
    print("Incorrect usage: cmd audio.mp3 template.csv")
    print(len(argv))
    sys.exit(1)

# get the file to disassemble
audio_file = argv[1]

# get the template file and configuration
t_file = open(argv[2])
t_reader = csv.reader(t_file)
# t_file.close()

# for every row in t_reader,
for row in t_reader:
    # check if the id is a number
    if row[3].isdigit():
        # create a list object with the row value
        name = str(row[0])
        start_time = str(row[1])
        duration = str(row[5])
        id = int(row[3])
        directory = str(row[4])

        filename = "'%d. %s.mp3'" % (id, name)
        cmd = "ffmpeg -i %s -ss %s -t %s -c copy %s" % (audio_file, start_time, duration, filename)
        subprocess.run(cmd, shell=True)

# track_name = "id " + "name" + ".mp3"
# ffmpeg -i audio_file -ss start_time -t duration -c copy filename
