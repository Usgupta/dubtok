import sys
import requests

def post_test():
    headers = {
        # requests won't add a boundary if this header is set when you pass files=
        # 'Content-Type': 'multipart/form-data',
    }

    files = {
        'file': open('../../sample_videos/cx.mp4', 'rb'),
        'dub_type': (None, 'English'),
    }

    # response = requests.post('https://dubtok-production.up.railway.app/upload/', headers=headers, files=files)
    # response = requests.post('http://0.0.0.0:9090/upload/', headers=headers, files=files)
    response = requests.post('http://127.0.0.1:8000/upload/', headers=headers, files=files)


    return response

def get_test(video_id):
    # response = requests.get(f'https://dubtok-production.up.railway.app/videos/{video_id}')
    response = requests.get(f'http://127.0.0.1:8000/videos/{video_id}')
    # response = requests.get(f'http://0.0.0.0:9090/videos/{video_id}')

    return response
        
if __name__ == '__main__':
    post_result = post_test()
    if post_result.status_code == 200:
        post_result = post_result.json()
    else:
        print(post_result.reason)
        sys.exit(1)
    
    video_id = post_result['video_id']
    filename = post_result['filename']
    upload_date = post_result['upload_date']        
            
    get_result = get_test(video_id)
    if get_result.status_code == 200:
        get_result = get_result.json()
        print(f"The retrieved video id is {video_id}: {video_id == get_result['video_id']}")
        print(f"The retrieved filename is {filename}: {filename == get_result['filename']}")
        print(f"The retrieved video id is {upload_date}: {upload_date == get_result['upload_date']}")

    else:
        print(get_result.reason)
        sys.exit(1)