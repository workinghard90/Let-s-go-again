import nltk
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_nltk_resources():
    """Download required NLTK resources"""
    
    nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
    if not os.path.exists(nltk_data_path):
        os.makedirs(nltk_data_path)
        
    # Set NLTK data path
    nltk.data.path.append(nltk_data_path)
    
    resources = [
        'vader_lexicon',  # For sentiment analysis
        'punkt',          # For tokenization
        'stopwords',      # For stopwords removal
        'wordnet',        # For word meanings
    ]
    
    logger.info(f"Downloading NLTK resources to {nltk_data_path}")
    
    for resource in resources:
        try:
            logger.info(f"Downloading {resource}...")
            nltk.download(resource, download_dir=nltk_data_path, quiet=False)
            logger.info(f"Successfully downloaded {resource}")
        except Exception as e:
            logger.error(f"Error downloading {resource}: {e}")
    
    logger.info("NLTK resources download completed")
    
if __name__ == "__main__":
    download_nltk_resources()