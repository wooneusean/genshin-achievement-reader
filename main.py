from pprint import isreadable
import pytesseract
import numpy as np
from mss import mss
from tkinter import *
import json
from fuzzywuzzy import fuzz

achievement_page = 0

f = open("./achievements.json", encoding="utf-8")
achievements = json.load(f)
completed_achievements = {str(achievement_page): {}}
has_exited = False
is_ready = False


def find_achievement_name(achievement_list, name):
    for achievement in achievement_list:
        # check if array
        if isinstance(achievement, list):
            result = find_achievement_name(achievement, name)
            if result is not None:
                return result
            continue

        if fuzz.ratio(achievement["name"], name) > 80:
            return achievement


def close_win(e, root):
    global has_exited
    with open(f"./completed.json", "w") as outfile:
        print("Saving completed achievements to completed.json")
        outfile.write(json.dumps(completed_achievements))

    root.destroy()
    has_exited = True


def change_page(e, direction):
    global achievement_page
    global is_ready
    if (achievement_page + direction) < 0 or (achievement_page + direction) > 36:
        return
    is_ready = False
    achievement_page += direction
    completed_achievements[str(achievement_page)] = {}
    print(
        f"Changing page to {achievements[str(achievement_page)]['name']}, press Enter to continue")


def ready_up(e):
    global is_ready
    is_ready = True


root = Tk()
root.title("Genshin Achievement Reader")
root.configure(bg="red")
root.attributes("-transparentcolor", "red")
root.resizable(True, True)
root.bind('<Escape>', lambda e: close_win(e, root))
root.bind('<Left>', lambda e:  change_page(e, -1))
root.bind('<Right>', lambda e:  change_page(e, 1))
root.bind('<Return>', lambda e:  ready_up(e))
change_page(None, 0)

with mss() as sct:
    while True and not has_exited:
        if not is_ready:
            root.update()
            continue

        x, y = (int(s) for s in root.geometry().split("+")[1:])
        w, h = (int(s) for s in root.geometry().split("+")[0].split("x"))
        bbox = {
            "top": y + 30,
            "left": x + 10,
            "width": w,
            "height": h
        }

        sct_img = sct.grab(bbox)

        lines = pytesseract.image_to_string(np.array(sct_img)).split("\n")
        for line in lines:
            if line == "":
                continue
            achievement = find_achievement_name(
                achievements[str(achievement_page)]["achievements"],
                line
            )

            if achievement is not None and achievement["id"] not in completed_achievements[str(achievement_page)]:
                completed_achievements[
                    str(achievement_page)
                ][
                    achievement["id"]
                ] = True

                print("Added achievement: " + achievement["name"])

        root.update()
