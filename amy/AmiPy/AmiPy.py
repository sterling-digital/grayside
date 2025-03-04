import AmiPy
import numpy as np

def HelloWorld(fullName, strHere, BBPy):
    # Use fullName in the file path
    file_path = fr"C:\Users\mike\Documents\AmiPy-Dump\{fullName}.txt"

    # Check if strHere is a list or a NumPy array and convert it to a string
    if isinstance(BBPy, (list, np.ndarray)):
        BBPy = '\n'.join(map(str, BBPy))  # Convert each element to a string and join with newline characters

    # Open the file in write mode ('w')
    with open(file_path, "w") as file:
        # Write text into the file
        file.write(f"Name:\n{fullName}\n...\n")
        file.write(BBPy)
        file.write("\nEND.\n")

    print(f"File '{file_path}' has been created and text has been written to it.")
    return strHere
