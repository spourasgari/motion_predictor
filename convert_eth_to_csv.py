import os

# Define the input and output file names
input_file = "/home/sina/env_prediction_project/motion_predictor/ETH_datasets/x_raw_files/students003.txt" 
output_file = os.path.splitext(input_file)[0] + ".csv"  # Same name but with .csv extension

# Open the input file and read its content
with open(input_file, "r") as infile:
    lines = infile.readlines()

# Open the output file for writing
with open(output_file, "w") as outfile:
    # Write the header
    outfile.write("timestamp,ped_id,x,y\n")
    
    # Process each line from the input file
    for line in lines:
        # Replace tabs with commas
        csv_line = line.strip().replace("\t", ",")
        # Write the converted line to the output file
        outfile.write(csv_line + "\n")

print(f"File converted and saved as {output_file}")