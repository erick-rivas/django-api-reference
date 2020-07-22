# Create virtual environment

python3 -m venv .venv
. .venv/bin/activate

# Install dependencies

pip3 install -r requirements.txt

# Create .env (settings)

cp .env.example .env.dev
cp .env.example .env.prod