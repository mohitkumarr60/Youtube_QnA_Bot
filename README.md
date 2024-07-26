# <h1>YouTube Playlist Q&A Bot </h1> #


<h3> This project enables users to generate transcripts for videos in a YouTube playlist, create embeddings, and ask questions about the video content using a Gradio interface. </h3> 

# <h2>Features</h2> #

1. Extracts video links from a YouTube playlist.
2. Generates transcripts for each video.
3. Creates embeddings for the transcripts.
4. Provides a Q&A bot to answer questions about the video content.
5. Interactive web interface using Gradio.

# <h2> Installation # </h2> 

<h3> To get started with this project, follow these steps: </h3>

1. Clone the Repository:

   `git clone https://github.com/mohitkumarr60/qnabot `
   
   `cd qnabot`

3. Install the necessary dependencies:


4. Set up environment variables:

   Create a .env file in the project root and add your Gemini API key:

   `GEMINI_API_KEY=your_gemini_api_key`

   `YOUTUBE_API_KEY= your_youtube_api_key`

# <h2> Usage</h2>  #

<h3> Running the Application </h3>

1. Run the Gradio Interface:

   `python app.py`

   
2. Interact with the Web Interface:

   * Open the link provided by Gradio in your web browser.
   * Enter a YouTube playlist URL and click "Process Playlist" to generate transcripts and embeddings.
   * Ask questions about the video content in the playlist and get answers.


