import os

from dotenv import load_dotenv
load_dotenv()

# Your PAT (Personal Access Token) can be found in the portal under Authentification
PAT = os.getenv("CLARIFY_PERSONAL_ACCESS_TOKEN")
# Specify the correct user_id/app_id pairings
# Since you're making inferences outside your app's scope
USER_ID = 'tuchohackathon'
APP_ID = 'RECA-user-intent'
# Change these to whatever model and text URL you want to use
WORKFLOW_ID = os.getenv("WORKFLOW_ID")
# The index of the workflow block we want to use as output
WORKFLOW_INDEX = 1


from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)

metadata = (('authorization', 'Key ' + PAT),)

userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

def generate_response_llama(msg):

    post_workflow_results_response = stub.PostWorkflowResults(
    service_pb2.PostWorkflowResultsRequest(
        user_app_id=userDataObject,
        workflow_id=WORKFLOW_ID,
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
    if post_workflow_results_response.status.code != status_code_pb2.SUCCESS:
        print(post_workflow_results_response.status)
        raise Exception("Post workflow results failed, status: " + post_workflow_results_response.status.description)

    # We'll get one WorkflowResult for each input we used above. Because of one input, we have here one WorkflowResult
    results = post_workflow_results_response.results[0]


    return results.outputs[WORKFLOW_INDEX].data.text.raw
