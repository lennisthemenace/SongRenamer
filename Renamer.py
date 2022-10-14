from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4
import os
import shutil
from path import Path

if __name__ == "__main__":
    folder = str(Path(__file__).parent)
    processed_folder = os.path.join(folder, "Processed")
    renamed_folder = os.path.join(folder, "Renamed")
    if not os.path.exists(renamed_folder):
        os.mkdir(renamed_folder)
    if not os.path.exists(processed_folder):
        os.mkdir(processed_folder)

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if file.endswith(".mp3"):
            try:
                audio = EasyID3(file_path)
                if audio.get('title') and audio.get('artist'):
                    title = str(audio['title'][0]).replace("/", "-")
                    artist = str(audio['artist'][0]).replace("/", "-")
                    if len(artist) > 15:
                        artist = ""
                    new_file_name = f"{title} - {artist}.mp3"
                else:
                    album = str(audio['album'][0]).replace("/", "-")
                    track = str(audio['tracknumber'][0])
                    new_file_name = f"{track} - {album}.mp3"
                if not os.path.exists(os.path.join(renamed_folder, new_file_name)):
                    shutil.copy(file_path,
                                os.path.join(renamed_folder, new_file_name))
                else:
                    print("Already Exists")
                shutil.move(file_path,
                            os.path.join(processed_folder, file))
            except Exception as e:
                pass

        if file.endswith("m4a"):
            try:
                mp4 = MP4(file_path).tags
                title = mp4['\xa9nam'][0].replace("/", "-")
                artist = mp4['\xa9ART'][0].replace("/", "-")
                new_file_name = f"{title} - {artist}.m4a"
                if not os.path.exists(os.path.join(renamed_folder, new_file_name)):
                    shutil.copy(file_path,
                                os.path.join(renamed_folder, new_file_name))
                else:
                    print("Already Exists")
                shutil.move(file_path,
                            os.path.join(processed_folder, file))
            except Exception as e:
                pass
