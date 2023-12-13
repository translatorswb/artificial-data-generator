# Artificial text data creation and annotation

## Data generator

Randomly generates values for placeholders in text. 

```
usage: data_generator.py [-h] -source SOURCE -output OUTPUT -names NAMES
                         -surnames SURNAMES -places PLACES [-keeptag]

Process data files.

optional arguments:
  -h, --help            show this help message and exit
  -source SOURCE, -s SOURCE
                        Source data file
  -output OUTPUT, -o OUTPUT
                        Modified data file
  -names NAMES, -n NAMES
                        Names file
  -surnames SURNAMES, -r SURNAMES
                        Surnames file
  -places PLACES, -p PLACES
                        Placenames file
  -keeptag, -t          Maintain tags in XML form
```

### Sample usage for Kanuri

```
python data_generator.py -s in/kanuri-src.txt -o out/kanuri-tagreplaced.txt -n kanuri/kanuri_names.txt -r kanuri/kanuri_surnames.txt -p kanuri/kanuri_placenames.txt
```

### Sample usage for Hausa

```
python data_generator.py -s in/hausa-src.txt -o out/hausa-tagreplaced.txt -n hausa/hausa_names.txt -r hausa/hausa_surnames.txt -p hausa/hausa_placenames.txt
```

## Label studio annotation file creator

Creates a JSON format file to load in label studio. Places tags that are already there.

```
usage: annotation_to_json.py [-h] -i I [-o O]

Convert annotation to JSON.

optional arguments:
  -h, --help  show this help message and exit
  -i I        Input file
  -o O        Output file
```

### Sample usage for Hausa

```
python annotation_to_json.py -i out/hausa-tagreplaced.txt -o out/hausa-labelstudio.json
```

### Sample usage for Kanuri

```
python annotation_to_json.py -i out/kanuri-tagreplaced.txt -o out/kanuri-labelstudio.json
```