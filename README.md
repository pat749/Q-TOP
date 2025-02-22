# 🚀 Flask HTOP Monitor

A simple **Flask-based** web application that displays **system information** and real-time `top` command output via the `/htop` endpoint.  

## 📌 Features
- Displays:
  - ✅ Your Full Name  
  - ✅ System Username  
  - ✅ Server Time (IST)  
  - ✅ Real-time `top` command output  
- Runs on **GitHub Codespaces, Docker, or Any Cloud Platform**  
- Exposes port `5000` for public access  

## 🚀 Quick Start  

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/flask-htop-app.git
cd flask-htop-app
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Flask App**
```bash
python app.py
```
Access it at:  
👉 **http://localhost:5000/htop**  

---

## 🌍 Deploy on GitHub Codespaces
1. Open the repository in **GitHub Codespaces**.  
2. Run:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
3. Expose **port 5000** as **Public**.  
4. Access:  
   ```
   https://your-codespace-5000.app.github.dev/htop
   ```

---

## 🐳 Docker Deployment
```bash
docker build -t flask-htop .
docker run -p 5000:5000 flask-htop
```
Then, visit:  
👉 **http://localhost:5000/htop**  

---

## 📜 License
This project is licensed under the **MIT License**.

---

🔗 **Submit Links:**
- **Live Endpoint:** `[Your Codespace URL]/htop`
- **GitHub Repo:** `https://github.com/your-username/flask-htop-app`

---

**👨‍💻 Developed by Durgesh Patel** 🚀  
