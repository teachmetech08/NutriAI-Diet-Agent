# NutriAI — Multi-Regional Full-Stack Indian Diet & Health Agent

NutriAI is a responsive, full-stack health web application that serves tailored dietary blueprints, caloric breakdowns, and regional Indian meal plans.

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Marked.js
- **Backend:** Python, Flask
- **LLM Infrastructure:** IBM watsonx.ai Runtime
- **Model Engine:** Meta Llama 3.3 70B Instruct

## ⚡ Architecture Flow
User UI Input ➔ Flask API Server ➔ `ibm-watsonx-ai` SDK ➔ IBM Cloud Sydney Cluster (`au-syd`) ➔ Llama 3.3 70B Inference ➔ Structured Markdown UI Stream.

## 📸 Application Previews

### 🤖 AI Nutrition Agent Chat
![AI Agent Chat Initial](assets/chat-initial.png)

### 📊 South Asian BMI Diagnostic Tool
![BMI Calculator](assets/bmi-calculator.png)

### 🗓️ Weekly Regional Indian Meal Planner
![Meal Planner Grid](assets/meal-planner.png)

### 👥 Multi-Profile Family Tracking
![Family Profiles](assets/family-profiles.png)

### 💬 Tailored Nutritional Feedback Stream
![Active Agent Chat Response](assets/chat-response.png)