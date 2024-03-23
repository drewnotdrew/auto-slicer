# Auto Slicer

A small tool for slicing a folder of 3D models using Slic3r or its derivatives.
Files are sliced one at a time, and as such are not grouped into plates.

## Quick Start

Clone this repository:

```
git clone git@github.com:drewnotdrew/auto-slicer.git
```

Ensure your slicer is added to `PATH`:

```
$ superslicer --help

SuperSlicer_2.4.58.5_2022-09-23 based on Slic3r (with GUI support)
https://github.com/supermerill/SuperSlicer
...
```

Set various parameters in `config.ini`:

```
[auto-slicer]
in: ./in/
out: ./out/
rotate: 0,90,0
profile: ./config/profile.ini
filament: ./config/filament.ini
printer: ./config/printer/ini
delete_in: true
```

Run `./auto-slicer.py` from the root directory:

```
python ./auto-slicer.py
```

## Compatibility

Tested with:

- Python 3.10.12
- SuperSlicer 2.4.58.5
