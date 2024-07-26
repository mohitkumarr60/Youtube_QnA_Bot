from llama_index.readers.youtube_transcript import YoutubeTranscriptReader

class Transcript_Generator:
  def __init__(self,url):
    self.url = url
    self.loader = YoutubeTranscriptReader()

  def generate_Transcript(self):
    documents = self.loader.load_data(
      ytlinks= [self.url]
    )
    return documents
    