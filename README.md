# HSK Flashcards

Pleco flashcards to use alongside HSK course.

Definitions from textbooks are not available. Pleco definitions are to be used.

Currently, database includes only upto **HSK 4**.

## How to use:

### Generating flashcards

- Run in command line: `python3 script.py`
- Flashcard options:
  - `newwords`: List of new words as introduced in textbook. Organized by HSK levels and lessons.
  - `newcharacters`: List of new characters introduced first time.
  - `heisig`: For those who are using Heisig's method from **Remembering Simplified Hanzi** book. List of characters and definitions in heisig order. (_Credit: [Alexis](https://www.plecoforums.com/threads/heisigs-remembering-simplified-hanzi-1-2.3114/) for `RSH_V2.txt`_)
- Selecting HSK levels `[1, 2, 3, 4a, 4b, 4]`:
  - `--hskfromto <from> <to>`
  - `--hsklevels <level1> <level2> ...`
- Examples:
  - `python3 script.py newcharacters --hskfromto 1 4a`
  - `python3 script.py newwords --hsklevels 1 2 4`
  - `python3 script.py newwords newcharacters heisig --hskfromto 1 3 --hsklevels 4b`

### Importing

After generating flashcard files (`.txt` files in `out` directory). It can be **imported** in Pleco app.

## Contribution

Any suggestions or contributions are welcome.
