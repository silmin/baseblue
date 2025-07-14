#!/usr/bin/env python3

import cv2; print(cv2.__version__)
import numpy as np
import argparse
import os
from pathlib import Path

def convert_to_blue_tones(image):
    """
    Convert image to blue-toned composition by enhancing blue channel
    and reducing red/green channels
    """
    blue_image = image.copy()
    
    # Extract BGR channels
    b, g, r = cv2.split(blue_image)
    
    # Enhance blue channel
    b = cv2.addWeighted(b, 1.5, np.zeros_like(b), 0, 20)
    b = np.clip(b, 0, 255).astype(np.uint8)
    
    # Reduce red and green channels
    r = cv2.addWeighted(r, 0.3, np.zeros_like(r), 0, 0)
    g = cv2.addWeighted(g, 0.4, np.zeros_like(g), 0, 0)
    
    # Merge channels back
    blue_result = cv2.merge([b, g, r])
    
    return blue_result

def apply_blue_filter(image):
    """
    Apply blue color filter using HSV color space
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Shift hue towards blue (240 degrees = 120 in OpenCV)
    hsv[:, :, 0] = np.clip(hsv[:, :, 0] * 0.7 + 30, 0, 179)
    
    # Increase saturation for more vivid blue
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.3, 0, 255)
    
    # Convert back to BGR
    result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    return result

def process_image(input_path, output_path, method='enhance'):
    """
    Process single image and convert to blue tones
    """
    # Load image
    image = cv2.imread(input_path)
    if image is None:
        raise ValueError(f"Could not load image: {input_path}")
    
    # Apply blue conversion
    if method == 'enhance':
        result = convert_to_blue_tones(image)
    elif method == 'filter':
        result = apply_blue_filter(image)
    else:
        # Combine both methods
        temp = convert_to_blue_tones(image)
        result = apply_blue_filter(temp)
    
    # Save result
    cv2.imwrite(output_path, result)
    print(f"Converted: {input_path} -> {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Convert images to blue-toned compositions')
    parser.add_argument('input', help='Input image file or directory')
    parser.add_argument('-o', '--output', help='Output file or directory (default: adds _blue suffix)')
    parser.add_argument('-m', '--method', choices=['enhance', 'filter', 'both'], 
                       default='both', help='Conversion method (default: both)')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    
    if input_path.is_file():
        # Single file processing
        if args.output:
            output_path = args.output
        else:
            output_path = input_path.stem + '_based' + input_path.suffix
        
        process_image(str(input_path), output_path, args.method)
        
    elif input_path.is_dir():
        # Directory processing
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
        image_files = [f for f in input_path.iterdir() 
                      if f.suffix.lower() in image_extensions]
        
        if not image_files:
            print("No image files found in directory")
            return
        
        output_dir = Path(args.output) if args.output else input_path / 'blue_converted'
        output_dir.mkdir(exist_ok=True)
        
        for img_file in image_files:
            output_file = output_dir / (img_file.stem + '_blue' + img_file.suffix)
            try:
                process_image(str(img_file), str(output_file), args.method)
            except Exception as e:
                print(f"Error processing {img_file}: {e}")
    else:
        print(f"Error: {input_path} is not a valid file or directory")

if __name__ == '__main__':
    main()
