# Contributing to School Library Management System 📚

Thank you for your interest in contributing to our project! 🎉  
We welcome contributions of all kinds, from fixing bugs to adding new features.

---

## 📌 How to Contribute

### **1️⃣ Fork the Repository**
- Click the **Fork** button at the top right of this repository.
- Clone your forked repository:
  ```sh
  git clone https://github.com/YOUR-USERNAME/library-management-system.git
- Navigate to the project directory:
  ```sh
  cd library-management-system

### **2️⃣ Set Up the Project Locally**
#### **🔹 Backend (Django)**
- Create a virtual environment:
  ```sh
  python -m venv venv
  source venv/bin/activate  # For Linux/Mac
  venv\Scripts\activate  # For Windows
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  
- Apply migrations:
  ```sh
  python manage.py migrate

#### **🔹 Frontend (PyQt6)**
- Ensure PyQt6 is installed:
  ```sh
  pip install PyQt6
  ```

### **3️⃣ Create a New Branch**
- Always work on a separate branch:
  ```sh
  git checkout -b feature-branch
  ```

### **4️⃣ Make Your Changes**
- Implement the feature or fix the bug.
- Run tests to ensure everything works.
- Format your code using:
  ```sh
  black .  # For Python
  ```

### **5️⃣ Commit Your Changes**
- Write a clear commit message:
  ```sh
  git add .
  git commit -m "📚 Added book reservation system"
  ```
- Push your changes:
  ```sh
  git push origin feature-branch
  ```

### **6️⃣ Create a Pull Request (PR)**
- Go to the **Pull Requests** tab in GitHub.
- Click **New Pull Request** and select your branch.
- Fill out the PR template and submit.

---

## 🔹 Contribution Guidelines
✔️ Follow the project's coding style.  
✔️ Keep PRs focused on a single issue or feature.  
✔️ Reference issues in commits (e.g., `Fixes #10`).  
✔️ Write meaningful commit messages.  
✔️ Be respectful in code reviews.  

---

## 🔥 Need Help?
If you have any questions, feel free to open an **issue** or ask in discussions.

Happy coding! 🚀
