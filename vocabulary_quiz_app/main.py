from __future__ import annotations

import sys

absolute_path = r"C:\Users\USER\Documents\2026_1-vocabulary_quiz_app"
if absolute_path not in sys.path:
    sys.path.insert(0, absolute_path)

from vocabulary_quiz_app.app import VocabularyQuizApp


import tkinter as tk

from vocabulary_quiz_app.app import VocabularyQuizApp
from vocabulary_quiz_app.data import WORDS


def main() -> int:
    root = tk.Tk()
    VocabularyQuizApp(root, WORDS)
    root.mainloop()
    return 0


if __name__ == "__main__":
    main()
