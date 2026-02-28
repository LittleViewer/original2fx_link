# FxTwitter Link Converter

A lightweight keyboard interface to simplify the use of [FxTwitter](https://github.com/FixTweet/FxTwitter). It automatically converts `x.com` links into `fxtwitter.com` links for better embed support (Discord, etc.) — no manual editing required.

## How it works

The script listens globally for keyboard shortcuts. When triggered, it reads the clipboard content, transforms the URL, copies the result back to the clipboard, and logs the operation to a file.

## Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+X` | Convert the `x.com` link in clipboard to `fxtwitter.com` |
| `Ctrl+Q` | Stop the program |

## Example

```
Input  → https://x.com/user/status/123456789
Output → https://fxtwitter.com/user/status/123456789/fr
```

## Project structure

```
├── main.py
├── save_output.txt          # Auto-generated log file
└── libCore/
    ├── util_class.py        # Utility helpers (file I/O, error handling)
    └── output_file_class.py # Handles logging of converted links
```

## Configuration

In `main.py`, you can change the language suffix appended to the converted URL:

```python
code_country = "fr"  # Change to your country code, e.g. "en", "de", "es"
```

## Dependencies

```
keyboard
pyperclip
```

Install them with:

```bash
pip install keyboard pyperclip
```

> **Note:** The `keyboard` library may require administrator/root privileges to listen to global hotkeys.

## Log output

Every successful conversion is appended to `save_output.txt` in the following format:

```
{'date_time': '2024-01-01 12:00:00', 'original_link': 'https://x.com/...', 'new_formated_link': 'https://fxtwitter.com/.../fr'}
```

## Documentation FxTwitter

Pour en savoir plus sur les options et fonctionnalités de FxTwitter :
https://docs.fxtwitter.com/en/latest/

