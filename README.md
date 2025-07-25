# Base Blue Converter

A Python script that converts images to base blue-tone compositions.

default
![megumi](./images/megumi.jpg "Megumi")

based
![megumi_based](./images/megumi_based.jpg "Megumi based")

monochrome
![megumi_based_monochrome](./images/megumi_based_monochrome.jpg "Megumi based monochrome")

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
python blue_converter.py input.jpg -m enhance     # Blue channel enhancement
python blue_converter.py input.jpg -m filter      # HSV color space filter
python blue_converter.py input.jpg -m monochrome  # Blue and white monochrome
python blue_converter.py input.jpg -m both        # Apply both methods (default)
```

## Features

- Blue channel enhancement and red/green channel reduction
- Hue shifting in HSV color space
- Blue and white monochrome conversion
- Single file or batch directory processing
- Support for major image formats (JPG, PNG, BMP, etc.)

## Conversion Methods

- **enhance**: Enhance blue channel and reduce red/green channels
- **filter**: Shift hue towards blue in HSV color space
- **monochrome**: Convert to blue and white monochrome (dark areas become blue, light areas become white)
- **both**: Combine enhance and filter methods (recommended)
