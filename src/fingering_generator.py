import os
from PIL import Image, ImageDraw, ImageFont
from note_mappings import generate_note_mappings_for_key

def generate_fingering_sequence_multi_line(note_sequences, key, output_path="output_multi_line.png"):
    # Generate the note mappings for the selected key
    key_note_mapping = generate_note_mappings_for_key(key)
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
#     test_input = [['1', '2', '3', '4', '5'], ['6', '7', '-2', '-3', '-4']]
#     generate_fingering_sequence_multi_line(test_input, 'G')
