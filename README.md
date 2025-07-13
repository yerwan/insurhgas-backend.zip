
# 🧠 YT Shorts Backend

A complete backend for generating short clips from YouTube videos with subtitles, transcripts, and virality score.

---

## 🚀 Features

- ✅ User Signup/Login (with token support)
- 🎞️ Input YouTube link + Time range → Output short video
- 📝 Automatic Subtitle extraction and overlay
- 📜 Full transcript generation (for script output)
- 🎯 Virality Score Prediction (10% - 100%)
- 🔁 Short video preview + download support
- 🎨 Multiple subtitle styles (classic, minimal, bold)
- 📱 Responsive frontend integration with result page

---

## ⚙️ Backend API Endpoints

| Method | Endpoint            | Description                     |
|--------|---------------------|---------------------------------|
| GET    | `/`                 | Check if backend is running     |
| POST   | `/signup`           | Create user                     |
| POST   | `/login`            | Login and get access token      |
| POST   | `/make_clip`        | Generate clip from YT link      |
| GET    | `/get_subtitles`    | Get raw subtitles text          |
| GET    | `/get_transcript`   | Get transcription text          |
| GET    | `/preview_clip`     | Play final short clip           |
| GET    | `/download_clip`    | Download clip with subtitles    |

---

## 🛠️ Deployment Guide (Render)

### 1. Upload Code to GitHub
- Go to [GitHub](https://github.com)
- Create new repo (e.g., `yt-shorts-backend`)
- Upload your backend folder or drag the ZIP contents

### 2. Deploy on [Render](https://render.com)
- Create new ➜ Web Service
- Connect GitHub ➜ Select your repo
- Runtime: `Python`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
- Set Environment: `PYTHON_VERSION = 3.10.8`

### 3. Done!
- You’ll get a public URL like:
  ```
  https://insurhgas-backend-zip.onrender.com
  ```

---

## 🧪 API Testing with Postman

1. Download this collection:  
   [YT_Shorts_Backend_Collection.postman_collection.json](./YT_Shorts_Backend_Collection.postman_collection.json)

2. Open [Postman](https://www.postman.com/)
3. Import JSON ➜ Use your backend URL in `{{base_url}}`

---

## 🖼️ Example Workflow

1. Input:  
   `https://youtube.com/watch?v=dQw4w9WgXcQ`

2. Set:  
   - Start: `00:00:10`  
   - End: `00:00:25`  
   - Subtitle Style: `classic`

3. Output:
   - 🎬 Video preview page on frontend
   - 📝 Full transcript (downloadable)
   - 📥 Download final clip
   - 🔥 Virality score shown (e.g., 87%)

---

## 📁 Extras

✅ Supports:
- Subtitle font & color customization  
- Multistyle subtitles (classic, bold, minimal)
- Mobile/desktop responsive result page  
- Easy domain switch — just change API base URL

---

## 💡 Tips

- Use `make_clip` after login (token not required for demo)
- If clip is stuck, check YouTube link format or start/end times
- Always use valid `hh:mm:ss` format

---

Developed with ❤️ for faceless content creators
