# ================================================
# NFL2K5 Draft Class Generator GUI - Version 2.0
# Updated by LostsouL
# ================================================

import csv
import random
import webbrowser
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import traceback
import re
import os
import configparser

# ====================== CONFIG FOR LAST FILES ======================
config = configparser.ConfigParser()
config_file = 'generator_config.ini'

def load_last_files():
    if os.path.exists(config_file):
        config.read(config_file)
        return config.get('LastFiles', 'csv', fallback=''), config.get('LastFiles', 'txt', fallback='')
    return '', ''

def save_last_files(csv_path, txt_path):
    config['LastFiles'] = {'csv': csv_path, 'txt': txt_path}
    with open(config_file, 'w') as f:
        config.write(f)

last_csv, last_txt = load_last_files()

# Load acceptable names
def load_names():
    global first_names, last_names
    first_names = []
    last_names = []
    try:
        with open('acceptableNames.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or ',' not in line:
                    continue
                parts = line.split(',')
                if len(parts) >= 2:
                    fname = parts[0].strip()
                    lname = parts[1].strip()
                    if len(fname) >= 3 and len(lname) >= 3:
                        first_names.append(fname)
                        last_names.append(lname)
    except:
        pass

first_names = []
last_names = []
load_names()

# ====================== GENERATION FUNCTIONS ======================
def generate_draft_class(use_random=False):
    generate_btn.config(state="disabled")
    status_label.config(text="Generating draft class... Please wait.")
    progress_bar['value'] = 0
    root.update()

    try:
        if use_random:
            position_list = ["QB"]*30 + ["RB"]*40 + ["WR"]*60 + ["TE"]*25 + ["OL"]*80 + \
                           ["DT"]*25 + ["DE"]*25 + ["LB"]*60 + ["CB"]*40 + ["S"]*35 + \
                           ["K"]*10 + ["P"]*10
            number_list = [str(random.randint(1,99)) for _ in range(len(position_list))]
            random.shuffle(position_list)
            valid_positions = {"QB","HB","FB","WR","TE","OL","C","G","T","DT","DE","LB","OLB","ILB","CB","S","FS","SS","K","P","KR","PR","LS"}
        else:
            csv_name = csv_entry.get().strip()
            if not csv_name:
                messagebox.showwarning("Input Required", "Please select a CSV file")
                status_label.config(text="Ready")
                generate_btn.config(state="normal")
                return

            with open(csv_name, newline='', encoding='utf-8') as csvfile:
                filecsv = csv.reader(csvfile, delimiter=' ', quotechar='|')
                position_list = []
                number_list = []
                valid_positions = {"QB","HB","FB","WR","TE","OL","C","G","T","DT","DE","LB","OLB","ILB","CB","S","FS","SS","K","P","KR","PR","LS"}

                for row in filecsv:
                    if not row: continue
                    line = ' '.join(row)
                    numbers = re.findall(r'\b\d+\b', line)
                    jersey = numbers[-1].lstrip('0') or '0' if numbers else '00'

                    pos_match = re.search(r'\b(QB|HB|FB|WR|TE|OL|C|G|T|DT|DE|LB|OLB|ILB|CB|S|FS|SS|K|P|KR|PR|LS)\b', line, re.IGNORECASE)
                    if pos_match:
                        pos = pos_match.group(1).upper()
                        position_list.append(pos)
                        number_list.append(jersey)

        # Remove headers
        while position_list and position_list[0] not in valid_positions:
            if position_list: position_list.pop(0)
            if number_list: number_list.pop(0)

        target = 380
        if len(position_list) < target:
            extra_needed = target - len(position_list)
            extra_pos = random.choices(list(valid_positions), k=extra_needed)
            extra_num = [str(random.randint(1,99)) for _ in range(extra_needed)]
            position_list.extend(extra_pos)
            number_list.extend(extra_num)

        position_list = position_list[:target]
        number_list = number_list[:target]

        global fnames_list, lnames_list, new_position_list, new_numbers_list
        fnames_list = []
        lnames_list = []
        new_position_list = []
        new_numbers_list = []

        with open("new.csv", 'w', newline='', encoding='utf-8') as csvwriter:
            writer = csv.writer(csvwriter)
            writer.writerow(["#Position", "fname", "lname", "JerseyNumber"])
            writer.writerow([])
            writer.writerow(["Team = DraftClass    Players:380"])

            for i in range(target):
                f_idx = random.randint(0, len(first_names)-1)
                l_idx = random.randint(0, len(last_names)-1)
                fname = first_names[f_idx]
                lname = last_names[l_idx]
                pos = position_list[i]
                num = number_list[i]
                writer.writerow([pos, fname, lname, num])
                fnames_list.append(fname)
                lnames_list.append(lname)
                new_position_list.append(pos)
                new_numbers_list.append(num)

                progress = int((i + 1) / target * 100)
                progress_bar['value'] = progress
                status_label.config(text=f"Generating... {i+1}/{target} players")
                root.update()

        save_last_files(csv_entry.get().strip(), txt_entry.get().strip())
        messagebox.showinfo("Success", f"Draft class with {target} players saved to new.csv")
        status_label.config(text=f"✅ Success! {target} players generated")
        
        try:
            os.startfile("new.csv")
        except:
            pass

    except Exception as e:
        messagebox.showerror("Error", f"Generation failed:\n{str(e)}")
        status_label.config(text="❌ Generation failed")
    finally:
        generate_btn.config(state="normal")
        progress_bar['value'] = 0

# ====================== OTHER FUNCTIONS ======================
def browse_csv():
    filename = filedialog.askopenfilename(title="Select Roster CSV File", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
    if filename:
        csv_entry.delete(0, tk.END)
        csv_entry.insert(0, filename)

def browse_txt():
    filename = filedialog.askopenfilename(title="Select Roster TXT File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        txt_entry.delete(0, tk.END)
        txt_entry.insert(0, filename)

# Toggle Button State
remove_suffixes = True  # True = Remove suffixes

# Toggle Button State
remove_suffixes = True  # True = Remove suffixes

def toggle_suffix_button():
    global remove_suffixes
    remove_suffixes = not remove_suffixes
    
    if remove_suffixes:
        suffix_btn.config(text="Remove name suffixes (Jr, Sr, III)", bg="#00cc66", fg="black")
    else:
        suffix_btn.config(text="Keep name suffixes (Jr, Sr, III)", bg="#555555", fg="white")
    
    # Auto-update acceptableNames.txt if a TXT file is selected
    txt_name = txt_entry.get().strip()
    if txt_name:
        messagebox.showinfo("Auto-Updating", "Suffix setting changed.")
        generate_acceptable_names()  # Auto call
    else:
        messagebox.showinfo("Setting Updated", 
            "Suffix setting changed!\n\nPlease select a Roster TXT file and click 'Generate acceptableNames.txt' to apply.")

def generate_acceptable_names():
    status_label.config(text="Generating acceptableNames.txt...")
    try:
        txt_name = txt_entry.get().strip()
        if not txt_name:
            messagebox.showwarning("Input Required", "Please select or enter the TXT filename")
            status_label.config(text="Ready")
            return

        with open(txt_name, 'r', encoding='utf-8') as b:
            names_data = b.read()

        names_lines = names_data.split('\n')
        acc_f = []
        acc_l = []

        for element in names_lines:
            temp = element.split(',')
            if len(temp) >= 4 and temp[0].strip():
                fname = temp[1].strip()
                lname = temp[2].strip()
                
                # Strong filtering to prevent asterisks in game
                if (len(fname) >= 3 and len(lname) >= 3 and
                    len(fname) <= 12 and len(lname) <= 14 and
                    not any(c in fname for c in ".'-*") and
                    not any(c in lname for c in ".'-*") and
                    not fname.isdigit() and not lname.isdigit()):
                    acc_f.append(fname)
                    acc_l.append(lname)

        if acc_f: acc_f.pop(0)
        if acc_l: acc_l.pop(0)

        # Apply user suffix setting
        if remove_suffixes:
            i = 0
            while i < len(acc_l):
                element = acc_l[i]
                remove = False
                if ' ' in element or '-' in element or "'" in element:
                    remove = True
                elif len(element) > 10:
                    remove = True
                elif element.endswith(("Jr", "Sr", "IV", "II", "V", "III", "Jr.")):
                    remove = True
                if remove:
                    del acc_l[i]
                    del acc_f[i]
                else:
                    i += 1

        with open('acceptableNames.txt', 'w', encoding='utf-8') as g:
            for i in range(min(len(acc_f), len(acc_l))):
                g.write(acc_f[i] + ',' + acc_l[i] + '\n')

        status_label.config(text="✅ acceptableNames.txt generated successfully")
        load_names()
        messagebox.showinfo("Success", f"acceptableNames.txt updated successfully!\n{len(acc_f)} names saved.")
        
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="❌ Failed")

def show_debug():
    debug_win = tk.Toplevel(root)
    debug_win.title("Debug Info")
    debug_win.configure(bg="#2b2b2b")
    txt = scrolledtext.ScrolledText(debug_win, width=100, height=30, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 10))
    txt.pack(padx=10, pady=10)
    txt.insert(tk.END, f"First Names Loaded: {len(first_names)}\n")
    txt.insert(tk.END, f"Last Names Loaded: {len(last_names)}\n\n")
    txt.insert(tk.END, "First Names Sample:\n" + str(first_names[:30]) + "\n\n")
    txt.insert(tk.END, "Last Names Sample:\n" + str(last_names[:30]) + "\n\n")
    txt.insert(tk.END, f"Generated Players: {len(fnames_list)}\n")

# ====================== GUI ======================
root = tk.Tk()
root.title("ESPN NFL 2K5 Draft Class Generator GUI - v2.0")
root.geometry("650x580")
root.configure(bg="#1e1e1e")

title_frame = tk.Frame(root, bg="#1e1e1e")
title_frame.pack(pady=15)
tk.Label(title_frame, text="ESPN NFL 2K5 Draft Class Generator v2.0", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="#00ccff").pack()

# File inputs
frame_csv = tk.Frame(root, bg="#1e1e1e")
frame_csv.pack(pady=8)
tk.Label(frame_csv, text="Roster CSV File:", bg="#1e1e1e", fg="#ffffff").pack(anchor="w")
csv_subframe = tk.Frame(frame_csv, bg="#1e1e1e")
csv_subframe.pack()
csv_entry = tk.Entry(csv_subframe, width=50, bg="#2b2b2b", fg="#ffffff", insertbackground="white")
csv_entry.insert(0, last_csv)
csv_entry.pack(side="left", padx=(0,5))
tk.Button(csv_subframe, text="Browse", command=browse_csv, bg="#444444", fg="#ffffff").pack(side="left")

frame_txt = tk.Frame(root, bg="#1e1e1e")
frame_txt.pack(pady=8)
tk.Label(frame_txt, text="Roster TXT File (for names):", bg="#1e1e1e", fg="#ffffff").pack(anchor="w")
txt_subframe = tk.Frame(frame_txt, bg="#1e1e1e")
txt_subframe.pack()
txt_entry = tk.Entry(txt_subframe, width=50, bg="#2b2b2b", fg="#ffffff", insertbackground="white")
txt_entry.insert(0, last_txt)
txt_entry.pack(side="left", padx=(0,5))
tk.Button(txt_subframe, text="Browse", command=browse_txt, bg="#444444", fg="#ffffff").pack(side="left")

# Progress and Status
progress_bar = ttk.Progressbar(root, length=355, mode='determinate')
progress_bar.pack(pady=10)
status_label = tk.Label(root, text="Ready", bg="#1e1e1e", fg="#00ff88", font=("Arial", 10))
status_label.pack(pady=5)

btn_pad = 6

tk.Button(root, text="Generate Random Draft Class", command=lambda: generate_draft_class(True),
          bg="#444444", fg="white", font=("Arial", 10, "bold"), height=1, width=31).pack(pady=btn_pad)

generate_btn = tk.Button(root, text="Generate New Draft Class", command=lambda: generate_draft_class(False),
                         bg="#444444", fg="white", font=("Arial", 10, "bold"), height=1, width=31)
generate_btn.pack(pady=btn_pad)

# Suffix Toggle Button
suffix_btn = tk.Button(root, text="Remove name suffixes (Jr, Sr, III)", command=toggle_suffix_button,
                       bg="#00cc66", fg="black", font=("Arial", 10, "bold"), width=31)
suffix_btn.pack(pady=btn_pad)

tk.Button(root, text="Generate acceptableNames.txt", command=generate_acceptable_names, 
          bg="#444444", fg="white", font=("Arial", 10, "bold"), width=31).pack(pady=btn_pad)

tk.Button(root, text="Quick Start Guide", command=lambda: webbrowser.open('https://github.com/lostsoul63b/NFL-2K5-Draft-Class-Generator/blob/master/docs/QuickStart.md'), 
          bg="#444444", fg="#ffffff", font=("Arial", 10, "bold"), width=31).pack(pady=btn_pad)

tk.Button(root, text="Show Debug Info", command=show_debug, bg="#444444", fg="#ffffff", font=("Arial", 10, "bold"), width=31).pack(pady=btn_pad)

tk.Button(root, text="Exit", command=root.quit, bg="#cc3333", fg="white", font=("Arial", 10, "bold"), width=31).pack(pady=btn_pad)

root.mainloop()