from .db_functions import populate, find_and_rag
import secrets
import logging as log
import weaviate

class queryVectorDB():
    """
    Class for the vector database
    """
    def __init__(self):
        self.client = self.start()

    def start(self):
        """
        Start the client

        Args:
            endpoint(str): URL endpoint for where the weaviate instance is
        
        Returns:
            weaviate.Client

        Example:
            start("http://localhost:8080")
        """
        try:
            client = weaviate.Client(
            url = secrets.WEAVIATE_URL,  
            auth_client_secret=weaviate.auth.AuthApiKey(api_key=secrets.WEAVIATE_AUTH_KEY),  
            additional_headers = {
            "X-Cohere-Api-Key": secrets.COHERE_API_KEY
            }
        )
            log.info('client created')
            return client
        except Exception as E:
            log.error('client cannot be created')
            print("Client not connected!")
            return 
        
    
    def get_data(self, query:str):
        """
        Retrieve data from the weaviate schema based on the query
        Returned data is the entire content

        """
        concept = query
        client = self.client
        classname = 'CodeDocv4'

        log.info('finding code and explanation')
        concept =  ["code for shopping list"]

        try:
            explanation_pseudo, code = find_and_rag(concept, client, classname = classname)
            result = {'exp_pseudo': explanation_pseudo,
                      'code': code}

        except:
            log.error('Error generating code and explanation')

        return result
    