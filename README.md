# Azure Blob Storage Folder Creation Script
Overview
The Azure Blob Storage Folder Creation Script is a Python script designed to create pseudo-directories (simulated folders) in Azure Blob Storage. It utilizes the Azure Storage SDK for Python to interact with Azure Blob Storage.

## Configuration
The script relies on a configuration file (**config.py**) that contains the necessary information. Ensure the configuration file is correctly set up with the following parameters:

**account_name**: Azure Storage account name.
**account_key**: Azure Storage account key.
**container_name**: Azure Blob Storage container name.
**folder_names_list**: A list of folder names to be created in Azure Blob Storage.

## Script Logic
The script establishes a connection to the Azure Blob Storage account using the provided credentials.
It retrieves or creates the specified container in Azure Blob Storage.
For each folder name in the provided list (folder_names_list):
It simulates the creation of a folder by creating a unique dummy text file within that "folder."
The dummy text file is then deleted, leaving the "folder" structure intact.

### Error Handling
The script includes basic error handling to catch and log any exceptions that may occur during the execution. Errors are logged with appropriate error messages.

### Logging
The script utilizes the Python logging module to provide informational and error messages during execution. Log messages are printed to the console.
