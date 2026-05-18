# ESPN NFL 2K5 Draft Class Generator GUI

**Version 2.0** – Improved GUI Edition

A clean, user-friendly tool that generates complete 380-player draft classes for ESPN NFL 2K5.

**YouTube Tutorial:** [Watch Here]()

---

### ✨ What's New in Version 2.0

- New dark-themed UI
- Easy **Browse** buttons for file selection
- Live **Progress Bar** with real-time status
- Remembers your last used CSV and TXT files
- Automatically opens `new.csv` after generation
- **Generate Random Draft Class** button (no CSV needed)
- Always generates **exactly 380 players**
- Much more reliable position and jersey number parsing
- Safer operation (button disabled while generating)

---

### Step 1: Setup

You need the following tools:

| Tool | Download |
| :------------- | :-------------: | 
| Flying_Finn's Gamesave Editor | [Download](https://github.com/lostsoul63b/NFL-2K5-Draft-Class-Generator/blob/master/NFL%202K5%20GameSave%20Editor.zip) | 
| Bad_AL's NFL 2K5Tool | [Download](https://github.com/lostsoul63b/NFL-2K5-Draft-Class-Generator/blob/master/NFL2K5Tool_0.9.0.9_Release.zip) |
| mymc | [Download](https://github.com/lostsoul63b/NFL-2K5-Draft-Class-Generator/blob/master/mymc.zip) |
| ESPN NFL 2K5 Draft Class Generator GUI v2.0 | (download latest release) |

---

### Step 2: Preparing Your Roster CSV

1. Make sure your franchise is in the **offseason**.
2. Save and close PCSX2.
3. Extract your franchise file using **myMC**.
4. Open **Bad_AL's 2K5Tool**.
5. Load your extracted `.max` file.
6. Go to **View** → deselect everything except **"List Draft Class"**.
7. Click **List Contents** → **File → Save Text** as `.csv`.

---

### Step 3: Using the ESPN NFL 2K5 Draft Class Generator GUI Tool

1. Run `NFL2K5_Draft_Class_Generator.exe`
2. Click **Browse** next to **Roster CSV File** and select your file.
3. (Optional) Select a TXT file for updated acceptable names.
4. Click **"Generate Draft Class (from CSV)"**

   - Watch the progress bar
   - `new.csv` will be created and automatically opened

**Quick Test:** Use **"Generate Random Draft Class (No CSV)"** anytime.

**Name Options:** Use the Disable/Enable buttons to control suffixes (Jr, Sr, III, etc.).

---

### Step 4: Importing Back Into Your Save

1. Open **Bad_AL's NFL 2K5Tool** and load your franchise.
2. View → Only enable **"List Draft Class"**.
3. Click **List Contents** → **Clear**.
4. Open `new.csv` in **Notepad** (not Excel), copy everything.
5. Paste into the tool and click **File → Save**.
6. Open **Flying_Finn's Editor**, load any player, click **Accept**, then save.
7. Use **myMC** to import the modified `.max` file back.

**Always backup your original save first!**

---

### Step 5: Notes

- The tool uses names from your game's database for best compatibility.
- For custom rosters, use **"Generate acceptableNames.txt"** first.
- The tool now intelligently pads to **exactly 380 players** if needed.
- Source code is open and free to modify.

---

Original Creator: **2k5master**  
Version 2.0 UI + Improvements: **LostsouL**

Enjoy your draft classes! 🏈

---

### Feedback & Support
Found a bug or have a suggestion? Feel free to open an issue or message me.
