# Base Blue Converter

A Python script that converts images to base blue-tone compositions.

![megumi](./images/megumi.jpg "Megumi") ![megumi_based](./images/megumi_based.jpg "Megumi based")

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Single Image Conversion
```bash
python blue_converter.py input.jpg
```

### Specify Output Path
```bash
python blue_converter.py input.jpg -o output_blue.jpg
```

### Convert All Images in Directory
```bash
python blue_converter.py /path/to/images/
```

### Select Conversion Method
```bash
python blue_converter.py input.jpg -m enhance  # Blue channel enhancement
python blue_converter.py input.jpg -m filter   # HSV color space filter
python blue_converter.py input.jpg -m both     # Apply both methods (default)
```

## Features

- Blue channel enhancement and red/green channel reduction
- Hue shifting in HSV color space
- Single file or batch directory processing
- Support for major image formats (JPG, PNG, BMP, etc.)

## Conversion Methods

- **enhance**: Enhance blue channel and reduce red/green channels
- **filter**: Shift hue towards blue in HSV color space
- **both**: Combine both methods above (recommended)
