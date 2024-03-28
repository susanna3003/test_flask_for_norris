## notes for this codespace

## trying to use autogen

# create venv
python -m venv env

# open venv
Windows: env\Scripts\activate

Mac: source env/bin/activate

# install flask
pip install flask

# install autogenstudio
pip install autogenstudio

# get API key from openai playground
use export OPENAI_API_KEY=<your key here>

# run autogenstudio
autogenstudio ui

Error occurred while processing message: api_key is not present in llm_config or OPENAI_API_KEY env variable for agent ** primary_assistant**. Update your workflow to provide an api_key to use the LLM.
use export OPENAI_API_KEY=<your key here>

Error occurred while processing message: Error code: 404 - {'error': {'message': 'The model `gpt-4-1106-preview` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'param': None, 'code': 'model_not_found'}}