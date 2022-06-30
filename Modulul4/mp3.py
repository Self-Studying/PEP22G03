

# importing the module

from pytube import YouTube

# location where to sqave the downloaded file

save_path = "sudo /home/phoenix/python"

# youtube url link

# link = "https://www.youtube.com/watch?v=A_HQJgLUe8Q"

try:
    # object creation using YouTbe
    # which was imported at the beginning
    YouTube('https://www.youtube.com/watch?v=A_HQJgLUe8Q').streams.first().download(save_path)
    yt = YouTube('https://www.youtube.com/watch?v=A_HQJgLUe8Q')
    yt.streams.filter(progressive=True, file_extension='mp4')


except:
    print("Connection Error!")  # to handle exception

# filters out all the files with mp4"  extension

# yt.filter(progressive=True, file_extension='mp4')

# to set the name of the file

# yt.set_filename('IrinaRimesVideo')

# get the video with the extension and resolution passe3d in the get() function

# d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
# try:
# downloading the video
# d_video.download(save_path)
# except:
#       print("Some Error!")
# print('Task Completed!')
