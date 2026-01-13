from pathlib import Path

skins_path = Path("../staging")
gta3_img_path = Path("../models/gta3.img")

excludes = []

def check_excludes(excludes):
    with open("excludes", "r") as readExcludes:
        for i in readExcludes:
            excludes.append(i)

def main(skins_path):
    check_excludes(excludes)
    valid_skin_file = [path for path in skins_path.rglob('*') if path.name not in excludes]

    with open("skin-sync.txt", "w") as f_out, open("excludes", "a") as writeExcludes:
        f_out.write(f"// Do not modify\n\n-open {gta3_img_path}\n")

        # Combine the extensions you want
        for ext in ["*.dff", "*.txd"]:
            for file_path in skins_path.rglob(ext):
                # CHECK THE EXCLUDES HERE
                if file_path.name not in excludes:
                    f_out.write(f"-import {file_path}\n")
                    writeExcludes.write(f"{file_path.name}\n")
                else:
                    print(f"Skipping {file_path.name}, it is excluded.")

    with open("skin-sync.txt", "a") as append:
        append.write("\n-exit")

if __name__ == "__main__":
    
    main(skins_path)