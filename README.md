# VisualThreatAI

VisualThreatAI is a Python-based tool designed to extract frames from videos and analyze both images and video frames using Google Gemini AI. This tool helps assess the likelihood of future risks by analyzing visual content and providing risk evaluation percentages. It supports both image and video-based analysis through an easy-to-use interface.

## Features

- **Video Frame Extraction**: Extracts frames from video files at specified time intervals.
- **Image and Frame Analysis**: Leverages the Gemini AI model to analyze images and provides a risk percentage indicating potential threats.
- **Batch Image Processing**: Automatically processes images from folders, making large-scale analysis easy.
- **Supports Local and Remote Images**: You can analyze both local image files and images from URLs.

## Technologies Used

- **Python 3.x**
- **PIL (Pillow)**: For image processing.
- **MoviePy**: For video frame extraction.
- **Google Generative AI (Gemini)**: For AI-powered content generation.
- **dotenv**: For managing environment variables.
- **Requests**: For handling URL-based image fetching.
- **NumPy**: For handling frame data arrays.

## Setup and Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/VisualThreatAI.git
    ```

2. Navigate into the project directory:
    ```bash
    cd VisualThreatAI
    ```

3. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Create the necessary directories for storing video frames and images:
    ```bash
    mkdir -p camera images
    ```

6. Create a `.env` file in the project root and add your API key for Gemini AI:
    ```
    API_KEY=your_gemini_ai_api_key_here
    ```

7. Run the main script:
    ```bash
    python main.py
    ```

## Usage

### Video Frame Extraction and Analysis
1. Place your video file in the `./videos` folder.
2. When prompted, choose the `video` option to extract frames from the video. Frames will be saved in the `./camera` folder.
3. After the extraction, the tool will automatically analyze the frames using Gemini AI and provide a percentage risk for each frame.

### Image Analysis
1. Place images in the `./images` folder for image analysis.
2. You can also place images in the `./camera` folder (frames extracted from video).
3. When prompted, choose the `image` option to analyze all images in the `./images` and `./camera` folders.
4. The tool will output the percentage likelihood of future threats for each image.

### Combined Analysis
1. To perform both video frame extraction and image analysis, select the `all` option.
2. The tool will first extract frames, analyze them, and then analyze all other images.

### Prompts
The tool uses the following default AI prompt for analysis:
