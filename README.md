# TJA Title Swap

Small Python utility for swapping localized title and subtitle fields in `.tja` files. It is primarily used when preparing charts for ESE Project.

## Behavior

For each processed file, the script examines the first ten lines and swaps the first available field pair:

- `TITLE` ↔ `TITLEJA`, otherwise `TITLE` ↔ `TITLEZH`;
- `SUBTITLE` ↔ `SUBTITLEJA`, otherwise `SUBTITLE` ↔ `SUBTITLEZH`.

Files are read and written as UTF-8 with BOM (`utf-8-sig`). Existing chart data outside the matched header fields is left unchanged.

## Usage

Back up the target charts, then run:

```powershell
python .\modify_tja_files.py
```

Enter the directory containing the `.tja` files when prompted. Review the console output and compare the modified headers before using the charts.
