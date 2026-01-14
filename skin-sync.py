from pathlib import Path

skins_path = Path("./staging")
gta3_img_path = Path("../models/gta3.img")
excludes = []

def check_excludes(excludes):
    excludes_file = Path("excludes")
    if excludes_file.exists():
        with open(excludes_file, "r") as readExcludes:
            for line in readExcludes:
                excludes.append(line.strip()) 

def main(skins_path, excludes):
    dff_files = [path for path in skins_path.rglob("*.dff") if str(path) not in excludes]
    txd_files = [path for path in skins_path.rglob("*.txd") if str(path) not in excludes]
    
    with open("skin-sync.txt", "w") as f_out:
        f_out.write(f"// Do not modify this file directly\n\n-open "{gta3_img_path}"\n")
        
        for valid_skin_file in dff_files:
            f_out.write(f'-import "{valid_skin_file}"\n')
        
        for valid_skin_file in txd_files:
            f_out.write(f'-import "{valid_skin_file}"\n')
        
        f_out.write("\n-exit")
    
    with open("excludes", "a") as writeExcludes:
        for valid_skin_file in dff_files + txd_files:
            writeExcludes.write(f"{valid_skin_file}\n")
            print(f"Added: {valid_skin_file}")

if __name__ == "__main__":
    check_excludes(excludes)
    main(skins_path, excludes)