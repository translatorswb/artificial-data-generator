import sys
import json
import re
import random
import string
import argparse

def generate_id_string():
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits  # You can customize this as needed
    
    # Generate a random string of length 3
    random_string = ''.join(random.choice(characters) for _ in range(3))
    
    return random_string


def convert_annotation_to_json(input_file):
    annotations = []

    with open(input_file, 'r') as file:
        for line in file:
            parts = re.split(r'(\[.*?\])', line.strip())
            entities = []
            text_cursor = 0
            label_start = None  # Initialize label here
            label_end = None
            sentence_text = ""
            labeled_text = ""
            label = None
        
            for part in parts:
                if part.startswith("[") and part.endswith("]"):
                    if not part.startswith("[/"):
                        label = part[1:-1]
                        label_start = text_cursor
                    else:
                        label_end=True
                        label_end = text_cursor
                else:
                    sentence_text += part
                    if label:
                        labeled_text += part
                    text_cursor += len(part)
                    
                if label_end:
                    entities.append({
                        "id": generate_id_string(),
                        "from_name": "label",
                        "to_name": "text",
                        "type": "labels",
                        "value": {
                            "start": label_start,
                            "end": label_end,
                            "score": 0.70,
                            "text": labeled_text,
                            "labels": [label]
                        }
                        
                    })
                    labeled_text = ""
                    label_end = False
                    label = None

            data = {
                "data": {
                    "text": sentence_text
                },
                "predictions": [
                    {
                        "model_version": "v1",
                        "score": 0.5,
                        "result": entities
                    }
                ]
            }
            annotations.append(data)

    return annotations

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert annotation to JSON.")
    parser.add_argument('-i', help='Input file', required=True)
    parser.add_argument('-o', help='Output file', default='output.json')

    args = parser.parse_args()

    input_file = args.i
    output_file = args.o

    output_data = convert_annotation_to_json(input_file)

    with open(output_file, 'w') as outfile:
        json.dump(output_data, outfile, indent=2)
