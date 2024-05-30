
def create_class(client, classname):
    class_obj = {
        "class": classname,
        "properties": [
            {
                "name": "output",
                "dataType": ["text"],
            },
            {
                "name": "instruction",
                "dataType": ["text"],
            },
        ],
        "vectorizer": "text2vec-cohere",  # set your vectorizer module
        "moduleConfig": {
            "generative-cohere": {
            "model": "command-xlarge-nightly", 
            }
    }
    }

    client.schema.create_class(class_obj)
    


def import_data(client,dataset, batch_size = 200,timeout_retries=3):

    client.batch.configure(
    batch_size=batch_size,
    dynamic=True,
    timeout_retries=timeout_retries,)

    counter=0

    def check_batch_result(results: dict):
        if results is not None:
            for result in results:
                if "result" in result and "errors" in result["result"]:
                    if "error" in result["result"]["errors"]:
                        print(result["result"])

    with client.batch as batch:
        for dictionary in dataset:        
            if (counter %5 == 0):
                print(f"Import {counter} ")

            properties = {
            "output": dictionary["output"] if dictionary["output"] else '',
            "instruction": dictionary["instruction"] if dictionary["instruction"] else '',
            }
            
            batch.add_data_object(properties, "CodeDoc")
            counter = counter+1
            if counter == 20: break
            
        print(f"Import {counter} / {len(dataset)}")
    print("Import complete")


def rag_function(concept, client):
    # instruction for the generative module
    generatePrompt = "explain {output} as if to a learner  and generate psedocode/algorithm for {output}"

    result = (
    client.query
    .get("CodeDoc", ["instruction", "output"])
    .with_generate(single_prompt=generatePrompt)
    .with_near_text({
        "concepts": concept #
    })
    .with_limit(1)
    ).do()

    explanation_pseudo = result['data']['Get']['CodeDoc'][0]['_additional']['generate']['singleResult']
    code = result['data']['Get']['CodeDoc'][0]['output']

    return explanation_pseudo, code



from datasets import load_dataset
import weaviate


if '__name__' == '__main__':
    dataset = load_dataset('flytech/python-codes-25k', split='train')
    print('loaded dataset')

    client = weaviate.Client(
        url = "https://weaviate-code-arg-e8eh4did.weaviate.network",  
        auth_client_secret=weaviate.auth.AuthApiKey(api_key="uhBe7uqF43N5douqKj50gWQGxtZIpWHHv48N"),  
        additional_headers = {
        "X-Cohere-Api-Key": "GJEKFhYN1dT2OLFAPTWP6Ig1IDfNduhseC8wxgPw"  
        }
    )
    print('client created')
    
    create_class(client, classname = "CodeDoc")
    import_data(client, dataset)
    print('data imported in collection')
    concept = ['code for phone usage check']
    print('finding code and explanation')
    explanation_pseudo, code = rag_function(concept)
    print(explanation_pseudo)
    print(code)
    