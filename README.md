\# Smart Gallery AI

## Deploying safely

This project processes personal photos and face embeddings. Before publishing it, use PostgreSQL and private S3-compatible object storage, set the environment variables in `.env.example`, and run it behind HTTPS. `render.yaml` provides a Docker-based Render blueprint; set the generated service URL in `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` before first deploy. The app's privacy notice and consent checkbox are product safeguards, not a substitute for legal advice or local privacy-law review.

Run migrations before serving traffic:

```bash
python core/manage.py migrate
python core/manage.py collectstatic --noinput
gunicorn --chdir core --bind 0.0.0.0:8000 core.wsgi:application
```



An AI-powered smart photo gallery built with Django, InsightFace, OpenCV, and SQLite.



Smart Gallery AI automatically analyzes uploaded photos, detects faces, generates face embeddings, groups people, organizes photos by events, and enables intelligent person-based photo discovery.



\## ✨ Features



\- 👤 Face detection and recognition

\- 🧠 AI-based face embeddings using InsightFace

\- 👥 Automatic grouping of photos by person

\- 📸 Smart photo gallery

\- 🔎 Person-based photo search

\- 📅 Event-based photo organization

\- 🖼️ Automatic face crop generation

\- 🎨 Person collage generation

\- 🔐 User authentication

\- 💾 SQLite database

\- ⚡ Background photo processing



\## 🛠️ Tech Stack



\### Backend

\- Python

\- Django

\- SQLite



\### AI \& Computer Vision

\- InsightFace

\- ONNX Runtime

\- OpenCV

\- NumPy

\- scikit-learn

\- Pillow



\### Frontend

\- HTML

\- CSS

\- Django Templates



\## 🏗️ Project Structure



```text

smart-gallery-ai/

│

├── core/

│   ├── manage.py

│   ├── core/

│   │   ├── settings.py

│   │   ├── urls.py

│   │   ├── asgi.py

│   │   └── wsgi.py

│   │

│   └── gallery/

│       ├── ai\_logic.py

│       ├── event\_logic.py

│       ├── collage\_maker.py

│       ├── models.py

│       ├── views.py

│       ├── forms.py

│       ├── templates/

│       └── migrations/

│

├── requirements.txt

├── runtime.txt

└── .gitignore

