# FxTwitter Link Converter

A lightweight keyboard interface to simplify the use of [FxTwitter](https://github.com/FixTweet/FxTwitter). It automatically converts `x.com` links into `fxtwitter.com` links for better embed support (Discord, etc.) — no manual editing required.

## How it works

The script listens globally for keyboard shortcuts. When triggered, it reads the clipboard content, transforms the URL, copies the result back to the clipboard, and logs the operation to a file.

## Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+X` | Convert the `x.com` link in clipboard to `fxtwitter.com` |
| `Ctrl+H` | Copy the full conversion history to the clipboard |
| `Ctrl+Q` | Stop the program |

## Example

```
Input  → https://x.com/user/status/123456789
Output → [ 2026-01-01 12:00:00 - [user](<https://x.com/user>) - https://fxtwitter.com/user/status/123456789/fr ]
```

The converted link is automatically formatted for Discord embeds: it includes the timestamp, a clickable mention of the account, and the FxTwitter link — all wrapped in brackets, ready to paste.

## Project structure

```
├── main.py
├── save_output.txt          # Auto-generated log file
├── un_authorized_account.json  # List of blocked accounts
└── libCore/
    ├── util_class.py        # Utility helpers (file I/O, error handling)
    └── output_file_class.py # Handles logging of converted links
```

## Configuration

In `main.py`, you can change the language suffix appended to the converted URL:

```python
code_country = "fr"  # Change to your country code, e.g. "en", "de", "es"
```

## Unauthorized accounts

You can block specific accounts from being converted by adding them to `un_authorized_account.json`:

```json
[
  {"name_account": "example_user", "reason": "reason for blocking"}
]
```

If you attempt to convert a link from a blocked account, the program will:
- Print a warning message in the console
- Copy the warning message to the clipboard instead of the converted link
- **Not** log the attempt to `save_output.txt`

## Log output

Every successful conversion is appended to `save_output.txt` in the following format:

```
{'date_time': '2024-01-01 12:00:00', 'account': 'user', 'link_account': 'https://x.com/user', 'id_post': '123456789', 'original_link': 'https://x.com/user/status/123456789', 'new_formated_link': 'https://fxtwitter.com/user/status/123456789/fr'}
```

You can retrieve the full history at any time by pressing `Ctrl+H`, which copies the entire content of `save_output.txt` to your clipboard.

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

## Documentation FxTwitter

To learn more about FxTwitter options and features:
https://docs.fxtwitter.com/en/latest/