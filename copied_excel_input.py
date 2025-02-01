import shutil

# Path to the source Excel file
source_file = r"C:\Users\adnan.alakori\PycharmProjects\critical-demand-model\Results computation.xlsx"

# Number of copies to create
num_copies = 220

# Starting number for sequential numbering
start_number = 60

# Iterate over the range with the specified start number
for i in range(start_number, start_number + num_copies):
    # Generate the destination file name with sequential number
    file_number = str(i).zfill(2)  # Zero-padding the number
    destination_file = f"Results computation_{file_number}.xlsx"

    # Copy the source file to the destination
    shutil.copyfile(source_file, destination_file)

    # Print the copied file name
    print(f"File {destination_file} copied.")
