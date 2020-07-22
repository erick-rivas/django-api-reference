# Create virtual environment

python -m venv .venv
. .\.venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt

# Create .env (settings)

cp .env.example .env.dev
cp .env.example .env.prod
