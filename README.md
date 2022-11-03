# Genshin Achievements Reader

This tool reads your Genshin Impact achievements and stores them in a formatted file that can directly be used with [paimon.moe](https://paimon.moe/)

## Usage

Install tesseract, follow this [guide](https://github.com/tesseract-ocr/tesseract#installing-tesseract)

Run the script and adjust the window to cover the achievements page. Then press <kbd>Enter</kbd> on the keyboard to start scanning for the current page.

A page refers to the achievement pages in Genshin Impact, i.e "Wonders of the World" or "Mortal Travails: Series I"

Once you are done scanning a page, press the <kbd>Right</kbd> or <kbd>Left</kbd> arrow key on your keyboard to switch pages.

Once you are done scanning, press <kbd>Esc</kbd> to save the scanned achievements to a file.

The file will be named `completed.json`.

Copy the contents of `completed.json` and paste it into line 12 of `update_script.js` as the first argument of `objectStore.put()`

Then copy the contents of `update_script.js` and run it in the dev tools window of [paimon.moe](https://paimon.moe/)

## Updating Achievement Data

This project uses the achievement data and IDs from [paimon.moe](https://paimon.moe/). In the event where new achievements are added, the process to update the file is as follows:

1. Go to the [achievement page of paimon.moe](https://paimon.moe/achievement) and open the network tab. Sort by size and pick the first `.js` file.

2. The file is minified so maybe use VS Code to pretty-fy it and then find the object where the achievements are stored at.

3. Use whatever you want to convert it to JSON, initially I pasted into a `.js` file and use node to write it to a json file.

4. Name it as `achievements.json`.

## To-do

1. Add ability to scan tiers of complete-ness of achievements.

## Preview

This is an early version but it still does the same thing

[![Watch the video](https://user-images.githubusercontent.com/20278298/199739441-42843f71-5588-4b73-beeb-3b0220fe9525.png)
](https://www.youtube.com/embed/lpvMbs4FRPs)
