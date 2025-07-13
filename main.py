from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import subprocess
import uuid

app = FastAPI()

VIDEO_DIR = "videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

class User(BaseModel):
    username: str
    password: str

class SubtitleRequest(BaseModel):
    youtube_url: str

class ClipRequest(BaseModel):
    youtube_url: str
    start_time: str
    end_time: str

class SubtitleStyleRequest(BaseModel):
    video_path: str
    subtitles: list
    font_size: int = 32
    font_color: str = "white"
    background_color: str = "black"
    position: str = "bottom"
    font_style: str = "bold"
    font_family: str = "Arial"

class ResizeRequest(BaseModel):
    video_path: str
    resolution: str  # e.g., "1080x1920"

class EnhanceRequest(BaseModel):
    video_path: str
    apply_filters: bool = True

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.post("/signup")
def signup(user: User):
    return {"message": f"User {user.username} signed up successfully."}

@app.post("/login")
def login(user: User):
    return {"message": f"User {user.username} logged in successfully."}

@app.post("/get-subtitles")
def get_subtitles(request: SubtitleRequest):
    return {"message": f"Subtitles fetched for: {request.youtube_url}"}

@app.post("/extract-clip")
def extract_clip(request: ClipRequest):
    clip_name = f"{uuid.uuid4()}.mp4"
    clip_path = os.path.join(VIDEO_DIR, clip_name)
    cmd = f"yt-dlp -f best -o - {request.youtube_url} | ffmpeg -ss {request.start_time} -to {request.end_time} -i - -c copy {clip_path}"
    subprocess.run(cmd, shell=True)
    return {"message": "Clip extracted", "clip_path": clip_path}

@app.post("/add-subtitles")
def add_subtitles(data: SubtitleStyleRequest):
    output_path = os.path.join(VIDEO_DIR, f"styled_{uuid.uuid4()}.mp4")
    input_path = data.video_path
    drawtext = f"drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='Subtitle':fontcolor={data.font_color}:fontsize={data.font_size}:box=1:boxcolor={data.background_color}@0.5:x=(w-text_w)/2:y=h-th-50"
    cmd = f"ffmpeg -i {input_path} -vf "{drawtext}" -codec:a copy {output_path}"
    subprocess.run(cmd, shell=True)
    return {"message": "Subtitles added", "output_path": output_path}

@app.post("/resize-video")
def resize_video(data: ResizeRequest):
    output_path = os.path.join(VIDEO_DIR, f"resized_{uuid.uuid4()}.mp4")
    cmd = f"ffmpeg -i {data.video_path} -vf scale={data.resolution} {output_path}"
    subprocess.run(cmd, shell=True)
    return {"message": "Video resized", "output_path": output_path}

@app.post("/enhance-video")
def enhance_video(data: EnhanceRequest):
    if not data.apply_filters:
        return {"message": "No enhancement applied."}
    output_path = os.path.join(VIDEO_DIR, f"enhanced_{uuid.uuid4()}.mp4")
    cmd = f"ffmpeg -i {data.video_path} -vf eq=brightness=0.05:contrast=1.3,unsharp {output_path}"
    subprocess.run(cmd, shell=True)
    return {"message": "Video enhanced", "output_path": output_path}

@app.get("/download/{filename}")
def download_video(filename: str):
    file_path = os.path.join(VIDEO_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=filename, media_type='video/mp4')
    return {"error": "File not found"}
