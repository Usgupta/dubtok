const uploadVideoFile = async (videoFile, dubType) => {
    const formData = new FormData();
    formData.append('file', videoFile);
    formData.append('dub_type', dubType); // Include the selected dub

    let result = null;

    try {
        const response = await fetch('http://127.0.0.1:8000/upload/', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            console.log('File uploaded successfully!');
            result = await response.json();
        } else {
            console.error('Failed to upload file');
        }
    } catch (error) {
        console.error(error);
    }

    return result;
}

const fetchResults = async (videoId) => {
    
    let fetchedRegions = null;

    try {
        const response = await fetch(`http://127.0.0.1:8000/videos/${videoId}`, {
            method: 'GET'
        });

        if (response.ok) {
            console.log('Regions fetched successfully!');
            fetchedRegions = await response.json();
        } else {
            console.error('Failed to fetch regions');
        }
    } catch (error) {
        console.error(error);
    }
    return fetchedRegions;
}

function helloWorld(){
    console.log("hello")
}


function getURL(videoId, dubType, fileName){
    return `https://tiktoktechjam-2024.s3.ap-southeast-1.amazonaws.com/${videoId}/${dubType}_${fileName}`
}
export { uploadVideoFile, fetchResults, helloWorld, getURL}