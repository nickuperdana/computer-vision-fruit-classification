import streamlit as st
import requests
import numpy as np
import cv2
import tensorflow as tf

model = tf.keras.models.load_model('cnn_model.h5')

def run():
    st.image('https://static.vecteezy.com/system/resources/thumbnails/025/868/984/small/freshy-various-fruits-for-summer-background-summer-festive-time-concept-generative-ai-free-photo.jpeg', use_column_width=True)
    st.markdown('# Fruit Classification Using Artificial Neural Network Modeling')
    st.markdown('This is a fun project to create a model that lets the computer predict a given image and classify it into any predetermined class upon this model development.')
    st.markdown('This model allows you to upload and predict images into any of these classes:\n- Apple\n- Banana\n- Grape\n- Mango\n- Strawberry')
    st.markdown('Image credit: Vecteezy')
    st.markdown('---')

    st.markdown("# Let's Predict An Image!")

    st.markdown('### Upload an Image.')
    uploadMethod = st.selectbox('Before we predict an image, choose an upload method first', ['Upload image', 'Send image URL'], index=None, placeholder='Select method...')
    
    try:  
        with st.form('MyForm'):
            if uploadMethod == 'Upload image':
                imgUpload = st.file_uploader('Upload your file here', type=['png', 'jpg', 'webp', 'jpeg'], accept_multiple_files=False)
                submit = st.form_submit_button('Start Predicting')
            elif uploadMethod == 'Send image URL':
                imgUrl = st.text_input('Enter URL', value=None, placeholder='URL...')
                # if inputUrl != None:
                #     st.markdown('Theploaded image:')
                #     st.image(inputUrl)
                submit = st.form_submit_button('Start Predicting')

        class_list = ['Apple', 'Banana', 'Grape', 'Melon', 'Strawberry']

        st.markdown('## Prediction Result:')
        if submit:
            if uploadMethod == 'Upload image':
                inf_img = cv2.imdecode(np.fromstring(imgUpload.read(), np.uint8), 1)
                inf_img_col = cv2.cvtColor(inf_img, cv2.COLOR_BGR2RGB)
                inf_prep_img = cv2.resize(inf_img_col, (400,400))
                inf_scal_img = inf_prep_img / 255.0
                inf_reshape = np.reshape(inf_scal_img, [1,400,400,3])
                class_img = model.predict(inf_reshape, verbose=0)
                confident_index = np.argmax(class_img)
                class_label = class_list[confident_index]
                listproba = list(class_img[0])
                st.markdown('You uploaded this image:')
                st.image(imgUpload, use_column_width=True)
                st.markdown(f'The model predicted the image given as a class of {class_label} with a probability of {listproba[confident_index]}.')
                st.markdown('Due to the current state of prediction accuracy, a significant occurence of misidentification is expected.')
            elif uploadMethod == 'Send image URL':
                if imgUrl == "":
                    pass
                else:
                    try:
                        response = requests.get(imgUrl)
                        if response.status_code == 200:
                            inf_url_img = cv2.imdecode(np.frombuffer(response.content, np.uint8), 1)
                            inf_img_url_col = cv2.cvtColor(inf_url_img, cv2.COLOR_RGB2BGR)
                            inf_prep_url_img = cv2.resize(inf_img_url_col, (400,400))
                            inf_scal_url_img = inf_prep_url_img / 255.0
                            inf_url_reshape = np.reshape(inf_scal_url_img, [1,400,400,3])
                            class_url_img = model.predict(inf_url_reshape, verbose=0)
                            confident_index_url = np.argmax(class_url_img)
                            class_url_label = class_list[confident_index_url]
                            listproba_url = list(class_url_img[0])
                            st.markdown('You uploaded this image:')
                            st.image(inf_img_url_col, use_column_width=True)
                            st.markdown(f'The model predicted the image given as a class of {class_url_label} with a probability of {listproba_url[confident_index_url]}.')
                            st.markdown('Due to the current state of prediction accuracy, a significant occurence of misidentification is expected.')
                            
                        else:
                            st.markdown("Unable to fetch image from the given URL. Please try again")
                            pass
                    except:
                        pass
    except:
        pass

if __name__ == '__main__':
    run()