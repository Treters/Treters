import os

# Ange roten för mappträdet
root_folder = "C:/Path/To/Your/Folder"

# Bild- och videoändelser att identifiera
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
video_extensions = {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"}
media_extensions = image_extensions.union(video_extensions)

# Funktion för att kontrollera om en mapp innehåller bilder eller videor
def contains_media_files(folder):
    for file in os.listdir(folder):
        if file.lower().endswith(tuple(media_extensions)):
            return True
    return False

# Funktion för att räkna antalet undermappar med bilder eller videor
def count_subfolders_with_media(folder):
    count = 0
    for subfolder in next(os.walk(folder))[1]:
        subfolder_path = os.path.join(folder, subfolder)
        if contains_media_files(subfolder_path):
            count += 1
    return count

# Huvudfunktion för att skapa lista
def list_folders_with_media(root_folder):
    folder_data = []

    for root, dirs, files in os.walk(root_folder):
        if contains_media_files(root):
            subfolder_count = count_subfolders_with_media(root)
            folder_data.append((root, subfolder_count))

        # Gå bara igenom översta nivån för submappar
        dirs[:] = []  # Detta gör att den inte traverserar längre ned

    return folder_data

# Skapa lista och skriv ut
folders_with_media = list_folders_with_media(root_folder)

print("Lista över mappar med bilder och filmer:")
for folder, subfolder_count in folders_with_media:
    print(f"{folder} ({subfolder_count} undermappar med media)")

# Spara till en fil (valfritt)
output_file = "folders_with_media.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for folder, subfolder_count in folders_with_media:
        f.write(f"{folder} ({subfolder_count} undermappar med media)\n")

print(f"Listan sparades till {output_file}")
