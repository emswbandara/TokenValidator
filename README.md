# TokenValidator

Captures 401 error codes and relevant context information when validating the access tokens in WSO2 APIM.
 
Make the following changes before running the script.

    Deploy a mock API in APIM-Publisher.
    Subscribe to the published API from APIM-store.
    Replace the value of keyAndSecret variable with the Consumer Key and Consumer Secret of the new application. It should be in the format Consumer_Key:Consumer_Secret
        You can obtain the production keys from APIM-store -> Applications -> select the application created -> Production Keys
    Replace tokenEndpoint with your server's IP. eg : https://<SERVER_IP>:8243/token
    Replace testApi variable with the url of the mock API deployed in Publisher. eg: "http://10.100.8.2:8280/pizzashack/1.0.0/menu"

After making the above changes use the following command to run the program

> python TokenValidator.py

