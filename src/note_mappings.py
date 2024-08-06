# Define the main sequence of notes
main_sequence = [
    '-2', '#-2', '-3', '-4', '#-4', '-5', '#-5', '-6', '#-6', '-7', 
    '1', '#1', '2', '#2', '3', '4', '#4', '5', '#5', '6', '#6', 
    '7', '+1', '#+1', '+2', '#+2', '+3', '+4', '#+4', '+5', '#+5'
]

# Define the starting index for each key in the main sequence
key_start_index = {
    'C': main_sequence.index('-6'),
    'F': main_sequence.index('-3'),
    'G': main_sequence.index('-2'),
    'A': main_sequence.index('1'),
    'D': main_sequence.index('-5'),
    'bB': main_sequence.index('-7'),
    'bE': main_sequence.index('#-4'),
}

# Function to generate the mapping for a specific key
def generate_note_mappings_for_key(key):
    start_index = key_start_index[key]
    # Slice the main sequence to get the 21 notes for the current key
    key_sequence = main_sequence[start_index:start_index + 21]

    # Map each note in the key sequence to the corresponding image
    note_mappings = {note: f'./src/{i+1}.png' for i, note in enumerate(key_sequence)}

    return note_mappings
