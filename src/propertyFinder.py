import src.llama as llama
import src.dbService as dbService
import json

def suggestProperties(prompt):
    # TODO check if is a valid json
    stringifiedJson = llama.generate_response_llama(prompt)
    query = json.loads(stringifiedJson)
    print(query)
    # TODO check if it is null what happens
    myQuery = {'Location': query['location']}

    db = dbService.MongoDBService()
    propertiesFound = db.find_matches(myQuery)
    print(propertiesFound)
    # TODO improve db connection management and implement error handling
    db.close()

    count = len(propertiesFound)

    if count == 0:
        response = "I have not found any property matching your criteria"
    else:
        response = f"I have found {count} properties that match your criteria."
        
    # links = [item['Link'] for item in propertiesFound]
    # response = "I have found these properties which I think you will love: " + ", ".join(links)  if(links) else "I have not found any property matching your criteria"

    return response, propertiesFound
