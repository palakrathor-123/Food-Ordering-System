# Food-Ordering-System for Restaurant


An intelligent voice-based food ordering system that allows users to place orders using natural language speech. The system converts speech to text in real-time, matches user intent with menu items using NLP techniques, and generates an order summary with pricing.

---

## 🚀 Features
*🎤 Real-time Speech-to-Text: High-accuracy voice capture using the Web Speech API.
*🧠 Semantic Item Matching: Powered by Sentence Transformers and FAISS for smart menu searches.
*🔢 Intelligent Extraction: Advanced Regex logic to identify quantities and item variants (e.g., "three farmhouse pizzas").
*🖥️ Professional Dashboard: A clean, centered, and responsive UI for real-time order tracking.
*⚡ Async Backend: Built with FastAPI for ultra-fast processing and low-latency responses.
*📑 Automatic Billing: Real-time generation of order summaries with precise price calculations.


---

## 🛠️ Tech Stack

- 🌐**Frontend:** HTML, JavaScript (Web Speech API)
- 🐍**Backend:** FastAPI (Python)
- 🧠**AI/NLP:** Rule-based + Regex + Matching Logic
- 📁**Database:** JSON (Menu storage)
- 🌐**Server:** Uvicorn

---

## 📁 Project Structure


voice-ordering-app/
│
├── 📁 app/
│ ├──🔌 api/
│ │ └── routes.py
│ ├──⚙️ services/
│ │ ├── matching_service.py
│ │ ├── order_service.py
│ │ └── embedding_service.py
│ └── main.py
│
├── 📊 data/
│ └── 🍕 menu.json
│
├── 🎨  frontend/
│ └──📄 index.html
│
├── 📜 scripts/
│ └──🏗️ build_index.py
│
├── 📝 requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Ruchi-novadule/voice-ordering-ai-app.git 
cd voice-ordering-ai-app
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Backend Server
uvicorn app.main:app --reload
4️⃣ Run Frontend
Open frontend/index.html
or use live server in vs code

🎯 Usage Guide
Open frontend/index.html in your browser.
Click the "Start Speaking" 🟢 button.
Place your order: "I want chocolate brownie" 🍔🥤.
View the Matched Items and Order Summary instantly.
The system will automatically disconnect 🔴 once the order is finalized.

📊 Sample Output Example
Matched Items:
Diet Coke
Order Summary:
Diet Coke x1 = ₹50
Total Summary:
Items: 1
Total Amount: ₹50✅

🧠 How It Works
🎤 Speech is captured using Web Speech API
📝 Converted to text in real-time
🔍 Text processed using NLP logic
🍔 Items matched from menu
🔢 Quantities extracted using regex
🧾 Order summary generated
💰 Total price calculated
🔥 Future Enhancements
🔊 Voice response (Text-to-Speech)
📱 Mobile responsive UI
🧠 ML-based recommendation system
💳 Payment integration
🛒 Cart management system
🌍 Multi-language support
📸 Screenshots
---
## Dashboard Preview
<img width="1352" height="536" alt="Image" src="https://github.com/user-attachments/assets/7459ec67-66d4-4cf5-ba2f-6cfe7cbf49a1" />

<img width="1181" height="494" alt="Image" src="https://github.com/user-attachments/assets/7bfed056-2a9b-4b9f-bbcf-260fbc24e453" />

<img width="1120" height="476" alt="Image" src="https://github.com/user-attachments/assets/24914245-986b-46ea-824d-f64c84a767e4" />

<img width="628" height="553" alt="Image" src="https://github.com/user-attachments/assets/932306f0-5b14-489c-9277-247819de1a5e" />
---
This project demonstrates real-world applications of:

AI in food ordering systems
Voice-based interfaces
NLP-based intent recognition
Automation in restaurants
👩‍💻 Author

Palak Rathor

⭐  Support

If you found this project helpful, please consider giving it a ⭐ on GitHub!
