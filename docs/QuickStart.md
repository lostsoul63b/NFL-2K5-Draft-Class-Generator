# NFL 2K5 Draft Class Generator v2.0

Updated GUI tool by **LostsouL** (fork of 2k5master's original)

---

## Quick Start Guide

### Prerequisites
- mymc
- Flying Finn’s NFL 2K5 Gamesave Editor
- Bad_AL’s NFL2K5 Tool

---

### Step-by-Step Instructions

1. **Extract** the ZIP file into a new folder and run `NFL2K5_DraftClassGenerator_v2.0.exe`

2. **Export Names** (for custom rosters):
   - Open your franchise in Bad_AL’s Tool
   - Go to **View** → deselect everything except **List Teams**
   - Save as `names.txt`

3. **Export Draft Class**:
   - Switch view to **List Draft Class only**
   - Save as `class.csv`

4. **Update Name Database**:
   - In the tool, browse to your `names.txt` under **Roster TXT File**
   - Click **Generate acceptableNames.txt**

5. **Generate Draft Class**:
   - Browse to your `class.csv` under **Roster CSV File**
   - Click **Generate New Draft Class**
   - `new.csv` will be created and opened automatically

### Alternative Options

- **Generate Random Draft Class** – Creates a full 380-player draft class instantly (no CSV needed)
- **Suffix Toggle** – Green button = Remove suffixes (Jr, Sr, III, etc.) | Grey = Keep suffixes

---

### Final Import Steps

6. Open your franchise in Bad_AL’s Tool (List Draft Class view)
7. Clear the window, then drag & drop `new.csv` into it and save
8. Open the save in Flying Finn’s Editor → open any player → click **Accept** → save
9. Import the modified save back into mymc

You’re now ready to load your franchise and enjoy the new draft class!

---

## Tips

- The tool remembers your last used files
- Always run the .exe from the same folder containing `acceptableNames.txt`
- **Green button** = Name suffixes (Jr, Sr, III, etc.) will be removed.
- **Grey button** = Name suffixes will be kept.
- Use **Show Debug Info** if you encounter any issues

---

**Enjoy building your franchises!** 🏈
