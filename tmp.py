import os
import json

input_folder = "rap_dataset"
output_file = "rap_corpus.txt"

total_songs = 0
total_chars = 0

print(f"Starting merge: reading from '{input_folder}' -> writing to '{output_file}'\n")

# Open the master output file once
with open(output_file, "w", encoding="utf-8") as f_out:
    
    # Iterate through every JSON file in your dataset folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            filepath = os.path.join(input_folder, filename)
            
            try:
                with open(filepath, "r", encoding="utf-8") as f_in:
                    artist_data = json.load(f_in)
                    
                    # artist_data is a list of dictionaries based on your scraper
                    for song in artist_data:
                        lyrics = song.get("lyrics", "").strip()
                        
                        if lyrics:
                            # Write lyrics followed by a double newline to separate songs
                            f_out.write(lyrics + "\n\n")
                            
                            total_songs += 1
                            total_chars += len(lyrics)
                            
                print(f"Merged: {filename}")
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")

print("\n" + "-"*30)
print("Corpus Merge Complete!")
print("-"*30)
print(f"Total songs merged: {total_songs}")
print(f"Total characters:   {total_chars:,}")
print(f"Estimated words:    {total_chars // 5:,} (assuming ~5 chars per word)")
print(f"Output saved to:    {output_file}")