# 📘 Git & GitHub Workflow Documentation

## 🔹 Section A – Conceptual Answers

### What is Git?
Git is a distributed version control system used to track changes in source code and collaborate with developers.

### What is GitHub?
GitHub is a cloud platform that hosts Git repositories and enables collaboration.

### Git Repository
A Git repository is a project folder tracked by Git.

### Working Directory vs Staging vs Repository
- Working Directory → where files are edited
- Staging Area → files ready to commit
- Repository → committed history

### Git Commit
A snapshot of changes with a message.

### Git Branch
A separate line of development.

### git pull vs git fetch
- `git fetch` → download changes only
- `git pull` → download + merge

### git merge vs git rebase
- merge → keeps history
- rebase → rewrites history

### .gitignore Purpose
Prevents unnecessary files from being tracked.

### Why avoid secrets?
To protect sensitive data like passwords and API keys.

---

## 🔹 Practical Tasks

### Task 1 – Git Configuration
- Configured username and email
- Verified using:

git config --global --list


---

### Task 2 – Git Workflow

Explained flow:

Working → Staging → Commit → Push

Commands used:
- git status
- git add
- git commit
- git log
- git diff

---

### Task 3 – Branching

Created:
- main
- develop
- feature/day-2-git-workflow

Used:
- git branch
- git switch
- git switch -c

---

### Task 4 – Commits

Created meaningful commit:

docs: update internship project documentation


---

### Task 5 – Remote Repository

Commands:
- git remote -v
- git push
- git pull
- git fetch

---

### Task 6 – .gitignore

Ignored:
- __pycache__/
- venv/
- .env
- logs
- IDE files

---

### Task 7 – Merge & Conflict

Conflict occurred when:
- Same file edited in two branches

Resolution:
- Manually edited conflict markers
- Used:

git add .
git commit


---

### Task 8 – Workflow Simulation


main → develop → feature → commit → push → merge


---

## ✅ Conclusion

Learned complete Git workflow including branching, commits, merging, and collaboration.

---
------------------------------------------------------------------------------------------------------------------------
# Hospital Management System — Odoo 19 Internship

A step-by-step training project to design and build a **Hospital Management System** on **Odoo 19 (Community Edition)**, developed as part of a structured Odoo Technical Internship.

| | |
|---|---|
| **Project** | Hospital Management System (Odoo 19 Community) |
| **Assigned To** | Ameer Nawaz — Odoo Technical Intern |
| **Reporting To** | Technical Team Leader |
| **Framework** | Odoo 19 |
| **Database** | PostgreSQL |
| **Language** | Python 3 / XML |

---

## About This Project

This repository documents the internship journey of building a Hospital Management System from the ground up on Odoo 19 — starting with framework fundamentals (architecture, ORM, module structure) before moving into custom module development (patients, doctors, appointments, consultations, prescriptions, billing).

Each day of the internship has a defined objective, a set of practical tasks, and required deliverables, all tracked in this repository.

---

## Repository Structure

```
hospital-management-odoo19-internship/
│
├── documentation/
│   └── architecture/
│       ├── odoo-architecture.md      # Odoo framework architecture notes
│       ├── module-analysis.md        # Comparison of existing Odoo modules
│       ├── orm-overview.md           # ORM, Registry & request-flow notes
│       └── hospital-architecture.md  # Planned HMS module architecture
│
├── custom_addons/                    # Custom modules (development starts later)
│
├── screenshots/                      # Supporting screenshots for each day's task
│
└── README.md
```

---

## Progress Log

### ✅ Day 3 (Monday) — Understanding Odoo 19 Architecture, Addons & Module Structure

**Objective:** Build a solid conceptual foundation of the Odoo framework — architecture, addons, modules, dependencies, Registry, ORM, and request flow — before starting custom module development.

**Completed:**
- [x] Reviewed the Odoo 19 source structure (`odoo/`, `addons/`, `odoo-bin`, `http.py`, `models.py`, `fields.py`, `api.py`, `service/`, `tools/`)
- [x] Analyzed and compared the structure of three existing Odoo modules
- [x] Documented module dependencies (`depends`), the dependency graph, and install/upgrade/loading order
- [x] Studied the Odoo Registry — what it is, when it's created, and its role in the ORM
- [x] Studied the ORM architecture (Model → Field → Record → Recordset → Environment → PostgreSQL)
- [x] Mapped the browser → HTTP request → controller → ORM → PostgreSQL → response request flow
- [x] Performed a full technical structure review of one standard Odoo module
- [x] Drafted the initial high-level module plan for the Hospital Management System:
  - `hospital_base`
  - `hospital_patient`
  - `hospital_doctor`
  - `hospital_appointment`
  - `hospital_consultation`
  - `hospital_prescription`
  - `hospital_billing`
- [x] No Odoo core files were modified
- [x] Documentation committed to Git

**Deliverables produced:**
- Odoo Architecture Documentation
- Addons & Module Structure Documentation
- Three Existing Module Analysis
- Module Dependency Analysis
- Registry Explanation
- ORM Architecture Diagram
- Odoo Request Flow Diagram
- Existing Module Architecture Diagram
- Hospital Management System Architecture Plan
- Supporting screenshots

**Git commit:**
```bash
git add .
git commit -m "docs: add Odoo 19 architecture and module structure"
git push origin feature/day-3-odoo-architecture
```

---

## Documentation

Detailed write-ups for each topic live under [`documentation/architecture/`](documentation/architecture/):

- **[odoo-architecture.md](documentation/architecture/odoo-architecture.md)** — Server, PostgreSQL, addons vs. modules, high-level architecture
- **[module-analysis.md](documentation/architecture/module-analysis.md)** — Comparison table of three existing Odoo modules
- **[orm-overview.md](documentation/architecture/orm-overview.md)** — Registry, ORM, and request-flow explanations
- **[hospital-architecture.md](documentation/architecture/hospital-architecture.md)** — Planned Hospital Management System module breakdown

---

## Development Guidelines

- Custom development stays isolated in `custom_addons/` — Odoo core files are never modified.
- Modules are kept focused on a single business responsibility rather than one large monolithic app.
- Dependencies are declared explicitly and correctly in each module's `__manifest__.py`.
- Work proceeds day-by-day per the internship plan, with documentation and screenshots committed alongside each milestone.

---

## Author

**Ameer Nawaz** — Odoo Technical Intern