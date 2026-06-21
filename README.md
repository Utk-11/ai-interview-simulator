# 🏢 Real-Time AI Technical Interview Simulator & Evaluation Dashboard

A full-stack software prototype engineered to simulate rigorous corporate technical interviews. The system dynamically generates context-aware engineering questions based on selected job roles, securely processes candidate technical answers using an isolated environment handler, and provides detailed feedback scores utilizing the **Google Gemini 2.5 Flash** model via the official `google-genai` SDK.

---

## 🛠️ Tech Stack & Architecture

* **Backend Core:** Python 3.14+
* **AI Integration:** Google GenAI SDK (`gemini-2.5-flash`)
* **Frontend Interface:** Gradio (Soft Theme Engine)
* **Environment Security:** Python-Dotenv (Zero-leak configuration)
* **Quality Assurance:** PyTest (Automated Input Validation Coverage)

---

## 🚀 Key Engineering Features

1. **Context-Aware Role Simulation:** Leverages advanced system instructions to lock the LLM into a rigorous "Senior Technical Interviewer" persona.
2. **Defensive Input Validation Layer:** Intercepts invalid, empty, or whitespace-only submissions locally to eliminate wasteful cloud API token utilization.
3. **Automated Regression Testing:** Integrated unit test suite to programmatically verify frontend-to-backend edge-case stability.
4. **Secure Secret Management:** Cryptographic API keys are completely decoupled from source control using localized configuration mapping.

---

## 🏃‍♂️ Local Installation & Setup

### 1. Clone the Architecture
```bash
git clone [https://github.com/Utk-11/ai-interview-simulator.git](https://github.com/Utk-11/ai-interview-simulator.git)
cd ai-interview-simulator