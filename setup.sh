#!/bin/bash

# setup.sh – Shell script to set up Research Paper Analyzer Pro environment

echo "🔧 Setting up Research Paper Analyzer Pro..."

# Step 1: Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python before running this script."
    exit 1
fi

# Step 2: Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv rpa_env

# Step 3: Activate virtual environment
echo "⚙️ Activating virtual environment..."
source rpa_env/bin/activate

# Step 4: Install dependencies
if [ -f "requirements.txt" ]; then
    echo "📥 Installing dependencies from requirements.txt..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "❌ requirements.txt not found!"
    exit 1
fi

# Step 5: Create basic folder structure if not present
echo "📂 Creating directory structure..."
mkdir -p app/pages modules services assets/css assets/models assets/sample_papers notebooks data/train data/test

# Step 6: Confirm success
echo "✅ Setup completed successfully!"
echo "➡️ To activate the environment later, run: source rpa_env/bin/activate"
echo "➡️ To start the app, run: streamlit run app/main.py"
