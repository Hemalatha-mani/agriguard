# AgriGuard — Early Detection and Management of Crop Diseases and Pest Infestations

Full-stack application for detecting crop diseases from leaf photos using a
trained Keras CNN, plus reference content on remedies, prevention, farming
practices, and an agricultural chatbot.

**Stack:** React + Vite · FastAPI · PostgreSQL · TensorFlow/Keras
**Deploy targets:** Frontend → Vercel · Backend → Render

---

## ⚠️ Before you do anything else

This project ships with **no fake AI logic and no hardcoded secrets**. That
means two things are required before it will actually run:

1. **Model file**: copy your trained `crop_disease_model_final.keras` into
   `backend/ml_models/`. Without it, `/api/predict` will return a clear
   `503` error explaining exactly what's missing — it will never return a
   fabricated prediction.
2. **Environment variables**: copy `.env.example` → `.env` in both
   `backend/` and `frontend/` and fill in real values (database URL, JWT
   secret, API URL). Nothing will run with placeholder values.

**Also verify the model contract** in `backend/app/ai/labels.py` and
`backend/app/ai/preprocess.py`: the class order and pixel normalization
(currently `/255.0` → `[0,1]`) must exactly match how your model was
trained, or predictions will be silently wrong even though no error is
thrown. If your training pipeline used `preprocess_input` from
`tf.keras.applications` (e.g. MobileNetV2's `[-1,1]` scaling), update
`normalize()` accordingly.

---

## Project structure

```
backend/
  app/
    main.py            # FastAPI entrypoint
    config.py           # env-based settings
    database.py          # SQLAlchemy engine/session
    models/               # ORM models (User, Prediction, ChatMessage)
    schemas/               # Pydantic schemas
    routes/                 # one router per resource
    auth/                    # password hashing, JWT, current-user dependency
    ai/                       # model loader, preprocessing, class labels
    chatbot/                   # keyword-based chatbot engine + knowledge base
    data/                        # structured reference data (diseases, remedies, etc.)
  ml_models/                      # put crop_disease_model_final.keras here
  alembic/                          # DB migrations
  tests/
  requirements.txt
  .env.example

frontend/
  src/
    pages/              # 11 pages (Login, Home, AI Detect, ... Chatbot History)
    components/           # layout, ai-detect, diseases, chatbot, common
    api/                     # Axios service layer (one file per resource)
    context/                  # AuthContext
    styles/                     # green agriculture theme + responsive rules
  .env.example
  vercel.json

render.yaml
vercel.json
.gitignore
```

---

## Local setup

### 1. Database
Create a local PostgreSQL database, e.g.:
```bash
createdb crop_disease_db
```

### 2. Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # then edit DATABASE_URL, JWT_SECRET_KEY, ALLOWED_ORIGINS
# place crop_disease_model_final.keras into ml_models/
uvicorn app.main:app --reload
```
Visit `http://localhost:8000/docs` for interactive API docs, and
`http://localhost:8000/api/health` to check DB connectivity and whether the
model is loaded (it lazy-loads on first `/api/predict` call, so `model_loaded`
will read `false` until then).

### 3. Frontend
```bash
cd frontend
npm install
cp .env.example .env               # set VITE_API_URL=http://localhost:8000
npm run dev
```
Visit `http://localhost:5173`.

### 4. Create an account
There's no seeded user. Use the "Register" link on the Login page, or:
```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"farmer1","email":"farmer1@example.com","password":"strongpassword123"}'
```

---

## Running tests
```bash
cd backend
pytest -v
```
The included test is a placeholder — real endpoint tests need a running
Postgres test database and the actual model file, neither of which can be
provided in this repository. Wire `DATABASE_URL` to a disposable test DB and
add tests per route using `httpx`/`pytest`.

---

## Deployment

### Backend → Render
1. Push this repo to GitHub.
2. In Render, choose **New → Blueprint** and point it at this repo (it will
   read `render.yaml` and provision a web service + a free Postgres
   instance automatically), **or** create the web service manually:
   - Root directory: `backend`
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
3. Add environment variables in the Render dashboard (Environment tab):
   `DATABASE_URL` (from your Render Postgres instance's "Internal Database
   URL"), `JWT_SECRET_KEY` (generate with `openssl rand -hex 32`),
   `ALLOWED_ORIGINS` (your Vercel URL, added after step below).
4. **Model file**: Render's free tier has limited disk and RAM.
   `tensorflow-cpu` plus the model file can be heavy — if the free plan's
   RAM (512 MB) isn't enough, you'll need a paid plan. Get the model onto
   the server via one of:
   - Git LFS (if the repo hosts it)
   - A small startup step that downloads it from S3/GCS using a signed URL
     stored in an env var
5. Once deployed, confirm `https://your-service.onrender.com/api/health`
   returns `{"status": "ok", ...}`.

### Frontend → Vercel
1. In Vercel, import the same repo.
2. Set **Root Directory** to `frontend`.
3. Framework preset: Vite (auto-detected).
4. Add environment variable `VITE_API_URL` = your Render backend URL
   (no trailing slash), e.g. `https://crop-disease-backend.onrender.com`.
5. Deploy. Vercel will run `npm install && npm run build` automatically.
6. Go back to Render and set `ALLOWED_ORIGINS` to your new Vercel URL
   (e.g. `https://your-app.vercel.app`), then redeploy the backend so CORS
   allows requests from it.

### Post-deploy checklist
- [ ] `GET /api/health` on Render returns `database: ok`
- [ ] Register + login works from the deployed frontend
- [ ] `/api/predict` returns a real prediction (not a 503) once the model
      file is in place
- [ ] Browser devtools show no CORS errors
- [ ] All 11 pages load and fetch data without errors

---

## Notes on what is genuinely tested vs. structurally correct

This project was generated in a sandboxed environment without network
access, a live PostgreSQL instance, or the actual `.keras` model file. That
means:
- **Verified**: Python syntax of every backend file, the import graph
  (no circular/broken imports), consistent route/schema naming.
- **Correct-by-construction but not live-tested**: actual DB queries against
  a real Postgres instance, actual model inference, `npm run build`,
  live Render/Vercel deployment.

Run the local setup steps above and fix anything environment-specific
(dependency versions, Python/TensorFlow compatibility on your OS) as it
comes up — the model loader and endpoints are written to fail with clear,
specific error messages rather than hiding problems.
