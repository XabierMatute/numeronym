# Numeronym

These programs convert words to numeronyms (e.g., "localization" → "l10n") and reverse them back to a masked format (e.g., "l10n" → "l________n"). They preserve spaces and punctuation.

## Motivation
This project was created for fun and as a critique of excessive abbreviations like "l10n" (localization) and "c8s" (containers), which can sometimes make text harder to read instead of simplifying it. While numeronyms are useful in some contexts, they can also make communication unnecessarily cryptic.

## Features
- Converts words into numeronyms by replacing the middle characters with their count.
- Reverts numeronyms back into a masked format to visualize their structure.
- Preserves spaces, punctuation, and formatting.
- Simple and lightweight, requiring only Python's built-in libraries.

## Usage
To convert words to numeronyms:
```sh
python numeronym.py "Hello localization world!"
# Output: H3o l10n w3d!
```

To reverse numeronyms:
```sh
python desnumeronym.py "H3o l10n w3d!"
# Output: H__o l________n w__d!
```

## Installation
No installation required. Just run the scripts using Python 3.

## Why This Matters
Abbreviations like "k8s" (Kubernetes) and "l10n" (localization) are widely used in tech communities, but they often make things harder to read for newcomers. This project playfully highlights how these abbreviations obscure meaning rather than clarify it.

## License
This project is free to use and modify.

## Contributions
Feel free to suggest improvements or add new features!

