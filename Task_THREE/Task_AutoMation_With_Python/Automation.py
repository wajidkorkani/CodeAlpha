import os
import shutil

Zero = 0 # This is just a dummy variable to run while loop

# While loop starts from here
while Zero < 1:

    print("Enter stop to stop the process.")
    # Take repo path as input from the user
    path = input("Enter Path: ")


    try:
        # Stoper or breaker
        if path == "stop" or path == "Stop" or path == "STOP":
            break

        else:

            # Geting the list of files
            files = os.listdir(path)

            # Running for loop for each file in the directory
            for file in files:

                # Spliting the file name and extension
                filename, extension = os.path.splitext(file)
                extension = extension[1:]  # Removeing dot or . from the extension

                # Creating the source and destination paths
                source_path = os.path.join(path, file)
                destination_path = os.path.join(path, extension, file)

                # Checking if the destination path already exists
                if os.path.exists(destination_path):
                    # If it exists, move the file to the destination
                    shutil.move(source_path, destination_path)
                else:
                    # Checking if the destination path doesn't exist, create it
                    directory_path = os.path.join(path, extension)
                    if not os.path.exists(directory_path):
                        os.makedirs(directory_path)

                    # Moving the file to the destination
                    shutil.move(source_path, destination_path)
    except:
        print('Please enter a valid path')
