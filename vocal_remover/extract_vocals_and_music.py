# Python 3.10.16
from pathlib import Path
from typing import Optional

import ffmpeg
from audio_separator.separator import Separator
import logging

logger = logging.getLogger(__name__)

# UVR Document for models
# https://docs.google.com/document/d/17fjNvJzj8ZGSer7c7OFe_CNfUKbAxEh_OBv94ZdRG5c/edit?pli=1&tab=t.0#heading=h.rz0d5zk9ms4w

def extract_audio_to_wav(video_path: Path, wav_path: Path, sample_rate: int = 44100) -> None:
    """Extracts the audio track from *video_path* to *wav_path* using FFmpeg.

    The audio is encoded as 16-bit PCM (wav) with 2 channels.
    """
    logger.info("Extracting audio from %s -> %s", video_path, wav_path)
    (
        ffmpeg.input(str(video_path))
        .output(str(wav_path), acodec="pcm_s16le", ac=2, ar=str(sample_rate))
        .overwrite_output()
        .run(quiet=True)
    )
    logger.info("Audio extraction complete")


def separate_stems(audio_path: Path, output_dir: Path, model_filename: Optional[str] = None) -> None:
    """Runs UVR separation on *audio_path* and writes stems to *output_dir*."""
    logger.info("Separating stems for %s", audio_path)

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    separator = Separator(output_dir=str(output_dir))
    separator.load_model(model_filename=model_filename)

    stem_files = separator.separate(str(audio_path))
    logger.info("Separation finished – files created:\n%s", "\n".join(stem_files))

if __name__ == "__main__":

    # Separate the audio using vocal remover
    separate_stems(Path("/Users/rajan/dev/youtube/vocal_remover/seperated_output_dir/Qayde-Se-arijit_(Vocals)_UVR_MDXNET_KARA_2.wav"), Path("/Users/rajan/dev/youtube/vocal_remover/seperated_output_dir"), model_filename="UVR_MDXNET_KARA_2.onnx")