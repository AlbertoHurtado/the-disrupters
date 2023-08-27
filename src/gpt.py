import os
from dotenv import load_dotenv
load_dotenv()

######################################################################################################
# In this section, we set the user authentication, user and app ID, model details, and the URL of
# the text we want as an input. Change these strings to run your own example.
######################################################################################################

# Your PAT (Personal Access Token) can be found in the portal under Authentification
PAT = os.getenv("CLARIFY_PERSONAL_ACCESS_TOKEN")
# Specify the correct user_id/app_id pairings
# Since you're making inferences outside your app's scope
USER_ID = 'openai'
APP_ID = 'chat-completion'
# Change these to whatever model and text URL you want to use
MODEL_ID = 'GPT-3_5-turbo'
MODEL_VERSION_ID = '8ea3880d08a74dc0b39500b99dfaa376'

############################################################################
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE TO RUN THIS EXAMPLE
############################################################################

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2


# PROMPTS
get_intent_prompt_gpt = """
I am building an intent detector for a chatbot that help users find real estate offerings. Here are the possible options for the intent:
user_neutral_greeting
user_neutral_goodbye
user_search_properties
user_neutral_out_of_scope

What would be the right intent for this input:
“{prompt}”

Please only return the intent and nothing else. Make your answer as short as possible.
"""

def get_intent_gpt(msg):
    return get_gpt_answer(get_intent_prompt_gpt.format(prompt=msg))

def get_gpt_answer(msg):
    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,  # The userDataObject is created in the overview and is required when using a PAT
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,  # This is optional. Defaults to the latest model version
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(
                            raw=msg
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception(f"Post model outputs failed, status: {post_model_outputs_response.status.description}")

    # Since we have one input, one output will exist here
    output = post_model_outputs_response.outputs[0]

    print("Completion:\n")
    print(output.data.text.raw)

    return output.data.text.raw
