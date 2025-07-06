# 🔍 `search` – AI-Powered Command Generator & Explainer for Terminal

A lightweight Python-based CLI tool that uses Google Gemini to generate and explain shell commands based on user input. No more browser detours during development. Just `search` and get the results instantly.

> "Who likes to visit the browser every time? 🙂"

---

## ✨ Features

- 🧠 Generates and explains CLI commands in a single line.
- 📘 Gives a usage example for better understanding.
- ⚡ Uses `gemini-1.5-flash-latest` (Google Gemini API) for fast results.
- ⏱️ Displays time taken for the response in milliseconds.
- 🖥️ Works fully within your terminal — no context switching.
- ❓ Prints usage help if no command is passed.

---

## 🚀 Example Usage

```bash
search git commands to configure username and email globally

```

**Output:**
```
It sets the username and email used for Git commits globally, preventing you from having to specify them for each repository;  `git config --global user.name "Your Name" && git config --global user.email "your.email@example.com"`

✨ Time taken: 2524 ms
```

---

## ⚙️ Installation

### 1. Install the required Python package

Ensure Python 3+ is installed:

```bash
pip install google-generativeai

or

pip install -r requirements.txt

```

### 2. Add your Gemini API Key

- Generate new API key from [Google AI Studio](https://aistudio.google.com/apikey)
- Open .zshrc or .bash depending on your system.
- Add this line then save the file and reload the terminal.
```python
export GEMINI_API_KEY="your-gemini-api-key"
```

- Confirm it worked (gives API key as output)

```python
echo $GEMINI_API_KEY
```

### 3. Rename your script (with no extension for clean usage)

```
mv search.py search
```
### 4. Make the script executable

```bash
chmod +x search
```

### 5. Move it to your $PATH to use it globally and reload the terminal

```bash
sudo mv search /usr/local/bin/
```

Now you can call it like any other shell command:

```bash
search docker stop $(docker ps -q)
```

---

## 📂 Project Structure

```
search/
├── search.py            # Python script
└── README.md            # Project documentation
└── requirements.txt     # Dependencies
```

---

## 🧠 How It Works

1. Uses `sys.argv` to collect the shell command from your input
2. Calls Gemini API's `generate_content()` with a natural prompt
3. Displays the explanation and example usage with response time in ms

If no input is passed:

```bash
search
```

You'll see:

```
Usage: search <your-command>
```

---

## 📚 Examples

```bash
search git reset --hard
```

```bash
search how to install nodemon globally
```


---

## 🧑‍💻 Built With

- 🐍 Python 3
- 🔮 Google Gemini API (google-generativeai)
- 💡 Developer laziness 😄 (the good kind)

---

## 📫 Contact

Made with ❤️ and ☕️ by Prajwal Gaikwad

If this tool saved you a trip to Browser, drop a ⭐!
