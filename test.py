import time
import requests

# replace your vercel domain
base_url = 'http://localhost:3000'


def custom_generate_audio(payload):
    url = f"{base_url}/api/custom_generate"
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    return response.json()


def extend_audio(payload):
    url = f"{base_url}/api/extend_audio"
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    return response.json()

def generate_audio_by_prompt(payload):
    url = f"{base_url}/api/generate"
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    return response.json()

def get_all_audio_information():
    url = f"{base_url}/api/get"
    response = requests.get(url)
    return response.json()

def get_audio_information(audio_ids):
    url = f"{base_url}/api/get?ids={audio_ids}"
    response = requests.get(url)
    return response.json()


def get_quota_information():
    url = f"{base_url}/api/get_limit"
    response = requests.get(url)
    return response.json()

def get_clip(clip_id):
    url = f"{base_url}/api/clip?id={clip_id}"
    response = requests.get(url)
    return response.json()

def generate_whole_song(clip_id):
    payload = {"clip_id": clip_id}
    url = f"{base_url}/api/concat"
    response = requests.post(url, json=payload)
    return response.json()

def download_audio(url, filename='test.mp3'):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def generate_lyrics(prompt):
    payload = {"prompt": prompt}
    url = f"{base_url}/api/generate_lyrics"
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == '__main__':
    # # To generate audio by prompt
    # data = generate_audio_by_prompt({
    #     "prompt": "A popular heavy metal song about war, sung by a deep-voiced male singer, slowly and melodiously. The lyrics depict the sorrow of people after math exams.",
    #     "make_instrumental": False,
    #     "wait_audio": False
    # })
    
    # # After the generation is complete. Suno Generates an audio id (different from the one returned by generation).
    # # To download all audios under the user, first fetch add the audio info.
    # all_audio_info = get_all_audio_information()
    # for line in all_audio_info:
    #     id = line['id']
    #     mp3_url = f'https://cdn1.suno.ai/{id}.mp3'
    #     download_audio(mp3_url, f'{id}.mp3')

    out = generate_lyrics('a cool song')
    print(out)
