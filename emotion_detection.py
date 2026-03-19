import requests

def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP Emotion Predict function and returns the response.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the API
    response = requests.post(url, json=input_json, headers=headers)
    
    # Return the text attribute of the response object
    return response.text