Place `crop_disease_model_final.keras` in this folder before starting the
backend (or point MODEL_PATH in your .env at wherever you keep it).

This file is intentionally not committed to git (see .gitignore) since
trained model files are typically too large for a git repo. For deployment
on Render, either:
  1. Commit the model with Git LFS, or
  2. Download it at build/start time from cloud storage (S3, GCS, etc.)
     using a small startup script, or
  3. Include it directly in the deploy if small enough and your git remote
     allows it.
