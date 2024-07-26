# Import necessary classes from different modules
from Links_Generator import YouTubePlaylist
from Transcript_Generator import Transcript_Generator
from generator import Generator
from retriever import Retriever
from speech_conversion import SpeakText, TextToSpeech

# Prompt the user to enter the YouTube playlist URL
url = str(input("Enter the YouTube playlist URL: "))

# Initialize the YouTubePlaylist object with the provided URL
yt_playlist = YouTubePlaylist(url)

# Get the list of video links from the playlist
links = yt_playlist.get_playlist_items()

# Initialize a counter for video numbering
i = 1

# Loop through each video link in the playlist
for link in links:
    # Initialize the Transcript_Generator object with the video link
    init_transcript = Transcript_Generator(link)
    
    # Generate the transcript for the current video
    transcript = init_transcript.generate_Transcript()
    
    # Prepare the input string for the current video with its transcript
    inp = f"Video {i}:\n {transcript}"
    
    # Print the input string (video number and its transcript)
    print(inp)
    
    # Initialize the Generator object with the transcript
    generator = Generator(transcript)
    
    # Generate embeddings for the transcript
    embeddings = generator.generate_embeddings()
    
    # Increment the video counter
    i += 1

# Initialize the Retriever object
init_retriever = Retriever()

# Continuously prompt the user for questions until they type 'exit'
while True:
    # Prompt the user to ask a question
    source = str(input("""Select the source of input: 
        1. Voice
        2. Text"""))

    if source == "1":
        question = TextToSpeech()  # Get the question from voice input
    elif source == "2":
        question = str(input("Enter your question('write 'exit' to terminate'): "))
    else:
        print("Invalid input. Please try again.")
        continue

    # Check if the user wants to exit
    if question.lower() == "exit":
        break
    
    # Generate an answer for the user's question
    answer = init_retriever.generate_answers(question)
    
    # Print the answer
    print(answer)
    SpeakText(answer)