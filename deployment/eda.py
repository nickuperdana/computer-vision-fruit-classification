import streamlit as st

def run():
    st.image('https://static.vecteezy.com/system/resources/thumbnails/025/868/984/small/freshy-various-fruits-for-summer-background-summer-festive-time-concept-generative-ai-free-photo.jpeg', use_column_width=True)
    st.markdown('# Fruit Classification Using Artificial Neural Network Modeling')
    st.markdown('This is a fun project to create a model that lets the computer predict a given image and classify it into any predetermined class upon this model development.')
    st.markdown('This model allows you to upload and predict images into any of these classes:\n- Apple\n- Banana\n- Grape\n- Mango\n- Strawberry')
    st.markdown('Image credit: Vecteezy')
    st.markdown('---')
    
    st.markdown('# Exploratory Data Analysis')
    st.markdown('This section provides a brief introduction to the dataset used for model construction in the background process.')
    st.markdown('---')
    st.markdown('## Link to the Main Dataset')
    st.markdown('You can obtain the dataset via this [link](https://www.kaggle.com/datasets/utkarshsaxenadn/fruits-classification/download?datasetVersionNumber=1)')
    st.markdown('---')
    st.markdown('## Sample Images from Train-set')
    st.markdown('Here are several images used for model training:')
    st.image('output_eda_train.png')
    st.markdown('Description: The training dataset includes three types of images:\n- Straightforward images focusing on a single fruit\n- Fruits with relevant backgrounds\n- Fruits with context and zoomed-out backgrounds, showing a wider environment')
    st.markdown('---')
    st.markdown('## Sample Images from Validation-set')
    st.markdown('Here are several images used for model validation:')
    st.image('output_eda_valid.png')
    st.markdown('Description: The validation dataset includes three types of images, similar to those in the training set. Images in the validation set inherit characteristics from the training set.')

    st.markdown('---')
    st.markdown('Managed by: Nicku R. Perdana | [LinkedIn](https://www.linkedin.com/in/nickurendyperdana/) | [Github](https://github.com/nickuperdana)')
    
if __name__ == '__main__':
    run()