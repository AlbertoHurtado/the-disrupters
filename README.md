# the-disrupters
Hackathon project for the disrupters team for lablab llama2 clarifai hackathon

## Running the project locally
Start by cloning the project.
```
git clone https://github.com/AlbertoHurtado/the-disrupters.git
cd the-disrupters
```
Copy the .env.example file and rename the copy to .env and add all the necessary values.

Then create a python virtual environment using conda and instal the necessary packages.

```
conda create -n hackathon python=3.9
conda activate hackathon
pip install -r requirements.txt
```

Then, for the image carousel to work, install the node packages inside `frontend` directory : `npm i`

Then, build the node modules : `npm run build`

Then run the app.
```
streamlit run app.py
```