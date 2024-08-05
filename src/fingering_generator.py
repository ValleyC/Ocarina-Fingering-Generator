import os
from PIL import Image, ImageDraw, ImageFont  # Import ImageDraw and ImageFont

# Define the mappings for all keys
note_mappings = {
    'G': {
        '-2': './images/G/G-2.png',
        '#-2': './images/G/G#-2.png',
        'b-3': './images/G/G#-2.png',  # Equivalent to #-2
        '-3': './images/G/G-3.png',
        '-4': './images/G/G-4.png',
        '#-4': './images/G/G#-4.png',
        'b-5': './images/G/G#-4.png',  # Equivalent to #-4
        '-5': './images/G/G-5.png',
        '#-5': './images/G/G#-5.png',
        'b-6': './images/G/G#-5.png',  # Equivalent to #-5
        '-6': './images/G/G-6.png',
        '#-6': './images/G/G#-6.png',
        'b-7': './images/G/G#-6.png',  # Equivalent to #-6
        '-7': './images/G/G-7.png',
        '1': './images/G/G1.png',
        '#1': './images/G/G#1.png',
        'b2': './images/G/G#1.png',  # Equivalent to #1
        '2': './images/G/G2.png',
        '#2': './images/G/G#2.png',
        'b3': './images/G/G#2.png',  # Equivalent to #2
        '3': './images/G/G3.png',
        '4': './images/G/G4.png',
        '#4': './images/G/G#4.png',
        'b5': './images/G/G#4.png',  # Equivalent to #4
        '5': './images/G/G5.png',
        '#5': './images/G/G#5.png',
        'b6': './images/G/G#5.png',  # Equivalent to #5
        '6': './images/G/G6.png',
        '#6': './images/G/G#6.png',
    },
    # Add mappings for other keys similarly
    'C': {
        '#+1': './images/C/C#+1.png',
        '#+2': './images/C/C#+2.png',
        '#-6': './images/C/C#-6.png',
        '#1': './images/C/C#1.png',
        '#2': './images/C/C#2.png',
        '#4': './images/C/C#4.png',
        '#5': './images/C/C#5.png',
        '#6': './images/C/C#6.png',
        '+1': './images/C/C+1.png',
        '+2': './images/C/C+2.png',
        '+3': './images/C/C+3.png',
        '+4': './images/C/C+4.png',
        '-6': './images/C/C-6.png',
        '-7': './images/C/C-7.png',
        '1': './images/C/C1.png',
        '2': './images/C/C2.png',
        '3': './images/C/C3.png',
        '4': './images/C/C4.png',
        '5': './images/C/C5.png',
        '6': './images/C/C6.png',
        '7': './images/C/C7.png',
        'b+2': './images/C/C#+1.png',
        'b+3': './images/C/C#+2.png',
        'b-7': './images/C/C#-6.png',
        'b2': './images/C/C#1.png',
        'b3': './images/C/C#2.png',
        'b5': './images/C/C#4.png',
        'b6': './images/C/C#5.png',
        'b7': './images/C/C#6.png',
    },
    'D': {
        '#+1': './images/D/D#+1.png',
        '#+2': './images/D/D#+2.png',
        '#-5': './images/D/D#-5.png',
        '#-6': './images/D/D#-6.png',
        '#1': './images/D/D#1.png',
        '#2': './images/D/D#2.png',
        '#4': './images/D/D#4.png',
        '#5': './images/D/D#5.png',
        '#6': './images/D/D#6.png',
        '+1': './images/D/D+1.png',
        '+2': './images/D/D+2.png',
        '-5': './images/D/D-5.png',
        '-6': './images/D/D-6.png',
        '-7': './images/D/D-7.png',
        '1': './images/D/D1.png',
        '2': './images/D/D2.png',
        '3': './images/D/D3.png',
        '4': './images/D/D4.png',
        '5': './images/D/D5.png',
        '6': './images/D/D6.png',
        '7': './images/D/D7.png',
        'b+2': './images/D/D#+1.png',
        'b+3': './images/D/D#+2.png',
        'b-6': './images/D/D#-5.png',
        'b-7': './images/D/D#-6.png',
        'b2': './images/D/D#1.png',
        'b3': './images/D/D#2.png',
        'b5': './images/D/D#4.png',
        'b6': './images/D/D#5.png',
        'b7': './images/D/D#6.png',
    },
    'F': {
        '#-4': './images/F/F#-4.png',
        '#-5': './images/F/F#-5.png',
        '#-6': './images/F/F#-6.png',
        '#1': './images/F/F#1.png',
        '#2': './images/F/F#2.png',
        '#4': './images/F/F#4.png',
        '#5': './images/F/F#5.png',
        '#6': './images/F/F#6.png',
        '+1': './images/F/F+1.png',
        '-3': './images/F/F-3.png',
        '-4': './images/F/F-4.png',
        '-5': './images/F/F-5.png',
        '-6': './images/F/F-6.png',
        '-7': './images/F/F-7.png',
        '1': './images/F/F1.png',
        '2': './images/F/F2.png',
        '3': './images/F/F3.png',
        '4': './images/F/F4.png',
        '5': './images/F/F5.png',
        '6': './images/F/F6.png',
        '7': './images/F/F7.png',
        'b-5': './images/F/F#-4.png',
        'b-6': './images/F/F#-5.png',
        'b-7': './images/F/F#-6.png',
        'b2': './images/F/F#1.png',
        'b3': './images/F/F#2.png',
        'b5': './images/F/F#4.png',
        'b6': './images/F/F#5.png',
        'b7': './images/F/F#6.png',
    },
    'A': {
        '#+1': './images/A/A#+1.png',
        '#+2': './images/A/A#+2.png',
        '#+4': './images/A/A#+4.png',
        '#+5': './images/A/A#+5.png',
        '#1': './images/A/A#1.png',
        '#2': './images/A/A#2.png',
        '#4': './images/A/A#4.png',
        '#5': './images/A/A#5.png',
        '#6': './images/A/A#6.png',
        '+1': './images/A/A+1.png',
        '+2': './images/A/A+2.png',
        '+3': './images/A/A+3.png',
        '+4': './images/A/A+4.png',
        '+5': './images/A/A+5.png',
        '1': './images/A/A1.png',
        '2': './images/A/A2.png',
        '3': './images/A/A3.png',
        '4': './images/A/A4.png',
        '5': './images/A/A5.png',
        '6': './images/A/A6.png',
        '7': './images/A/A7.png',
        'b+2': './images/A/A#+1.png',
        'b+3': './images/A/A#+2.png',
        'b+5': './images/A/A#+4.png',
        'b+6': './images/A/A#+5.png',
        'b2': './images/A/A#1.png',
        'b3': './images/A/A#2.png',
        'b5': './images/A/A#4.png',
        'b6': './images/A/A#5.png',
        'b7': './images/A/A#6.png',
    },
    'bB': {
        '#+1': './images/bB/bB#+1.png',
        '#+2': './images/bB/bB#+2.png',
        '#+4': './images/bB/bB#+4.png',
        '#1': './images/bB/bB#1.png',
        '#2': './images/bB/bB#2.png',
        '#4': './images/bB/bB#4.png',
        '#5': './images/bB/bB#5.png',
        '#6': './images/bB/bB#6.png',
        '+1': './images/bB/bB+1.png',
        '+2': './images/bB/bB+2.png',
        '+3': './images/bB/bB+3.png',
        '+4': './images/bB/bB+4.png',
        '+5': './images/bB/bB+5.png',
        '-7': './images/bB/bB-7.png',
        '1': './images/bB/bB1.png',
        '2': './images/bB/bB2.png',
        '3': './images/bB/bB3.png',
        '4': './images/bB/bB4.png',
        '5': './images/bB/bB5.png',
        '6': './images/bB/bB6.png',
        '7': './images/bB/bB7.png',
        'b+2': './images/bB/bB#+1.png',
        'b+3': './images/bB/bB#+2.png',
        'b+5': './images/bB/bB#+4.png',
        'b2': './images/bB/bB#1.png',
        'b3': './images/bB/bB#2.png',
        'b5': './images/bB/bB#4.png',
        'b6': './images/bB/bB#5.png',
        'b7': './images/bB/bB#6.png',
    },
    'bE': {
        '#+1': './images/bE/bE#+1.png',
        '#-4': './images/bE/bE#-4.png',
        '#-5': './images/bE/bE#-5.png',
        '#-6': './images/bE/bE#-6.png',
        '#1': './images/bE/bE#1.png',
        '#2': './images/bE/bE#2.png',
        '#4': './images/bE/bE#4.png',
        '#5': './images/bE/bE#5.png',
        '#6': './images/bE/bE#6.png',
        '+1': './images/bE/bE+1.png',
        '+2': './images/bE/bE+2.png',
        '-5': './images/bE/bE-5.png',
        '-6': './images/bE/bE-6.png',
        '-7': './images/bE/bE-7.png',
        '1': './images/bE/bE1.png',
        '2': './images/bE/bE2.png',
        '3': './images/bE/bE3.png',
        '4': './images/bE/bE4.png',
        '5': './images/bE/bE5.png',
        '6': './images/bE/bE6.png',
        '7': './images/bE/bE7.png',
        'b+2': './images/bE/bE#+1.png',
        'b-5': './images/bE/bE#-4.png',
        'b-6': './images/bE/bE#-5.png',
        'b-7': './images/bE/bE#-6.png',
        'b2': './images/bE/bE#1.png',
        'b3': './images/bE/bE#2.png',
        'b5': './images/bE/bE#4.png',
        'b6': './images/bE/bE#5.png',
        'b7': './images/bE/bE#6.png',
    }
}

def generate_fingering_sequence_multi_line(note_sequences, key, output_path="output_multi_line.png"):
    if key not in note_mappings:
        print(f"Invalid key: {key}")
        return None

    key_note_mapping = note_mappings[key]
    rows = []

    for note_sequence in note_sequences:
        images = []
        labels = []
        for note in note_sequence:
            image_path = key_note_mapping.get(note)
            if image_path and os.path.exists(image_path):
                img = Image.open(image_path)
                images.append(img)
                labels.append(note)
            else:
                print(f"Note {note} does not have an associated image or the image file does not exist.")
        
        if images:
            # Combine images horizontally for this line
            widths, heights = zip(*(i.size for i in images))
            total_width = sum(widths)
            max_height = max(heights)

            combined_row = Image.new('RGB', (total_width, max_height + 30))  # Add space for labels

            # Paste images in a row
            x_offset = 0
            for img in images:
                combined_row.paste(img, (x_offset, 0))
                x_offset += img.width

            # Add labels below images
            draw = ImageDraw.Draw(combined_row)
            font = ImageFont.load_default()  # Use a simple default font
            x_offset = 0
            for i, label in enumerate(labels):
                text_width, text_height = draw.textsize(label, font=font)
                text_x = x_offset + (images[i].width - text_width) // 2
                text_y = max_height + 5
                draw.text((text_x, text_y), label, font=font, fill="black")
                x_offset += images[i].width

            rows.append(combined_row)

    if not rows:
        print("No valid rows were found.")
        return None
    
    # Combine rows vertically
    total_height = sum(row.size[1] for row in rows)
    max_width = max(row.size[0] for row in rows)

    final_image = Image.new('RGB', (max_width, total_height))

    y_offset = 0
    for row in rows:
        final_image.paste(row, (0, y_offset))
        y_offset += row.size[1]

    final_image.save(output_path)
    return output_path

# if __name__ == "__main__":
#     # For testing purposes
#     test_input = [['-2', '3', '4', '#5', '6'], ['1', '2', '#4', '5', '#6']]
#     generate_fingering_sequence_multi_line(test_input, 'G')
