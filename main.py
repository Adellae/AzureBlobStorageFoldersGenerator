import logging
from azure.storage.blob import BlobServiceClient, ContainerClient
from config import account_name, account_key, container_name, folder_names_list

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create a BlobServiceClient
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

# Create a ContainerClient
container_client = blob_service_client.get_container_client(container_name)

for name in folder_names_list:
    try:

        # Use the container_client to create a blob with the name as a pseudo-directory
        blob_name = f"{name}/uniqueDummyTextFile.txt"  # This simulates a "folder"
        blob_client = container_client.get_blob_client(blob_name)
        
        # Create an empty blob to simulate a folder
        blob_client.upload_blob(b"", overwrite=True)

        # Delete the dummy txt file
        blob_client.delete_blob()

        logging.info(f"Folder '{name}' created in Azure Blob Storage.")

    except Exception as e:
        logging.error(f"An error occurred while processing folder '{name}': {str(e)}")

logging.info("Script execution completed.")